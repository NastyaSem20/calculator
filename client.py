import socket

def user_send(sock, data):
    sock.send(data.encode('ascii'))
    ans = sock.recv(1024)
    return ans
