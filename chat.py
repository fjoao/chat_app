from threading import Thread
import sys
from socket import *
import tkinter

class server:
    def __init__(self, servername, serverport):
        self.servername = servername
        self.serverport = serverport

    def start(self):
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind(('', self.serverport))
        serverSocket.listen(1)

    def connections(self):
        while True:
            client, client_address = SERVER.accept()
            client.send(bytes('Enter your name', 'utf8'))
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

    def start(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        ADDR = (self.servername, self.clientport)
        client_socket.connect(ADDR)

    def recieve():
        while True:
            try:
                msg = client_socket.recv(BUFSIZ).decode("utf8")
                msg_list.insert(tkinter.END, msg)
            except:
                break

    def send(event=None):
        msg = my_msg.get()
        my_msg.set("")  # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()

    def on_closing(event=None):
        my_msg.set("{quit}")
        send()

    top = tkinter.Tk()
    top.title("Chatter")

    messages_frame = tkinter.Frame(top)
    my_msg = tkinter.StringVar()
    my_msg.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)
    msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    entry_field = tkinter.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send)
    send_button.pack()

    top.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    server = server('localhost', 1200)
    server.start()
    server_thread = Thread(target=server.connections)
    client = client('localhost', 1300)
    client.start()
    receive = Thread(target=receive)
    receive.start()
    tkinter.mainloop()
