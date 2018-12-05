#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module
import psycopg2             # import python postgres module

#function to connect database
def connectdb(database, user, password, host='127.0.0.1', port='5432'):
	con = psycopg2.connect(database=database, user=user, password=password,host=host, port=port)
	return con

#function to get results
def returnDatabaseResults(sql, cursor):
	cursor.execute(sql)                    #executes the querry on the database
	results = cursor.fetchall()            #fetch the results 
	return results                         #return the results


#conncect to the database
database = 'patientdb'
user = 'ngai'
password = 'ngai'
host = '127.0.0.1'
port = '5432'
con = connectdb(database,user,password, host,port)
print ("database opened successfully")

#create a cursor handler
cursor = con.cursor()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   sql = c.recv(1024)   #receive statement to execute from client
   results = returnDatabaseResults(sql, cursor)    #execute querry and return the results
   for result in results:
   	c.send(result[0])
   	c.send(result[1])
   	c.send(result[2])
   	c.send(result[3])
   #c.send('Thank you for connecting')
   c.close()                # Close the connection