#!/usr/bin/env python
from flask import Flask, request, make_response
from json import dumps
from requests import post

@app.route("/slack/<username>/<token>/<channel>", methods=['POST'])
def handle_slack(username, token, channel):
    #           'text': '```' + request.get_data() + '```',
    payload = {'token': token,
               'channel': channel,
               'text': request.get_data(),
               'username': username}
    r = post("https://slack.com/api/chat.postMessage", params=payload)
    return make_response(r.text, r.status_code)

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
