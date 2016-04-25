from flask import render_template, request, jsonify, make_response

from app import app
from app.controls import robot, oauth

@app.route('/', methods=['GET', 'POST'])
def receive_msg():
    if not oauth.oauth(request): return 'Hello world!'
    if request.method == 'GET': return request.args.get('echostr', 'Please use post to send msg!')
    response = make_response(robot.deal_with_msg(request.data))
    response.content_type = 'application/xml'
    return response
