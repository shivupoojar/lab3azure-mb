from flask import Flask, render_template, request

app = Flask(__name__)


def read_messages_from_file():
    with open('messages.txt') as messages_file:
        return messages_file.readlines()


def append_message_to_file(content):
    with open('messages.txt', mode='a') as messages_file:
        messages_file.write(content + "\n")


@app.route("/")
def home():
    new_message = request.args.get('msg')
    if new_message:
        append_message_to_file(new_message)

    messages = read_messages_from_file()
    return render_template('home.html', messages=messages)
