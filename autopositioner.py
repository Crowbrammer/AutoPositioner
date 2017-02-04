import libs.apa_database
import inspect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, Property
from kivy.uix.screenmanager import ScreenManager, Screen#, FadeTransition

class ScreenManagement(ScreenManager):
	pass

class PositionerScreen(Screen):

	pass
	
class PositionerLayout(BoxLayout):
	def __init__(self, **kwargs):
		super(PositionerLayout, self).__init__(**kwargs)
		# for i in all_active_machines:
			# check if the machine's up 
			# check the model_in_the_machine
			# check the positions required for the model_in_the_machine
			# generate a tuple of positions ID's mach_model_pos
		# for num_machines in machine_list:
			# self.add_widget(MmpModule())
			# current_module_machine_name = machine_list[num_machine]
			# current_module_model_name = dropdown_list_of_models
			# list_view_thing = ready_to_be_updated
					
		machine_list = libs.apa_database.get_data('machineID_modelID_status', order_by_column='machineID')
		global position_chart
		position_chart = libs.apa_database.assign_people_to_positions()
		
		mmpm = []
		
		for i in range(0, len(machine_list)):
		
			mmpm.append(MmpModule())
			mmpm[i].ids.machine_button.text = 'Wow: {}'.format(machine_list[i][0])
			mmpm[i].ids.model_button.text = 'Wow: {}'.format(machine_list[i][1])
			
			# Needs to pick each item apart and analyze it for its model name. 
			# Should move onto the item immediately if the item doesn't have the model
			
			for each in position_chart:
				
				if each[0][0] == machine_list[i][1]:
					if each[0][1] == 3:
						mmpm[i].ids.position3.text = 'Wow: {}'.format(each[1])
					elif each[0][1] == 2:
						mmpm[i].ids.position2.text = 'Wow: {}'.format(each[1])
					else:
						mmpm[i].ids.position1.text = 'Wow: {}'.format(each[1])
			
			#print('\n\nThe LC result: ' + str([x for x in position_chart if (machine_list[i][1]	 in position_chart]) + '\n\n^ ^ : Trying to get the values with only the current model.\n\n')
			#print()
			
			
			
			
			mymodel = mmpm[i].ids.machine_button.text
			self.add_widget(mmpm[i])
		
		# need to get a person in each position
		
		print(machine_list)
		
			
				
			

	def position_people(self):
		
		# Get a list of all the available people
		
		# c.execute('SELECT teammate FROM teammate_modelID_positionnum WHERE modelID=current_model AND positionNum=current_position')
			
		# available_people = c.fetchall
		
		# print(available_people)
		
		# # Compare the training of each person with the list 
		# c.execute('SELECT * FROM teammate_modelID_positionnum WHERE modelID=current_position)
		# if current_person in c.fetchall:
			# current_position_list += current_person
			
		pass
	
	def prioritize_position_by_training(self):
		
		pass
		# For each position, get the # of rows where people are trained in this position
		
class MmpModule(BoxLayout):

	machine_name = StringProperty()
	
	def __init__(self, **kwargs):
	
		super(MmpModule, self).__init__(**kwargs)
		self.machine_name = 'I-34'
		self.model_name = 'CSEG'

class IsSheTrained(BoxLayout):

	pass
	
class AddTeammatesLayout(BoxLayout):
	
	def __init__(self, **kwargs):

		super(AddTeammatesLayout, self).__init__(**kwargs)
		
		global lsm		
		lsm = [] # Label-Switch Module
		print(str(position_chart))
		for i in range(0, len(position_chart)):
			
			lsm.append(IsSheTrained())
			lsm[i].ids.position_label.text = 'Wow: {}'.format(position_chart[i][0][0])
			self.add_widget(lsm[i])
			
			
			# Needs to pick each item apart and analyze it for its model name. 
			# Should move onto the item immediately if the item doesn't have the model
			
	def record_that_shit(self):
	
		teammate_name = self.ids.teammate_name.text
		print('\n\nThe TextInput result: ' + teammate_name + '\n\n^ ^ : Trying to get the result of whether the TI*s text is registering\n\n')
		
		for each in range(0, len(lsm)):

			if lsm[each].ids.position_training_switch.active:
				
				#print('\n\nfor each positionNum: ' + str(position_chart[each][0][1]) + '\n\n^ ^ : Trying to see what position_chart[each][1][0] is bringing me.\n\n')
				
				#Add an entry to teammate_modelID_positionnum
				
				libs.apa_database.insert_data(tb='teammate_modelID_positionnum', col1='teammate', data1=teammate_name, col2='modelID', data2=position_chart[each][0][0], col3='positionNum', data3=position_chart[each][0][1], col4='available', 	data4='Yes', col5='restricted', data5='No')
				
				# Do db shit
		
		#for i in range(0, len(position_chart)):
		
class AddTeammatesScreen(Screen):

	pass

		
class AutopositionerApp(App):
	def build(self):
		ScreenManagement()
		
		
if __name__ == '__main__':
	AutopositionerApp().run()
