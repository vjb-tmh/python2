'''
Client
'''
import socket, select, string, sys
import time

def prompt() :
    '''
    Print a prompt
    '''
    sys.stdout.write('>> ')
    sys.stdout.flush()

if __name__ == "__main__":

    # A sample HL7 ADT message
    # Note that all HL7 messages must be formatted with special beginning
    # and ending characters to be processed correctly by the integration engine.
    # Messages must start with a vertical tab: \v
    # Messages must end with a field seperator and a carriage return: \x1C\r
    msg = '''\vMSH|^~\&|FOOBAR LOGIC|FOOBAR^NFWC|BBRHIO Export|MRN^2.16.840.1.113883.3.7120.10.3|20180606070000||ADT^A08|1843887518113770|P|2.3.1|||NE|NE
EVN|A08|20180606070000
PID|1||161111||Parker^Peter^A||19880507|F||2106-3|7777 Easy Street^^Tallahassee^FL^32312||^^^kclark0507@yahoo.com~(860) 859-7234^^CP||English|M|||000-00-7058|||UPD1||||^Gamble^Terreze
NK1|1|Clark^Carol|M||8608597232
NK1|1||P|1202 N MAGNOLIA DR^^TALLAHASSEE^FL^323084634|8508773075||||||||Walgreens #TLH \F\ * N Magnolia @ Miccosukee*
NK1|2|Rosenberg^Lori^W^M.D.|O|1401 Centerville Road Ste 202^^Tallahassee^FL^32308-4638|8508777241|8508771338|||||||N FL W C - L. Rosenberg, MD
NK1|3|Gamble^Terreze|O|1803 Miccosukee Commons Dr^Suite 803^Tallahassee^FL^32308|8504026210|8503256015|||||||TPCA
PV1|1|O|^^^NFWC||||lrosenberg|^Rosenberg^Lori^W|||||||||||_EXPORTVISITID_|||||||||||||||||||||||||||||||_EXPORTVISITID_
GT1|1||Sharp^Kelsea^A||9166 Stonehenge trail^^Tallahassee^FL^32312|8608597234^^^kclark0507@yahoo.com||19880507000000|F|P||000-00-7058
IN1|1||CIGNA|CIGNA|PO BOX 188061^^Chattanooga^TN^37422||8556069294|3341051||||20180101|||P||S|||||||||||||||||||U6641500701\x1C\r'''

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
    print 'Enter \'y\' at the prompt to send a message.'
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
                    sys.stdout.write('Received: ' + data + '\n')
                    prompt()
            # Otherwise, it's keyboard input from stdin
            # Send the message
            else:
                # Print a propmpt and wait for keyboard input before
                # sending another message.
                prompt()
                ans = sys.stdin.readline()
                s.send(msg.encode())
                time.sleep(2)
