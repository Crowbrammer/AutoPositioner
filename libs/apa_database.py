print("Hi, I'm apa_database.py!!")

import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

def create_table(table1, table2=None, table3=None):

	print('create_table() was called')

	c.execute('CREATE TABLE IF NOT EXISTS ' + table1 + '(machineID TEXT, modelID TEXT, machine_status INTEGER)')
	
	if table2 is not None:
		
		c.execute('CREATE TABLE IF NOT EXISTS ' + table2 + '(modelID TEXT, position_num INTEGER)')
		
		if table3 is not None:
		
			c.execute('CREATE TABLE IF NOT EXISTS ' + table3 + '(teammate TEXT, modelID	TEXT, position_num INTEGER)')
		
	print('create_table() finished')	

def insert_data(tb=None, col1=None, data1=None, col2=None, data2=None, col3=None, 	data3=None):
	
	print('insert_data() was called')
	
	if tb == None: pass
	
	elif col1 is None: pass
	
	elif col1 is not None or data1 is not None:
	
		if col2 is not None or data2 is not None:
		
			if col3 is not None or data3 is not None:
			
				c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ', ' + col3 + ') VALUES(?, ?, ?)', (data1, data2, data3))
				
			else: 
			
				c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ') VALUES(?, ?)', (data1, data2))
				
		else:
		
			c.execute('INSERT INTO ' + tb + '(' + col1 + ') VALUES(?)', (data1,))
	
	conn.commit()
	
	print('insert_data() finished')
	
create_table('machineID_modelID_status', 'modelID_position', 'teammate_modelID_position')

insert_data('machineID_modelID_status', 'machineID', 'I-41', 'modelID', 'CSEG')

# On listing tables: http://bit.ly/2k50OVC
