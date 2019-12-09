# TCP-Socket-Client-Server
Built a simple TCP Socket client/server programming implemented using Python that parses input, processes HTTP GET requests and handles errors accordingly.

- The client program reads a line of input from standard input, send the line to the server program over a socket connection, receive a response line(s) from the server, echo all output from the server to standard output, and then get another line from standard input. 
- A separate new socket is created for each interaction (HTTP GET request/response) between the client and the server.
