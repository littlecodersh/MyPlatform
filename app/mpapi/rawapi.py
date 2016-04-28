import requests, json, os, time

from config import APP_ID, SECRET_KEY, BASE_URL

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
        self.__accessToken = None
        self.__endTime = None
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
            if self.__accessToken is None and self.__endTime is None: self._set_token(*self._load_file_token())
            if self.__endTime < time.time(): self._set_token(self.get_token(), time.time() + 7200)
            for i in range(3):
                result = fn(*args, accessToken = self.__accessToken, **kwargs)
                if not result is None: break
                self._set_token(self.get_token(), time.time() + 7200)
            else:
                raise Exception('This function has wrong return values')
            return result
        return _api

at = AccessToken(APP_ID, SECRET_KEY)

class ApiError(AttributeError):
    def __init__(self, path):
        self.message = "api has no attribute '%s'"%'.'.join(path)
        self.args = (self.message,)
class ApiFramework(object):
    def __init__(self, apiList = {}, warning = False, path = []):
        self.apiList = apiList
        self.warning = apiList != {} and warning
        self.path = path
    def __getattr__(self, s):
        try:
            tmpApi = self.apiList
            for name in self.path + [s]: tmpApi = tmpApi[name]
        except:
            if self.warning: raise ApiError(self.path + [s])
            api = ApiFramework(self.apiList, self.warning, self.path + [s])
        else:
            api = ApiFramework(self.apiList, self.warning, self.path + [s])
            api.__doc__ = tmpApi
        return api
    @at.api
    def __call__(self, *args, **kwargs):
        url = '%s/%s?access_token=%s'%(BASE_URL, '/'.join(self.path), kwargs.get('accessToken', ''))
        if kwargs.get('data') is None: return requests.get(url).json()
        del kwargs['accessToken']
        return requests.post(url, **kwargs)

api = ApiFramework()

__all__ = [api]
