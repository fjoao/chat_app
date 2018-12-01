from threading import Thread
import sys
from socket import *



class server:
    def __init__(self, serverport):
        self.serverport = serverport

    def connections(self, mess):
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind(('', self.serverport))
        print(self.serverport)
        serverSocket.listen(1)
        print('here')
        client, client_address = serverSocket.accept()
        # client.send(bytes('Enter your name', 'utf8'))
        # name = client.recv(1024).decode("utf8")
        # client.send(bytes(welcome, "utf8"))

        while True:
            msg = client.recv(1024)
            mess.insert(INSERT, '%s\n' % msg)
            if msg != bytes("quit", "utf8"):
                client.send(bytes(name+': '+msg))
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
