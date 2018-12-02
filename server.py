from threading import Thread
import sys
from socket import *
from tkinter import *



def connections(mess, serverport):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverport))
    print(serverport)
    serverSocket.listen(1)
    print('here')

    # client.send(bytes('Enter your name', 'utf8'))
    # name = client.recv(1024).decode("utf8")
    # client.send(bytes(welcome, "utf8"))

    while True:
        print('check')
        client, client_address = serverSocket.accept()
        msg = client.recv(1024)
        print(msg)
        mess.insert(INSERT, '%s\n' % msg)
        if msg != bytes("quit", "utf8"):
            client.send(bytes(name+': '+msg))
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
