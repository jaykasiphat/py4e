import socket

'''
    Change the socket program socket1.py to prompt the user for
    the URL so it can read any web page. You can use split('/') to
    break the URL into its component parts so you can extract the
    host name for the socket connect call.
'''

web = input("Enter a website: ")
host = web.split('/')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host[2], 80))
request = 'GET ' + web + ' HTTP/1.0\r\n\r\n'
request = request.encode()
sock.send(request)

while True:
    data = sock.recv(500)
    if len(data) < 1:
        break
    print(data.decode(), end='')
sock.close()
