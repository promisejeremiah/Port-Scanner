import socket
from datetime import datetime


ip = input('Enter target IP address... ') #request target ip from user
target = socket.gethostbyname(ip) #gets target ip
print(f'Scanning: {ip} for open ports.')
print(f'Time Started: {str(datetime.now())}')
#scans for open port ranging from port 50 - 58 in the target ip and prints it out
for ports in range(50,85):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, ports))
    if result == 0:
        print(f'Port: {ports} is open')
    else:
        print(f'Port: {ports}')
    s.close()
