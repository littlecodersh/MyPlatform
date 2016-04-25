#coding=utf8
import time
import xml.etree.ElementTree as ET

from config import ADMIN_OAUTH

robotValue = {'adminUserName': None, }

def deal_with_msg(xmlMsg):
    xmlRecv = ET.fromstring(xmlMsg)  
    toUserName = xmlRecv.find("ToUserName").text  
    fromUserName = xmlRecv.find("FromUserName").text  
    content = xmlRecv.find("Content").text
    baseReply = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>'
    baseReply = baseReply%('%s', toUserName, str(int(time.time())), '%s')
    if authAdmin(fromUserName, content): return reply(fromUserName, baseReply, u'很高兴为你服务')
    content += fromUserName
    if fromUserName == robotValue['adminUserName']:
        return reply(fromUserName, baseReply, u'收到指令: %s'%content)
    else:
        return reply(fromUserName, baseReply, u'收到: %s'%content)
    
def authAdmin(userName, content):
    if content == ADMIN_OAUTH:
        robotValue['adminUserName'] = userName
        return True
    else:
        return False

def reply(toUserName, baseReply, content):
    return baseReply%(toUserName, content)

