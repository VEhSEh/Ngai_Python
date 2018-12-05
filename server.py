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

# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# s.bind((host, port))        # Bind to the port

# s.listen(5)                 # Now wait for client connection.
# while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print ('Got connection from', addr)
#    sql = c.recv(1024)   #receive statement to execute from client
#    results = returnDatabaseResults(sql, cursor)    #execute querry and return the results
#    for result in results:
#    	c.send(result[0])
#    	c.send(result[1])
#    	c.send(result[2])
#    	c.send(result[3])
#    #c.send('Thank you for connecting')
#    c.close()                # Close the connection
