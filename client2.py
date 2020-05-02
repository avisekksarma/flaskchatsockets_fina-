import socket
import pickle
import time

from flask import Flask,render_template,request
c = socket.socket()
c.connect(('127.0.0.1',9999))
print("i m here")
app = Flask(__name__)

@app.route('/',methods = ["POST","GET"])
def index():

    if request.method == "POST":
        msg = request.form.get('msg')
        msg = "Shyam: " + msg
        c.send(pickle.dumps(msg))

    while True:
        c.send(pickle.dumps('qwert'))
        return render_template('chat.html')

msg_list = []
@app.route('/chat')
def livechatting():

    while True:
        print("1")
        try:
            msg = pickle.loads(c.recv(4096))
            msg_list.append(msg)

        except:
            print("2")
            msg = ""

        return render_template('livechatting.html',msg_list=msg_list)


if __name__ == "__main__":
    app.run(debug = False,port = 8000)
