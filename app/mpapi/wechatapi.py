import requests, json, os, time

from config import APP_ID, SECRET_KEY

try:
    import pylibmc
    mc = pylibmc.Client()
    def get_mc(): return mc.get('token')
    def set_mc(j): return mc.set('token', j)
except:
    TOKEN_DIR = os.path.join('app', 'mpapi', 'access_token.json')
    def get_mc():
        try:
            with open(TOKEN_DIR) as f: return f.read()
        except:
            with open(TOKEN_DIR, 'w') as f: return
    def set_mc(j):
        with open(TOKEN_DIR, 'w') as f: return f.write(j)

class AccessToken(object):
    def __init__(self, appId = APP_ID, secretKey = SECRET_KEY):
        self.appId = appId
        self.secretKey = secretKey
        self._set_token(*self._load_file_token())
    def _set_token(self, accessToken, endTime):
        self.__accessToken = accessToken
        self.__endTime = endTime
        self._dump_file_token(accessToken, self.__endTime)
    def _load_file_token(self):
        try:
            tokenDict = json.loads(get_mc())
            if tokenDict['accessToken'] and time.time() < tokenDict['endTime']:
                return tokenDict['accessToken'], tokenDict['endTime']
        except:
            pass
        for i in range(3):
            accessToken = self.get_token()
            if not accessToken is None: break
        else:
            raise Exception('Failed to get access token')
        endTime = time.time() + 7200
        return accessToken, endTime
    def _dump_file_token(self, accessToken, endTime):
        set_mc(json.dumps({
                'accessToken': accessToken,
                'endTime': endTime, }))
    def get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
        url = url%(self.appId, self.secretKey)
        r = requests.get(url).json()
        return r.get('access_token')
    # auto set access_token and gives token as first param, fns use this decorator should return None when failure
    def api(self, fn, *args, **kwargs):
        def _api(*args, **kwargs):
            if self.__endTime < time.time(): self._set_token(self.get_token(), time.time() + 7200)
            for i in range(3):
                result = fn(self.__accessToken, *args, **kwargs)
                if not result is None: break
                self._set_token(self.get_token(), time.time() + 7200)
            else:
                raise Exception('This function has wrong return values')
            return result
        return _api

at = AccessToken(APP_ID, SECRET_KEY)
api = at.api

@api
def get_ip_list(accessToken):
    url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'%accessToken
    r = requests.get(url).json()
    return r.get('ip_list')

@api
def send_text(accessToken, msg, toUserName):
    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s'%accessToken
    data = {
        'touser': toUserName,
        'msgtype': 'text',
        'text': { 'content': msg }
    }
    headers = { 'ContentType': 'application/json' }
    r = requests.post(url, data = json.dumps(data), headers = headers)
    return True

@api
def get_menu(accessToken):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s'%accessToken
    return requests.get(url).json()

@api
def set_menu(accessToken, menu):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'%accessToken
    r = requests.post(url, json.dumps(menu)).json()
    if r.get('errcode', -1) == 0:
        return True
    elif r.get('errcode', -1) == 48001:
        raise Exception(repr(r))
