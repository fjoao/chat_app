from threading import Thread
import sys
from socket import *
from tkinter import *
from server import *

class client:
    def __init__(self, servername, clientport):
        self.servername = servername
        self.clientport = clientport

    def start(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        ADDR = (self.servername, self.clientport)
        print(ADDR)
        client_socket.connect(ADDR)
        recieve = Thread(target=client.receive)
        recieve.start()


    def recieve(self):
        while True:
            try:
                msg = client_socket.recv(1024).decode("utf8")
                messages.insert(INSERT, '%s\n' % msg)
                # msg_list.insert(tkinter.END, msg)
            except OSError:
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



if __name__ == "__main__":

    window = Tk()

    messages = Text(window)
    messages.pack()

    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    send_button = Button(window, text="Send") #command=self.send)
    send_button.pack()

    server = server(13000)
    server_thread = Thread(target=server.connections, args=((messages,)))
    server_thread.start()

    client = client('127.0.0.1', 12000)
    client.start()



    def Enter_pressed(event):
        input_get = input_field.get()
        print(input_get)

        # label = Label(window, text=input_get)
        input_user.set('')
        # label.pack()
        return "break"

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
