from app.mpapi.wechatapi import get_menu, set_menu
from config import MENU

def init_menu():
    if MENU == {}: return
    if MENU == get_menu(): return True
    return set_menu(MENU)
