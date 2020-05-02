import socket
import  pickle
from _thread import *
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9999))
print("server started")
s.listen()
print('waiting for connections....')


def threaded_client(c,addr,my_position):
   while True:
        try:
            data = pickle.loads(c.recv(4096))
            if data != "qwert":
                for i in range(len(chatlist)):
                    # if i != my_position:
                        chatlist[i].send(pickle.dumps(data))
        except:
            break
   print("Lost connection to",addr)
   c.close()

chatlist = []

while True:
    c, addr = s.accept()
    print("connected to ",addr)
    chatlist.append(c)
    start_new_thread(threaded_client,(c,addr,len(chatlist)-1))

