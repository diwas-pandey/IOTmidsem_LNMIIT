import socket
import threading

host = "127.0.0.1"
port = 5000

name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            msg = client.recv(1024).decode()

            if msg == "NAME":
                client.send(name.encode())
            else:
                print(msg)

        except:
            print("Connection closed")
            client.close()
            break


def send():
    while True:
        message = input()
        full_message = name + ": " + message
        client.send(full_message.encode())


t1 = threading.Thread(target=receive)
t1.start()

t2 = threading.Thread(target=send)
t2.start()