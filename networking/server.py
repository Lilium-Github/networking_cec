import socket

HOST = "10.17.68.56"  # Standard loopback interface address (localhost)
PORT = 33169  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # socket.socket creates a socket object. socket.AF_INET tells it to use IPv4, socket.SOCK_STREAM tells it to use the TCP.
    # using our socket in a with statement means you can use it without having to call s.close()

    s.bind((HOST, PORT)) #s.bind associates the socket s to the specific network interface (HOST) and port number (PORT)

    s.listen() # makes the server a "listening" socket

    conn, addr = s.accept() # waits for an incoming connection. when it gets one, it returns a new socket (conn) and a tuple with the client's address.

    with conn: # using the new socket we got from s.accept()

        print(f"Connected by {addr}") # confirmation message
        while True:
            data = conn.recv(1024)
            if not data:
                break

            if int(data) > 9:
                response = "That number is greater than 9."
            else:
                response = "That number is less than or equal to 9."

            conn.sendall(bytes(response, 'ascii'))