import socket

# create socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

# bind to socket
serversocket.bind((host, port))

# start tcp listener
serversocket.listen(3)

while True:
    # start connection
    clientsocket, address = serversocket.accept()
    print("recieved connection from " % str(address))

    message = 'Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message)

    clientsocket.close()



