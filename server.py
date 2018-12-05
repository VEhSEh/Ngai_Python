#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module
import psycopg2             # import python postgres module
import json

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
def returnDatabaseResults(sql, con):
	all_patients = []
	
	#Create the cursor handler in the reader function	    
	try:
		cursor = con.cursor()
		cursor.execute(sql)                    #executes the querry on the database
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
	
		      


#conncect to the database
con = connectdb()
#Check if the connection object is not None
if conn is not None:
	print ("database opened successfully")

	result = returnDatabaseResults('select * from patient_info', con)
	if result is not None:
		print(result, type(result))
	else:
		print('No data read')
else:
	print('Fail to establish connecton to database')

		      
		      
		      
		      
		      

def service_request(client):
	try:
		data = client.recv(1024)
		print(data)
	except Exception as e:
		print(e)




def receive_request():
	sock = socket.socket() # this simple syntax creates by default tcp IPv4 socket object
	sock.bind(('', 5555)) # The '' host makes it to listen on all posible addresses in the local machine
	sock.listen('5') # Listen to 5 concurrent request
	
	try:
		# We listen forever
		while True:
			#We accept a client that tries to connect
			client, address = sock.accept()
			
			#We send the client to another routine to service the request (They are commonly called request handlers)
			service_request(client)
			
	
	except Exception as e:
		print(e)
	
	sock.close()
