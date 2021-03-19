import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print(" Server akan dimulai pada host : ", host)
port = 8080
s.bind((host,port))
print("")
print("Hubungan antar host dan port telah sukses")
print("")
print("Server sedang menunggu koneksi yang akan masuk")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "Telah terkonek ke server dan sedang online...")
print("")
while 1:
            message = input(str(">> "))
            message = message.encode()
            conn.send(message)
            print("pesan telah terkirim...")
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print(" Client : ", incoming_message)
            print("")

