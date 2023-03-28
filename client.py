# client
import socket
import threading
import os
import signal
from tkinter import *
from mttkinter import mtTkinter


def kill_signal():
    sock.close()
    pid = os.getpid()
    os.kill(pid, signal.SIGKILL)


def receive(socket):
    while True:
        name = socket.recv(32)
        data = socket.recv(32)
        text = str(name.decode("utf-8")).replace('0', '') + ": " + str(data.decode("utf-8"))
        print(text)
        label = Label(window, text=text)
        label.pack(pady=10)


host, port = "localhost", 12366

window = mtTkinter.Tk()
window.geometry("400x400")
canvas1 = Canvas(window, width=400, height=300)
canvas1.pack()

nameEntry = Entry(window)
canvas1.create_window(0, 0, window=nameEntry)
nameEntry.place(anchor=NW)

button_pressed = StringVar()
name_button = Button(text='Submit name', command=lambda: button_pressed.set("button_pressed"))
canvas1.create_window(320, 0, window=name_button, anchor=NE)
name_button.wait_variable(button_pressed)
name = nameEntry.get()
name.ljust(32, '0')
nameEntry.destroy()
name_button.destroy()

entry1 = Entry(window)
canvas1.create_window(200, 140, window=entry1)
entry1.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

sock.sendall(str.encode(name))
receiveThread = threading.Thread(target=receive, args=(sock,))
receiveThread.start()

while True:
    button_pressed2 = StringVar()
    button1 = Button(text='Send text', command=lambda: button_pressed2.set("button_pressed"))
    canvas1.create_window(80, 80, window=button1)

    button2 = Button(text='Quit', command=kill_signal)
    canvas1.create_window(20, 20, window=button2)

    button1.wait_variable(button_pressed2)
    message = entry1.get()
    label = Label(window, text=message)
    label.pack(pady=10)
    sock.sendall(str.encode(message))
