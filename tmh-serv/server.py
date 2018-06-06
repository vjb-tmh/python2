'''
Broadcast Server
'''
import socket, select

def broadcast_data (sock, message):
    '''
    Broadcast messages to connected clients.
    @param sock: the socket creating the message (we don't want to write to it)
    @param message: the message to send
    '''
    for socket in CONNECTION_LIST:
        # Do not send the message to server and
        # the client who has sent us the message
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                # Broken socket due to ctrl+c, etc.
                socket.close()
                CONNECTION_LIST.remove(socket)

# Send the data to the integration engine
# Send an ACK to the system that sent the original message
def tmh_send_data(sock, data):
    CP_TCPIP = '10.9.76.144'
    CP_PORT = 6666
    cpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cpsock.connect((CP_TCPIP,CP_PORT))
        sock.send('Simple ACK')
        cpsock.send(data)
        print('Message sent to {0} at {1}'.format(CP_TCPIP,CP_PORT))
        cpsock.close()
    except:
        sock.close()

if __name__ == "__main__":

    # List to keep track of socket descriptors
    CONNECTION_LIST = []

    # How much data to receive
    RECV_BUFFER = 4096

    # Note that localhost, '', and 0.0.0.0 all refer to localhost
    HOST = ''
    PORT = 5000

    # Build a socket and bind to address/port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Note that bind takes a tuple
    server_socket.bind((HOST, PORT))

    # Accept five connections
    server_socket.listen(5)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print "Server up on port " + str(PORT)

    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                # Periodically check for new connection on server socket
                # Add new client socket to connection list
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
            # Read client messages
            else:
                data = sock.recv(RECV_BUFFER)
                if(data):
                    if data:
                        # send the ack and the data to CP
                        tmh_send_data(sock, data)
                else:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()
