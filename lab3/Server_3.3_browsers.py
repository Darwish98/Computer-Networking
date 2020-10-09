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
                connectionSocket.send(outputdata)

               
                #Because internet explorer didnt show image i did it on firefox and chrome insted
                #And because the recived data from chrome have some extra lines more than firefox
                #I had to add this lines because User-agent on chrom have differet index than on firefox 
                
                if 'User' in data_received[2].split()[0].decode():
                        Browser=(data_received[2].split()[9]).decode().split("/")[0]


                if 'User' in data_received[5].split()[0].decode():
                        Browser=(data_received[5].split()[11]).decode().split("/")[0]

                

                
                # Because split requires a bytes-like object is and not 'str'
                #print('------------',Browser)


                if Browser=='Chrome':
                        Chrome_m=(b'/C:/Users/mohammed/Desktop/Data_kommunaktion/LabSession_material_2020/DT503G_20120/Lab_Session03/SupportMaterial/text_image.html')
                        
                        c = open(Chrome_m[1:],'rb')
                        Chrome_output= c.read()
                        connectionSocket.send(Chrome_output)
                        connectionSocket.close()
                        
                if Browser=='Firefox':
                        Firefox_m=(b'/C:/Users/mohammed/Desktop/Data_kommunaktion/LabSession_material_2020/DT503G_20120/Lab_Session03/SupportMaterial/text_only.html')
                        q = open(Firefox_m[1:],'rb')
                        Firefox_output= q.read()
                        connectionSocket.send(Firefox_output)
                        connectionSocket.close()

                                
                
               

               
        except IOError:
                # ----------------------------------
                #       I/O Error handling
                # ----------------------------------
                        Error_m=(b'/C:/Users/mohammed/Desktop/Data_kommunaktion/LabSession_material_2020/DT503G_20120/Lab_Session03/SupportMaterial/Error_window.html')
                        a = open(Error_m[1:],'rb')
                        output_= a.read()
                        connectionSocket.sendall(output_)

                        
                
                        connectionSocket.close()
        except IndexError:
                print('Index error exception')                          
serverSocket.close()                
                
                
        

