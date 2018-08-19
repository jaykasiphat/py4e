import socket

'''
    You are to retrieve the following document using the HTTP protocol in a
    way that you can examine the HTTP Response headers.
    http://data.pr4e.org/intro-short.txt
'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(request)

while True:
    data = sock.recv(500)
    if len(data) < 1:
        break
    print(data.decode(), end='')
sock.close()
