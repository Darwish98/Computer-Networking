import sys  
import re
from socket import* 



#Q1 code 
def int2bin(number):  #Using recursion 

    if (type(number)!=int):
        
        sys.exit('ERROR! You entered a non integer number')

    if number:
        print(number,'÷',2,'=',number//2," and res:", number%2)

    if number>1:
        int2bin(number//2)
    print(" --- ")
    print("|",number % 2,"|")

## exception handling not useful in this exercise because the program will not crash 
# try:
#     int2bin(1.5)
# except IOError:
#     print('Non integer number entered')
#     sys.exit(1)




#Q2 code 
def parseMessage(inputString):
    #input_list=inputString.split(" ")
    input_list= re.split(" |\r|\n",inputString)
    requested_resource= input_list[1]
    clients_browser= input_list[8]
    HTTPversion= input_list[2]
    language=input_list[14]
    #compare the string, if the string=useragent the do something ( search it up)
    return requested_resource, clients_browser, HTTPversion, language




#Q3
def changeChar(inputString, index, newChar):
    if(index>len(inputString)):
        sys.exit('Input index out of range')
    input_list= re.split("",inputString)
    input_list.pop(index+1)
    input_list.insert(index+1,newChar)
    sep=""
    output_string=sep.join(input_list)
    return output_string


#try:
#     changeChar("Test",8,"B")
# except IndexError:
#     print('The index is out of range')
#     sys.exit(1)




def main():
    #Q1 test 
    int2bin(10)


    print("\n\n")


    #Q2 test 
    string1='GET /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n'
    function_output=parseMessage(string1)
    print(function_output)


    print("\n\n")


    #Q3 test
    print(changeChar("This is a string",0,"X"))
    print(changeChar("This is a string",5,"X"))
    print(changeChar("This is a string",10,"X"))
    

main()







