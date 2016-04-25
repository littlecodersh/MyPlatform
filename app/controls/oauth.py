import hashlib

from config import TOKEN

def oauth(request):
    s = [request.args.get(paramsName, '') for paramsName in ['timestamp', 'nonce']] + [TOKEN]
    s.sort()
    s = ''.join(s)
    return hashlib.sha1(s).hexdigest() == request.args.get('signature')
