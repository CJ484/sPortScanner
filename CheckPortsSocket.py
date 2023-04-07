
import socket
import sys
from datetime import datetime

# Input for Remote Scan
#R_Server = input("Enter a remote host to Scan: ")
#R_ServerIP = socket.gethostname(R_Server)

# Check's what time the scan starts
now = datetime.now()
print(now)


"""IP and port test configuration"""
host = '1.1.1.1'


#Defining socket.socket to "s' for better convenience
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def portScan(port):
        try:
            s.connect((host,port))
            return True
        except:
            return False
    for x in range(1,200):
        if portScan(x):
            print('Port',x, 'is open')
        else: print('Port',x,'is closed')    
    # s.bind((host, port))
    # s.listen()
    # conn, addr = s.accept()
    # with conn:
    #     print('Connected by', addr)
    #     while True:
    #         data = conn.recv(1024)
    #         if not data:
    #             break
    #         conn.sendall(data)


