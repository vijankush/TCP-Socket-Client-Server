# TCP-Socket-Client-Server
Built a simple TCP Socket client/server programming implemented using Python that parses input, processes HTTP GET requests and handles errors accordingly.

How it works:
1. The client program reads a line of input from standard input
2. Sends the line to the server program over a socket connection
3. Receives a response line(s) from the server
4. Echoes all output from the server to standard output
5. Then get another line from standard input and repeat the process. 

*A separate new socket is created for each interaction (HTTP GET request/response) between the client and the server.*
