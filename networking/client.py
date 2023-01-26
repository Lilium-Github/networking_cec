import socket

HOST = "10.17.68.56"  # The server's hostname or IP address
PORT = 33169 # The port used by the server

num = bytes(input("Input number:"), 'ascii')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:# socket.socket creates a socket object. socket.AF_INET tells it to use IPv4, socket.SOCK_STREAM tells it to use the TCP.
    # using our socket in a with statement means you can use it without having to call s.close()
    s.connect((HOST, PORT)) # connects to the server using the hostname + the port

    s.sendall(num)   # sends its message

    data = s.recv(1024)   # reads server's reply, puts it in data

print(f"Received {data!r}")   # prints data