#coding=utf8
import os, json, re, platform
from config import ARTICLES_DIR, ARTICLES_NAME
from app.models.articles import output_articles_json
import app.plugins.tuling as tuling

def update_config():
    print('Updating config, if you know python, you may change `config.py` yourself')
    print('If you DO NOT want to change, input Enter to continue')
    c = ''
    keyList = ['TOKEN', 'APP_ID', 'SECRET_KEY', 'TULING_KEY', 'INDEX_URL']
    regex = "%s = '(.*?)'"
    with open('config.py') as f:
        for l in f:
            for key in keyList:
                r = re.compile(regex % key).findall(l)
                if 0 < len(r):
                    value = raw_input("%s:['%s'] "%(key, r[0]))
                    if value != '':
                        if key == 'INDEX_URL':
                            if value[-1] != '/': value += '/'
                            value += 'articles_list/'
                        c += "%s = '%s'\n"%(key, value.strip());break
            else:
                c += l
    with open('config.py', 'w') as f: f.write(c)
    print('Config updated!')

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

def upload_to_server():
    if not 'Windows' in platform.platform():
        print('''\
            You are not using windows, I believe you can control git yourself
            There's the command:
                git add --all .
                git commit -m "%date%%time%"
                git push origin master:1
            Have a try~''')
    if raw_input('You are uploading your program to SAE, continue?[y] ') != 'y': return
    os.startfile(os.path.join('app', 'plugins', 'upload.bat'))

if __name__ == '__main__':
    fnList = [update_config, update_articles, check_for_upload, upload_to_server]
    while 1:
        print('*** Command List ***\n0: Quit')
        for i, fn in enumerate(fnList): print('%s: %s'%(i + 1, fn.__name__.replace('_', ' '))) 
        choice = raw_input('Your command: ')
        if not choice.isdigit: print('Please enter a number'); continue
        choice = int(choice)
        if choice == 0: print('Bye~'); break
        if 0 < choice <= len(fnList): fnList[choice - 1]()
