import socket
import datetime

host = '127.0.0.1'
port = 1450
buffer_size = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))

j=0
while (j < 5):

    # receive request from client

    request_from_client = server.recvfrom(buffer_size)\

    # print time at which request is received

    now = datetime.datetime.now()
    print(now)

    # reply to the client
    address = request_from_client[1]
    server.sendto(str.encode("i received your request"),address)

    j+=1

# close the server socket
server.close()
