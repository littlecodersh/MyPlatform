from client.webApp import app
from client import robot
from config import TOKEN
from flask import render_template, request, jsonify, make_response

import hashlib

def auth(request):
    s = [request.args.get(paramsName, '') for paramsName in ['timestamp', 'nonce']] + [TOKEN]
    s.sort()
    s = ''.join(s)
    return hashlib.sha1(s).hexdigest() == request.args.get('signature')

@app.route('/', methods=['GET', 'POST'])
def receive_msg():
    if not auth(request): return 'Hello world!'
    if request.method == 'GET': return request.args.get('echostr', 'Please use post to send msg!')
    response = make_response(robot.deal_with_msg(request.data))
    response.content_type = 'application/xml'
    return response
