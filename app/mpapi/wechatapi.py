import requests, json, os, time

from app.mpapi.rawapi import api

def get_ip_list():
    return api.getcallbackip().get('ip_list')

def send_text(msg, toUserName):
    data = {
        'touser': toUserName,
        'msgtype': 'text',
        'text': { 'content': msg }
    }
    headers = { 'ContentType': 'application/json' }
    return api.message.custom.send(data = data, headers = headers)

def get_menu():
    return api.menu.get()

def set_menu(menu):
    r = api.menu.create(data = json.dumps(menu))
    if r.get('errcode', -1) == 0:
        return True
    elif r.get('errcode', -1) == 48001:
        return False
