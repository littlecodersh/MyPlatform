#coding=utf8
import os, json
from config import ARTICLES_DIR, ARTICLES_NAME
from app.models.articles import output_articles_json
import app.plugins.tuling as tuling

def update_articles():
    try:
        with open(os.path.join('app', 'models', ARTICLES_NAME)) as f:
            lastUpdateTime = json.loads(f.read()).get('time')
        if raw_input('Last record: %s\nDo you want to update?[y] '%lastUpdateTime) == 'y':
            raise Exception
    except:
        r = output_articles_json(ARTICLES_DIR, ARTICLES_NAME)
        print('Articles update %sed'%('succeed' if r else 'CANCEL'))

def check_for_upload():
    print('*** Running upload check ***')
    # articles json
    try:
        with open(os.path.join('app', 'models', ARTICLES_NAME)) as f:
            print('Articles clear, recorded time: ' + json.loads(f.read())['time'])
    except:
        print('Please run %s successfully'%update_articles.__name__.replace('_', ' '))
    #tuling key
    print('Tuling plugin is %sopen'%'not ' if tuling.get_reply(u'Hello') is None else '')
    print('*** Upload check finished ***')

if __name__ == '__main__':
    fnList = [check_for_upload, update_articles, ]
    while 1:
        print('*** Command List ***\n0: Quit')
        for i, fn in enumerate(fnList): print('%s: %s'%(i + 1, fn.__name__.replace('_', ' '))) 
        choice = raw_input('Your command: ')
        if not choice.isdigit: print('Please enter a number'); continue
        choice = int(choice)
        if choice == 0: print('Bye~'); break
        if 0 < choice <= len(fnList): fnList[choice - 1]()
