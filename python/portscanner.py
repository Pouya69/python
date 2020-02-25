import socket

ip=input("Please Enter Your Target's IP : ")

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portscan(port):
       try:
            con=s.connect((ip,port))
            return True
       except:
            return False


for x in range (10000):
    if portscan(x) :
        print("port open : "+ str(x))
    else :
        print("port closed : "+str(x))    
input("")
