print("Hi, I'm apa_database.py!!")

import sqlite3

def open_connection():

	global conn 
	global c
	conn = sqlite3.connect('mydb.db')
	c= conn.cursor()

def close_connection():

	c.close()
	conn.close()
	
def create_table(table1, table2=None, table3=None):
	
	open_connection()
	
	print('create_table() was called')

	c.execute('CREATE TABLE IF NOT EXISTS ' + table1 + '(machineID TEXT, modelID TEXT, machine_status INTEGER)')
	
	if table2 is not None:
		
		c.execute('CREATE TABLE IF NOT EXISTS ' + table2 + '(modelID TEXT, positionNum INTEGER)')
		
		if table3 is not None:
		
			c.execute('CREATE TABLE IF NOT EXISTS ' + table3 + '(teammate TEXT, modelID	TEXT, positionNum INTEGER)')
		
	print('create_table() finished')	

	close_connection()
	
def alter_table(table_name=None, column_name=None, column_type=None, default_value=None):

	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
				.format(tn=table_name, cn=column_name, ct=column_type, df=default_value))
	
	''' Example use: 
	
	alter_table('modelID_positionnum', 'teammates', 'TEXT', 'needs_positioning') '''	
	
def insert_data(tb=None, col1=None, data1=None, col2=None, data2=None, col3=None, 	data3=None, col4=None, 	data4=None, col5=None, 	data5=None):
	
	print('insert_data() was called')
	
	if tb == None: pass
	
	elif col1 is None: pass
	
	elif col1 is not None or data1 is not None:
	
		if col2 is not None or data2 is not None:
		
			if col3 is not None or data3 is not None:
			
				if col4 is not None or data4 is not None:
					
					if col5 is not None or data5 is not None:
					
						c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ', ' + col3 + ', ' + col4 + ', ' + col5 + ') VALUES(?, ?, ?, ?, ?)', (data1, data2, data3, data4, data5))
					
					else:
					
						c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ', ' + col3 + ', ' + col4 + ') VALUES(?, ?, ?, ?)', (data1, data2, data3, data4))
					
				else:
			
					c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ', ' + col3 + ') VALUES(?, ?, ?)', (data1, data2, data3))
				
			else: 
			
				c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ') VALUES(?, ?)', (data1, data2))
				
		else:
		
			c.execute('INSERT INTO ' + tb + '(' + col1 + ') VALUES(?)', (data1,))
	
	conn.commit()
	
	print('insert_data() finished')
	
	'''Example use:
	
	insert_data('machineID_modelID_status', 'machineID', 'test', 'modelID', 'test')'''

def get_data(table_name=None, specific_data=False, column_name=None, model=None,
				order_by_column=None):

	open_connection()
	
	if specific_data == 'column':
	
		c.execute('SELECT {cn} FROM {tn} ORDER BY {cn}'.\
			format(tn=table_name, cn=column_name))
			
	elif model is not None: 
		
		c.execute('SELECT * FROM {tn} WHERE {cn}="{mo}" ORDER BY {ob} '.\
			format(tn=table_name, cn=column_name, mo=model, ob=order_by_column))
	
	elif order_by_column is not None:
		
		c.execute('SELECT * FROM {tn} ORDER BY {ob} '.\
			format(tn=table_name, ob=order_by_column))
	
	else:
	
		c.execute('SELECT * FROM {tn}'.format(tn=table_name))
		
	return c.fetchall()

	close_connection()
	
def prepopulate_teammate_table():

	open_connection()
	
	c.execute('SELECT * FROM modelID_positionnum')
	current_positions = c.fetchall()
	
	tm_name = input("Please enter the teammates's full name: ")
	
	if tm_name:
	
		for row in current_positions:
		
			insert_data('teammate_modelID_positionnum', 'teammate', tm_name, 'modelID', row[0], 'positionNum', row[1], 'available', 'Yes', 'restricted', 'No')	
			print(row[0], row[1])
			
		if input("Would you like to add another person?"):
			
			prepopulate_teammate_table()
	
	close_connection()

def position_people():
		
	# Get a list of all the available people
	
	open_connection()
	
	current_model = "CSEG"
	current_position = 1
	
	c.execute('SELECT teammate FROM teammate_modelID_positionnum WHERE modelID=? AND positionNum=?', (current_model, str(current_position)))
		
	available_people = c.fetchall
	
	print(available_people)
	
	# # Compare the training of each person with the list 
	# c.execute('SELECT * FROM teammate_modelID_positionnum WHERE modelID=current_position)
	
	# if current_person in c.fetchall:
		# current_position_list += current_person
		
	close_connection()
	
def list_positions():

	open_connection()
	
	c.execute("SELECT * FROM machineID_modelID_status WHERE machine_status='Up'")
	
	# Finally getting comfortable
	
	# Generate a list based on models of machines that are up. 
	
	up_machines = c.fetchall()
	global positions
	positions = []
	
	for machine in up_machines:
		
		c.execute("SELECT * FROM modelID_positionnum WHERE modelID=?", (machine[1],))
		
		# Where I learned to use a '?..., (tuple,)' format instead of Python vars: http://bit.ly/2l6XCY0
		# Where I learned to make the last part a tuple, not just a single item: http://bit.ly/2l7KFwp
		
		positions.append(c.fetchall())
	
	close_connection()
	
	print("The positions are: " + str(positions))
	
	# Positions done!
	
def update_database():
	
	open_connection()
	
	c.execute('UPDATE teammate_modelID_positionnum SET available="No" WHERE teammate="Louis"')
	conn.commit()
	
	# Where I learned this command: http://bit.ly/2k6oqXw
	
	close_connection()
	
def get_number_of_people_trained_on_each_position():

	open_connection()
	
	c.execute('SELECT * FROM teammate_modelID_positionnum')
	
	available_people = list(set([x[0] for x in c.fetchall() if x[3] != 'No']))
	
	# Where I learned to use list comprehensions properly (i.e. list only things of a certain value, that the first part is what's usually below it.): http://bit.ly/2l368uq
	# Where I learned to create sets from list comprehensions: http://bit.ly/2l3cmdE
	
	print('The people currently available are: ' + str(available_people))
	
	for each in positions:
		
		print('The current positions handled are: ' + str(each))
		
		for each in each:
		
			print('The single current position handled is: ' + str(each))
			
			c.execute('SELECT * FROM teammate_modelID_positionnum WHERE modelID=? AND positionNum=?', (each[0], each[1]) )
			
			for each in c.fetchall():
			
				print(each)
			
			
			
	close_connection()
	
create_table('machineID_modelID_status', 'modelID_positionnum', 'teammate_modelID_positionnum')

list_positions()
get_number_of_people_trained_on_each_position()

# Python's guide that will probably help me learn fetchone and executemany: http://bit.ly/2kvtKXY
# Best SQLite3 guide to-date: http://bit.ly/2l2jsv4
# On listing tables: http://bit.ly/2k50OVC
