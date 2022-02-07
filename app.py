import json
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


def read_messages_from_file():
    """ Read all messages from a JSON file"""
    with open('messages.json') as messages_file:
        return json.load(messages_file)


def append_message_to_file(content):
    """ Read the contents of JSON file, add this message to it's contents, write it to disk. """
    messages = read_messages_from_file()
    new_message = {
        'content': content,
        'timestamp': datetime.now().isoformat(" ", "seconds")
    }
    messages['messages'].append(new_message)
    with open('messages.json', mode='w') as messages_file:
        json.dump(messages, messages_file)


# The Flask route, defining the main behaviour of the webserver:
@app.route("/")
def home():
    new_message = request.args.get('msg')
    if new_message:
        append_message_to_file(new_message)

    messages = read_messages_from_file()
    return render_template('home.html', messages=messages['messages'])
