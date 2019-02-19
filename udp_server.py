from socket import *
import sys
import json
import unicodedata
s = socket(AF_INET, SOCK_DGRAM)
host = "192.168.100.113"

port = 55555
buf = 1024
data= b"Hello"
addr = (host, port)
num =1
arr1 = [1, 2, 3]
ip = gethostbyname("192.168.100.181")
while True:
    try:
        #s.sendto(num, addr)
        #s.sendto(data, addr)
        data = json.dumps({"Message": arr1})
        s.sendto(data.encode(),addr)
        print ("sending ...", data.encode())
        print(ip)
    except:
        print("Data has not been sent ... ")
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        someVar = 7
        data = json.dumps({"a": arr1, "b": arr2, "c": someVar})
        s.send(str(data))
        print("sending ...")