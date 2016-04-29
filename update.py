import os, json
from config import ARTICLES_DIR, ARTICLES_NAME
from app.models.articles import output_articles_json

def update_articles():
    try:
        with open(os.path.join('app', 'models', ARTICLES_NAME)) as f:
            lastUpdateTime = json.loads(f.read()).get('time')
        if raw_input('Last record: %s\nDo you want to update?[y] '%lastUpdateTime) == 'y':
            raise Exception
    except:
        r = output_articles_json(ARTICLES_DIR, ARTICLES_NAME)
        print('Articles update %sed'%('succeed' if r else 'CANCEL'))

if __name__ == '__main__':
    fnList = [update_articles, ]
    while 1:
        print('*** Command List ***\n0: Quit')
        for i, fn in enumerate(fnList): print('%s: %s'%(i + 1, fn.__name__.replace('_', ' '))) 
        choice = raw_input('Your command: ')
        if not choice.isdigit: print('Please enter a number'); continue
        choice = int(choice)
        if choice == 0: print('Bye~'); break
        if 0 < choice <= len(fnList): fnList[choice - 1]()
