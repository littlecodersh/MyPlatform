import re, requests, os, sys, json, time

regexDict = {
    'title': 'var msg_title = "(.*?)";',
    'summary': 'var msg_desc = "(.*?)";',
    'pic_url': 'var msg_cdn_url = "(.*?)";', }
for k, v in regexDict.items(): regexDict[k] = re.compile(v)

def get_detail_from_url(url):
    try:
        c = requests.get(url).content
    except:
        print('Check url: ' + url)
        return
    r = {'url': url}
    for k, v in regexDict.items():
        matches = v.findall(c)
        r[k] = matches[0].decode('utf8') if matches else None
    if any([v is None for v in r.values()]):
        print('Check url:')
        for k, v in r.items(): print('%s: %s'%(k,v))
        return
    return r

def output_articles_json(articlesDir, articlesName):
    aj = {'time': time.ctime()}
    for urlFile in os.walk(articlesDir).next()[2]:
        k = urlFile.decode(sys.stdin.encoding).split('.')[0]
        aj[k] = []
        with open(os.path.join(articlesDir, urlFile)) as f:
            for url in f:
                detail = get_detail_from_url(url.strip())
                if detail is None: return False
                aj[k].insert(0, detail)
    with open(os.path.join('app', 'models', articlesName), 'w') as f: f.write(json.dumps(aj))
    return True

def get_articles(articlesName):
    with open(os.path.join('app', 'models', articlesName)) as f:
        return json.loads(f.read())

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # url = 'https://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=2650968201&idx=1&sn=d3f7f393f5e9adf881357c58e75d9a26'
    for k, v in get_pic(url).items(): print('%s: %s'%(k,v))
