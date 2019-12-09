import socket
import sys
import os

req = ['','','']
reqErrors = [
    'ERROR -- Invalid Method token.\n',
    'ERROR -- Invalid Absolute-Path token.\n',
    'ERROR -- Invalid HTTP-Version token.\n',
    'ERROR -- Spurious token before CRLF.\n'
]

def main():

    args = sys.argv
    port = int(args[1])

    try:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Server Connection Established
        s_socket.bind(("", port))
        s_socket.listen(1)
    except OSError as e: # Errors
        print('Connection error')
        return

    while True:
        (client_socket, address) = s_socket.accept()

        input = client_socket.recv(1024)
        input = input.decode('utf-8')

        response = checkinput(input)

        client_socket.send(response.encode('utf-8'))

def checkinput(input):
    curr_token = 0
    response = ''

    if input[0] in ' \f\n\r\t\v':
        return reqErrors[0]

    arr = input.split(' ')

    for elt in arr:
        elt = elt.strip()
        if elt == '': continue
        rv = checkSubstring(curr_token, elt)
        curr_token += 1
        if rv < 0:
            break

    if rv != 0:
        return reqErrors[rv]

    if curr_token == 3:
        response += 'Method = ' + req[0] + '\n'
        response += 'Request-URL = ' + req[1] + '\n'
        response += 'HTTP-Version = ' + req[2] + '\n'

        if req[1].split('.')[-1].lower() not in ['txt', 'html', 'htm']:
            return response + '501 Not Implemented: ' + req[1] + '\n'

        file_name = req[1][1:]

        try:
            path = os.getcwd() + '/' + file_name
            file = open(file_name, 'r')
            for input in file:
                response += input
            return response
        except FileNotFoundError:
            return response + '404 Not Found: ' + req[1] + '\n'
        except IOError as e:
            return 'ERROR: ' + e + '\n'
    else: return reqErrors[curr_token-4]

def cleanFilePath(token):
    if token[0]=='/': token = token[1:]
    arr = token.split('.')
    arr[-1] = arr[-1].lower()
    response = arr[0]
    for elt in arr[1:]:
        response += '.' + elt
    return response

def validFilepath(token):
    if token[0] != '/':
        return -3
    token = token.lower()
    for char in token:
        if char not in 'qwertyuiopasdfghjklzxcvbnm1234567890._/': return -3
    return 0

def validHTTPVersion(token):
    arr = token.split('/')
    if len(arr) != 2 or arr[0] != 'HTTP': return -2
    arr = arr[1].split('.')
    if len(arr) != 2: return -2
    for elt in arr:
        for char in elt:
            if char not in '1234567890': return -2
    return 0

def checkSubstring(token_index, token):
    global req
    rv = 0
    if token_index == 0 and token != 'GET': rv = -4
    elif token_index == 1: rv = validFilepath(token)
    elif token_index == 2: rv = validHTTPVersion(token)
    elif token_index > 2: rv = -1

    if rv == 0: req[token_index] = token
    return rv

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        try: sys.exit(0)
        except SystemExit: os._exit(0)
