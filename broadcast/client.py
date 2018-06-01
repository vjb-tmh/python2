'''
Client
'''
import socket, select, string, sys

def prompt() :
    '''
    Print a prompt
    '''
    sys.stdout.write('>> ')
    sys.stdout.flush()

if __name__ == "__main__":

    # check for the correct number of cmdline arguments
    if(len(sys.argv) < 3):
        print 'Invalid number of arguments.\n'
        print '\tUsage: python client.py hostname port'
        print '\tExample: python client.py localhost 5000'
        sys.exit()

    # Get address and port to connect to
    host = sys.argv[1]
    port = int(sys.argv[2])

    # Get a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # Connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect.'
        sys.exit()

    print 'Connected to remote host at %s on port %s' % (host, port)
    prompt()

    while True:
        # Read from stdin and from remote host
        # We need stdin to capture keyboard input
        socket_list = [sys.stdin, s]

        # Check for readable sockets
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            # If the socket is the one we used to connect to the broadcast server
            # It's an incoming message
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from remote host.'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    prompt()
            # Otherwise, it's keyboard input from stdin
            # Extract and send the message
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
