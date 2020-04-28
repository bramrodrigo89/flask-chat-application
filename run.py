import os
from flask import Flask, redirect

app = Flask(__name__)
messages=[]

def add_message(username, message):
    """Add messages to the messages' list"""
    messages.append("{}: {}".format(username,message))

def get_all_messages():
    """Gets all messages and separates them with a <br> tag"""
    return "<br>".join(messages)

@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message please use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    """Welcome user and display stored messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username,get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to main page"""
    add_message(username,message)
    return redirect("/" + username)

if __name__=="__main__":
    app.run(host=os.getenv("IP"),
        port=int(os.getenv("PORT")),
        debug=True)