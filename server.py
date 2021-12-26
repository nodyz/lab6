import socket
import sys
import time
import errno
from multiprocessing import Process

choice = '1', '2', '3'

def process_start(s_sock):

    s_sock.send(str.encode("Welcome To Online Calculator"))

    while True:

                  #check if choice in options

                   if choice in ('1', '2', '3'):

                      if choice == '1':

                           print ("Square root of", num,  "=",  math.sqrt(num))

                      elif choice == '2':

                           print ("Base 10 of", num, "=", math.log10(num))

                      elif choice == '3':

                           print ("Base 2 of", num, "=", math.log2(num))

                   #check if user want to calculate again

                      calcAgain = input("Wants to calculate again? (yes/no): ")
                      if calcAgain == "no" :
                         break

                   else:
                             print ("Invalid Input!")
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
                print ('an exception occurred!')
                print (e)
                sys.exit(1)

    finally:
                s.close ()
