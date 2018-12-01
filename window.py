from tkinter import *
from chat_app.chat import server, client

window = Tk()

messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)
send_button = Button(window, text="Send") #command=self.send)
send_button.pack()

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', 13000))
serverSocket.listen(5)
serverO = server(serverSocket)
server_thread = Thread(target=server.connections)
server_thread.start()

client = client('localhost', 12000)
client.start()
recieve = Thread(target=client.receive)
recieve.start()



def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    messages.insert(INSERT, '%s\n' % input_get)
    # label = Label(window, text=input_get)
    input_user.set('')
    # label.pack()
    return "break"

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()
