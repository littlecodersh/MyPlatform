import time
import xml.etree.ElementTree as ET

__all__ = ['get_dict_from_xml', 'get_xml']

TEMPLATE = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>'

def get_dict_from_xml(x):
    r = {}
    try:
        x = ET.fromstring(x)
        for i in x: r[i.tag] = i.text
    except:
        pass
    return r

def get_xml(msgType, toUserName, fromUserName, content):
    return TEMPLATE%(toUserName, fromUserName, int(time.time()), msgType, content)
