import requests

url = 'http://geoffcmdwechat.applinzi.com/?signature=3dd211ac4759a4765558e89acd5ea82dcb693e82&timestamp=1459853751&nonce=1886306063'
data = '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[this is a test]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>
'''
r = requests.post(url, data)
with open('reply', 'w') as f: f.write(r.content)
