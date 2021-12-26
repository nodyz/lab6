import socket

ClientSocket = socket.socket()
host = '192.168.56.110'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))


Response = ClientSocket.recv(1024)
print(Response)

choice = '1','2','3'

while True:

    print ("\n\n Select operation would you like : \n")
    print ("1.Find square root \n ")
    print ("2.Find base 10 logarithm \n")
    print ("3.Find base 2 logarithm \n")


    choice = input("Enter your choice(1/2/3/4): \n")
    ClientSocket.send(str.encode(choice))
    num = float(input("Enter Your Number: \n"))
    ClientSocket.send(str.encode(num))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
