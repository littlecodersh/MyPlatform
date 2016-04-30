#coding=utf8
from config import REPLY_DICT

def get_reply(content):
    return REPLY_DICT.get(content)
