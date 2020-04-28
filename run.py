import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key="randomString123"
messages=[]

def add_message(username, message):
    """Add messages to the messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now,username,message))

def get_all_messages():
    """Gets all messages and separates them with a <br> tag"""
    return "<br>".join(messages)

@app.route("/", methods=["POST","GET"])
def index():
    """Main page with instructions"""
    if request.method=="POST":
        session["username"]=request.form["username"]
    if "username" in session:
        return redirect(session["username"])
        
    return render_template("index.html")

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