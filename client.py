#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import json


def connect():
  sock = socket.socket()
  host = 'localhost'
  port = 5555
  
  try:
    sock.connect((host, port))
    return sock
  
  except Exception as e:
    print(e)
 

def send_data(sock, data):
  #We always dump our data as json before sending it, whether string or list or dictionary, just dump to save lives
  data = json.dumps(data)
  if sock is not None:
    sock.sendall(data.encode())
  else:
    print("Null socket")

def receive_data(sock):
  if sock is non None:
    data = sock.recv(1024).decode()      #We decode the bytes to string Again 1024 is bad we are gonna fix this
    
    # Data might be dump as json, we try to load to normal form
    try:
      data = json.loads(data)
    
    except Exception as e:
      pass #Do nothing
    
    return data
  

def do_work():
  #Data we need to send to the server
  request_data = {'type':'GET', 'data':'lizzy'}
  
  #Connect to the server to establish a socket
  server_sock = connect()
  if server_sock is not None:
    #Send the request data
    send_data(server_sock, request_data)
    
    #Receive response from the server
    response = receive_data(server_sock)
    print(response)
    
  
if __name__ == '__main__':
    do_work()
