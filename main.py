from socket import *
import re



#server
#define server port
serverPort = 9966
#define TCP server
serverSocket = socket(AF_INET, SOCK_STREAM)
# make binding with any ip address by ''
serverSocket.bind(('', serverPort))
# listen for requests
serverSocket.listen(1)
# print for the server is ready
print('The server is ready receive')

# open index.html file
with open('index.html', 'r', encoding='utf-8') as file:
   hfile = file.read()

# open arabic index.html file
with open('indexar.html', 'r', encoding='utf-8') as file0:
   hfile0 = file0.read()

# open html file for display it
with open('any.html', 'r',  encoding='utf-8') as file1:
   hfile1 = file1.read()

# open css file for display it
with open('html_en.css', 'r', encoding='utf-8') as file2:
   hfile2 = file2.read()

# open image with png tybe
with open('b.png', 'rb') as file3:
   hfile3=file3.read()

# open image with jpg tybe
with open('bb.jpg', 'rb') as file4:
   hfile4 = file4.read()

# open html for error page
with open('error.html', 'r',   encoding='utf-8') as file5:
   hfile5 = file5.read()

while True:

    # accept all requests
    connectionSocket, addr = serverSocket.accept()

    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))

    # receve http reqeust and store it in sentence
    sentence = connectionSocket.recv(4096).decode()
    # we split the request to get the request line from user input
    match=re.split(pattern=" ",string=sentence)
    response=match[1]
    # print http request in termanel
    print(sentence)


    # for any of this we handle the request depinding on the url
    # for sending our html file
    if(response=="/" or response=="/index.html" or response=="/main_en.html" or response=="/en"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile.encode())

    # for sending arabic page
    elif(response=="/ar"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile0.encode())

    # for sending html file and display it as request
    elif(response=="/.html%20file"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile1.encode())

    # for sending css code
    elif(response=="/.css"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile2.encode())

    # for sending image with png type
    elif(response=="/.png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile3)

    # for sending image with jpg type
    elif (response == "/.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile4)


    check = ["/", "/index.html", "/main_en.html", "/en", "/ar", "/.html", "/.css", "/.png", "/.jpg"]
    for c in check:
        # opening cornell website
        if response == "/cr":
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
            connectionSocket.send("Location: https://www.cornell.edu\r\n".encode())
            connectionSocket.send('\r\n'.encode())
            print("cornell.edu website successfully connected\r\n")
            break

        # opening stackoverflow website
        elif response == "/so":
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
            connectionSocket.send("Location:http://www.stackoverflow.com\r\n".encode())
            connectionSocket.send('\r\n'.encode())
            print("stackoverflow.com website successfully connected\r\n")
            break

        # opening ritaj website
        elif response == "/rt":
            connectionSocket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())
            connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
            connectionSocket.send("Location:https://ritaj.birzeit.edu/register/\r\n".encode())
            connectionSocket.send('\r\n'.encode())
            print("ritaj.com website successfully connected\r\n")
            break

        # for sending error page
    else:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(hfile5.encode())



