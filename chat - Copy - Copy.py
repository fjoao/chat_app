from threading import Thread
import sys
from socket import *
import tkinter

class server:
    def __init__(self, S_socket):
        self.socket = S_socket

    def connections(self):
        while True:
            client, client_address = self.socket.accept()
            Thread(target=client, args=(client)).start()

    def client(self, client):
        name = client.recv(1024).decode("utf8")
        client.send(bytes(welcome, "utf8"))

        while True:
            msg = client.recv(1024)
            if msg != bytes("quit", "utf8"):
                client.send(bytes(name+': '+msg))
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
class client:

    

    
    def __init__(self, servername, clientport):
        self.servername = servername
        self.clientport = clientport
        self.client_socket = self.start()
        top = tkinter.Tk()
        top.title("Chatter")
        messages_frame = tkinter.Frame(top)
        self.my_msg = tkinter.StringVar()
        self.my_msg.set("Type your messages here.")
        scrollbar = tkinter.Scrollbar(messages_frame)
        self.msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(top, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.pack()
        send_button = tkinter.Button(top, text="Send", command=self.send)
        send_button.pack()
        top.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def start(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        ADDR = (self.servername, self.clientport)
        client_socket.connect(ADDR)

        return client_socket

    def recieve(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode("utf8")
                self.msg_list.insert(tkinter.END, msg)
            except OSError:
                break

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()

    def on_closing(self, event=None):
        self.my_msg.set("{quit}")
        send()

    
    

if __name__ == "__main__":

    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', 13000))
    serverSocket.listen(1)
    server = server(serverSocket)
    server_thread = Thread(target=server.connections)
    server_thread.start()
    
    print('SERVER READY')
    
    client = client('localhost', 12000)
    client.start()
    receive = Thread(target=client.recieve)
    receive.start()
    print('CLIENT READY')
    tkinter.mainloop()
    serverSocket.close()

