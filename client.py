import socket
import datetime
import time

host = '127.0.0.1'
port = 1450
buffer_size = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
total_time = 0

i = 0
while (i < 5):

    # Time now
    start = time.time()

    # send an echo request
    client.sendto(str.encode("hello echo server"),(host,port))

    # receive a reply
    message_from_server = client.recvfrom(buffer_size)

    # time now
    end = time.time()

    # print the reply received from the server
    message = "message from server {}".format(message_from_server[0])
    print(message)

    # print the elapsed time between request and reply
    elapsed = end - start

    # the sum of total elapsed time
    total_time = total_time + elapsed

    i+=i

# print the averag of the elapsed time
average = total_time/5
print("the average RTT: ", average)

#close the client socket
client.close()
