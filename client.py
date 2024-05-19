import socket
import threading

neckname=input("Enter a nickname:")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode(ascii)
            if message=="neck":
                client.send(neckname.encode(ascii))
            else:
                print(message)

        except:
            print("an error accured")
            client.close()
            break


def write():
    while True:
        message=input()
        client.send(message.encode(ascii))


receive_thread=threading.Thread(target=receive_messages)
receive_thread.start()

right_thread=threading.Thread(target=write)
right_thread.start()