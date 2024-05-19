import threading
import socket

host="127.0.0.1"
port=55555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

clients=[]
neck_names=[]

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:

            message=client.recv(1024)
            broadcast(message)
        except:
            index=client.index(client)
            client.remove(client)
            client.close()
            neck_name=neck_names[index]
            broadcast(f"{neck_name}left the chat".encode(ascii))
            neck_names.remove(neck_name)
            break


def receive_messages():
    while True:
        client,address=server_socket.accept()
        print(f"connected with{address}")
        client.send("neck".encode(ascii))
        neckname=client.recv(1024).decode(ascii)
        neck_names.append(neckname)
        clients.append(client)
        print(f"neckname of the client is{neckname}")
        broadcast(f"{neckname}joined the chat".encode(ascii))
        client.send("connected to the server".encode(ascii))


        thread=threading.Thread(target=handle ,args=(client,))
        thread.start()

print("server is listening....")
receive_messages()


