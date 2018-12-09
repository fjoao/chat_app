from threading import Thread
from socket import *
from tkinter import *
import Encrypt

#pulls from the encrypt file to encrypt the message before it is sent
def encrypt(message):
    key = 'as'
    mappedKey = ""

    j = 0

    for i in message:
        if i == chr(32):
            mappedKey += chr(32)
        else:
            if j < len(key):
                mappedKey += key[j]
                j += 1
            else:
                j = 0
                mappedKey += key[j]
                j += 1

    message = message.upper()
    mappedKey = mappedKey.upper()

    return Encrypt.encryption(message, mappedKey)
#this decrypts the message using the decryption method in the encrypt file
def decrypt(message):
    key = 'as'
    mappedKey = ""

    j = 0

    for i in message:
        if i == chr(32):
            mappedKey += chr(32)
        else:
            if j < len(key):
                mappedKey += key[j]
                j += 1
            else:
                j = 0
                mappedKey += key[j]
                j += 1

    message = message.upper()
    mappedKey = mappedKey.upper()

    return Encrypt.decryption(message, mappedKey)
#sets up the server and accepts connections from clients
def connections(serverport):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverport))
    serverSocket.listen(1)

    while True:
        client, client_address = serverSocket.accept()
        msg = client.recv(1024).decode("utf8")
        print(msg)
        msg = decrypt(msg)
        msg = msg[0] + msg[1:].lower()
        messages.insert(INSERT,'%s\n' % msg)
        if msg == bytes("quit", "utf8"):
            client.send(bytes("{quit}", "utf8"))
        else:
            client.close()
#this sets ups the client and sends messages to the server
def send(name, event=None):
    client = ('127.0.0.1', 13000)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(client)
    msg = input_field.get()
    messages.insert(INSERT,name+': ' '%s\n' % msg)
    msg = encrypt(name+': '+msg)
    input_user.set('')
    client_socket.send(bytes(msg.encode()))
    if msg == "{quit}":
            client_socket.close()
            top.quit()

if __name__ == "__main__":
    #takes the users name
    name = input('Enter your name: ')
    #sets up the chat window
    window = Tk()
    window.title("Chatt App")
    messages = Text(window)
    messages.pack()
    #starts the server
    server_thread = Thread(target=connections, args=((12000,)))
    server_thread.start()
    #sets up user inout field and submit button
    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    send_button = Button(window, text="Send", command=send)
    send_button.pack()

    def Enter_pressed(event):

        sendmsg = Thread(target=send, args=((name,)))
        sendmsg.start()

        return "break"

    frame = Frame(window)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
