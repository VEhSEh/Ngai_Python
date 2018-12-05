
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





