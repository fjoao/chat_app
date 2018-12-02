from threading import Thread
import sys
from socket import *
from tkinter import *



def connections(serverport):
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
        msg = client.recv(1024).decode("utf8")
        print(msg)
        messages.insert(INSERT,'other: '+'%s\n' % msg)
        if msg == bytes("quit", "utf8"):
            client.send(bytes("{quit}", "utf8"))
        else:
            client.close()




def recieve(ADDR):
    while True:
        try:
            client_socket = socket(AF_INET, SOCK_STREAM)
            client_socket.connect(ADDR)
            msg = client_socket.recv(1024).decode("utf8")
            messages.insert(INSERT, '%s\n' % msg)
        except OSError:
            break

def send(event=None):
    client = ('127.0.0.1', 12000)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(client)
    msg = input_field.get()
    messages.insert(INSERT,'me: ' '%s\n' % msg)
    input_user.set('')
    print('hi: '+msg)
    client_socket.send(bytes(msg.encode()))
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

    server_thread = Thread(target=connections, args=((13000,)))
    server_thread.start()

    client = ('127.0.0.1', 14000)
    recieve = Thread(target=recieve, args=((client,)))
    recieve.start()


    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    send_button = Button(window, text="Send", command=send)
    send_button.pack()





    def Enter_pressed(event):

        #input_get = input_field.get()
        #print(input_get)
        sendmsg = Thread(target=send)
        sendmsg.start()

        # label = Label(window, text=input_get)
        #messages.insert(INSERT,'me: ' '%s\n' % input_get)
        #
        # label.pack()
        return "break"

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
