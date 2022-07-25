import socket 

trg_hst = input("Enter The Host Name => ")
trg_prt = int(input("Enter The Port Name => "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((trg_hst,trg_prt))

client.send(b"GET / HTTP/1.1\r\nHost:"+trg_hst)

response = client.recv(4096)
client.close()