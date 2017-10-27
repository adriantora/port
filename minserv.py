#alzar un mini servidor para recibir un socket con el mensaje exterior
import socket
from flask import Flask, request,redirect

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def hello_world():
    return '<form action="submit" id="textform" method="post"><textarea name="text" rows="4" cols="50" ></textarea></br><input type="submit" value="Submit"></form>  '


@app.route('/submit', methods=['POST'])
def submit_textarea():
    print request.form["text"]
    return redirect("/")


def minserver(ip,puerto):
    app.run(host=ip, port=puerto)
