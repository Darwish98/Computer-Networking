#-----------------------------------------------------------
#-----------------------------------------------------------
# Lab 5: DNS client
# General structure
#------------------------------------------------------------
#-----------------------------------------------------------
import sys, time
import re
from socket import *

#DNS_server='10.1.112.11'
DNS_server='130.243.97.77'
#DNS_server='8.8.4.4'
DNS_port=53
timeout=5

clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.settimeout(timeout)
DNS_port = int(DNS_port) 

def FormatNameField(query_url):
    url_input= query_url.split(".")
    out_url=""
    for line in url_input:
        out_url+=chr(len(line))+line
    out_url+='\x00'
    out_url=out_url.encode()
    #print(type(out_url))
    return out_url

url_to_query='www.oru.se'
#url_to_query='www.google.se'
formatted_url=FormatNameField(url_to_query);
additional_info=b'\x00\x01\x00\x01'
FormatedURL_plus_additional=formatted_url+additional_info


def messageassembly(queryDNS):
    AtypeHeader=b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
    queryDNS=AtypeHeader+queryDNS
    return queryDNS

query_to_DNS= messageassembly(FormatedURL_plus_additional)
print('query_to_DNS', query_to_DNS)



try:
    
    clientsocket.sendto(query_to_DNS,(DNS_server, DNS_port))
    message, address = clientsocket.recvfrom(1024)
    print ('message',message)
    
    #-----------------------------------------
    # Response parsing (YOUR CODE)
    #----------------------------------------
    messageStartwithanswer=message[len(query_to_DNS):]  #Here i inserted the message - question or in other words [len(query_to_DNS):]
    empque=[]
    for x in messageStartwithanswer: #Herse i inserted into a list
        empque.append(x)
            
            
    QueList=''.join(str(empque))  #Convert list to str and  join the elements
    QueList= QueList.replace(" ", "") #Remove spaces
    QueList= QueList.replace(",", ".") #replace , with .
    QueList= QueList.replace("192", " 192") #Becuse every new querie starts with b'\xc0' = 192 therfore i replaced "192" with " 192" now there is space between every querie   
    QueList= QueList.split(" ") #Convert back to list but now list of queries instead 
    print(QueList) 
    Iplist=[]
    for x in QueList:
        if x[6:14] == ".0.1.0.1": #Check if type A 
            if x[28]=='.':
                Iplist.append(x[29: -1])
            elif x[27]=='.':
                Iplist.append(x[28: -1])
            else:
                Iplist.append(x[27: -1])
    print("\nIP addresses from a type-A DNS query\n",Iplist ) #print the Ip adresses 

    


##My older code that don't check additional records 
    
##    if messageStartwithanswer[2:4]==b'\x00\x01':
##            print("its type A")
##            IPToConvert=messageStartwithanswer[12:16]
##            IPAddress=''
##            for x in IPToConvert:
##                if x == IPToConvert[-1]:
##                    IPAddress+=str(int.from_bytes([x],byteorder='big'))
##
##                else:
##                    IPAddress+=str(int.from_bytes([x],byteorder='big'))+'.'
##            
##            print(IPAddress)
           
##
##
##            
##    else:
##            print("its not A type")
        
    
    
    


except:
#-----------------------------------------
# Exception handling
#-----------------------------------------
    print('A timeout has occured, no reply from the DNS server');

  
     
 
