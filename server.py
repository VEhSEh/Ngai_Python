#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module
import psycopg2             # import python postgres module
import json
from threading import Thread

#function to connect database
def connectdb():
	database = 'patientdb'
	user = 'ngai'
	password = 'ngai'
	host = '127.0.0.1'
	port = '5432'
	
	con = None
	# Here it will try to connect to the DB
	try:
		con = psycopg2.connect(database=database, user=user, password=password,host=host, port=port)
	
	#if there's a connection problem, you handle it here
	except Exception as e:
		print(e)
		print('Doing nothing with the problem found)
		      
	return con

#function to get results
#NB: python returns None by default
#Modified to call the connection method by itself
def returnDatabaseResults(name):
	con = connectdb()
	if con is not None:
		all_patients = []

		#Create the cursor handler in the reader function
		try:
			cursor = con.cursor()
			cursor.execute('SELECT * FROM patien_if WHERE name=%s', (name,))                    #Querying from database using varibles
			results = cursor.fetchall()            #fetch the results 

			#I will iterate over each row to create a dictionary of each row (patient) here
			for each in results:
			      each_row = {}
			      each_row['name'] = each[0]
			      each_row['phone'] = each[1]
			      each_row['email'] = each[2]
			      each_row['address'] = each[3] 

			      #I now append this row of patient entry to the list of all patients
			      all_patients.append(each_row)
			      #And go back for the next row

			return json.dumps(all_patients)                         #return the results

		except Exception as e:
			print(e)

		      
		      
		     

def service_request(client):
	try:
		request_data = client.recv(1024)
		
	except Exception as e:
		print(e)
	#Here now we can do whatever we intend to do with the request data
	#Suppose the data received is something like this {'type':'GET', 'data':'lizzy'}
	if request_data['type'] == 'GET':
		# We get the search keyword in the request_data of the client
		name = request['name']
		
		# We can now call the reader function
		result = returnDatabaseResults(name)
		
		#We now send the results back to the server
		client.send(result.encode())



def receive_request():
	sock = socket.socket() # this simple syntax creates by default tcp IPv4 socket object
	sock.bind(('', 5555)) # The '' host makes it to listen on all posible addresses in the local machine
	sock.listen('5') # Listen to 5 concurrent request
	
	try:
		# We listen forever
		while True:
			#We accept a client that tries to connect
			client, address = sock.accept()
			
		      	req = Thread(target=service_request, args=(client,))
		        req.start()
		      
		      	print("Going back to start listening for other request)
			
	
	except Exception as e:
		print(e)
	
	sock.close()
