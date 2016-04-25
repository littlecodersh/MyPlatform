import requests, json

import client.logging as logging

from config import APP_ID, SECRET_KEY

envValue = {
    'access_token': ''
    'ip_list': [], }

def set_ip_list():
    url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'%envValue['access_token']
    r = requests.get(url).json()
    ip_list = r.get('ip_list')
    if ip_list is None:
        logging.write(str(r), 'WARN')
        return False
    else:
        envValue['ip_list'] = ip_list
        return True

# auto set access_token
def api(fn, *args, **kwargs):
    def _api(*args, **kwargs):
        for i in range(10):
            if set_ip_list(): break
            set_access_token()
            if i == 9: return False
        result = fn(*args, **kwargs)
        return result
    return _api

def set_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
    url = url%(APP_ID, SECRET_KEY)
    r = requests.get(url).json()
    access_token = r.get('access_token')
    if access_token is None:
        logging.write(str(r), 'WARN')
        return False
    else:
        envValue['access_token'] = access_token
        return True

def send_text(msg, toUserName):
    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s'%envValue['access_token']
    data = {
        'touser': toUserName,
        'msgtype': 'text',
        'text': { 'content': msg }
    }
    headers = { 'ContentType': 'application/json' }
    r = requests.post(url, data = json.dumps(data), headers = headers)

set_access_token()
set_ip_list()
