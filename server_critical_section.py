import socket
from _thread import *

server_socket = socket.socket()
host          = "127.0.0.1"
port          = 61000
thread_count  = 0

try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waiting for connections...")
server_socket.listen(5)

def threaded_client(connection):
    #connection.send(str.encode("Welcome to the Server"))
    while True:
        data = connection.recv(2048)
        reply = "Server Says: " + data.decode("utf-8")
        if not data:
            break
        print(data.decode("utf-8"))
        print()
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = server_socket.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    thread_count += 1
    print("Thread Number: " + str(thread_count))
server_socket.close()
