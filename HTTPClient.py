import socket
import sys
args = sys.argv

hostname = 'comp431afa19.cs.unc.edu'
port = int(args[1])

for line in sys.stdin:
    print(line, end='')
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket established
        s.connect((hostname,port)) #Socket connect
		
		#Creating stream
        s.sendall(line.encode('utf-8')) 
        msg = s.recv(1024)
		
		#Closing stream
        s.close()
		
        print (msg.decode('utf-8'), end='')
    except OSError as e:
        print('Connection error')
