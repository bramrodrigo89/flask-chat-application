import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key="randomString123"
messages=[]


def add_message(username, message):
    """Add messages to the messages' list in dictionary form"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict={"timestamp":now, "from":username, "message":message}
    messages.append(messages_dict)

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
    return render_template("chat.html", username=username, chat_messages=messages)

@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to main page"""
    add_message(username,message)
    return redirect("/" + username)

if __name__=="__main__":
    app.run(host=os.getenv("IP"),
        port=int(os.getenv("PORT")),
        debug=True)