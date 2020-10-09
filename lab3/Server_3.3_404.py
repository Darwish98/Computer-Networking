# Import socket module
from socket import *    
import sys
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
        print('Waiting for requests ...')
        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
                message =  connectionSocket.recv(1024)
                # -------------------------------------------
                #       Request handling Section
                # -------------------------------------------
                data_received=message.split(b'\r\n')
                for x in data_received:
                        if x==b'':
                                continue
                        print(x)

                requested_resource=data_received[0].split()[1]
                f = open(requested_resource[1:],'rb')
                outputdata = f.read()
                connectionSocket.sendall(outputdata)
                print(requested_resource)

               
        except IOError:
                # ----------------------------------
                #       I/O Error handling
                # ----------------------------------
                        Error_m=(b'/C:/Users/mohammed/Desktop/Error_window.html')
                        a = open(Error_m[1:],'rb')
                        output_= a.read()
                        connectionSocket.sendall(output_)

                        
                
                        connectionSocket.close()
        except IndexError:
                print('Index error exception')                          
serverSocket.close()                
                
                
        

