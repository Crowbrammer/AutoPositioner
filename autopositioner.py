# AutoPositionerApp for Kyle Woodsworth
# Name: Aaron Bell
# Collaborators: None
# Time Spent: 35:00

import libs.apa_database
import inspect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, Property
from kivy.uix.screenmanager import ScreenManager, Screen#, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


# # # # # # # # # # # # # # # # # # # # 

# Screens

# # # # # # # # # # # # # # # # # # # # 

class ScreenManagement(ScreenManager):

	pass
	
	
# # # # # # # # # # # # # # # # # # # # 

# Positioner Screen

# # # # # # # # # # # # # # # # # # # # 

class PositionerScreen(Screen):

	pass
	
class PositionerLayout(BoxLayout):

	def __init__(self, **kwargs): # Don't know **kwargs
	
		super(PositionerLayout, self).__init__(**kwargs)
		
		# What I WANT
		# for active_machine in all_active_machines:
			# check if the machine's up 
			# give the user the option to disable it or activate it, which will affect how the program positions people--or whether they position people at that machine
			# check the model_in_the_machine
			# give the user the option to change which model is used in the machine, which will affect how the program positions people--or whether they position people at that machine--because it changes the training and restriction requirements for that machine
			# check the positions required for the model_in_the_machine, for proper display of buttons--and accurate positioning.
			# people correctly positioned--according to their training and restrictions and availability--at each machine, in a randomized way.
		# for each_machines in machine_list:
			# # separated, is because deactivated machines still need to be displayed
			# self.add_widget(MmpModule())
			# current_module_machine_name = machine_list[num_machine]
			# current_module_model_name = current model, with a dropdown_list_of_models bound to it
			# a of positions to its left-- updated with people to fill the position (list_view_thing = ready_to_be_updated)
					
		machine_list = libs.apa_database.get_data('machineID_modelID_status', order_by_column='machineID') 
		model_list = set([x[0] for x in libs.apa_database.get_data('modelID_positionnum', order_by_column='modelID')]) # set does not contain duplicate values, and I don't think it orders it... don't know how to test that, yet... 
		#print('model_list is: ' + str(model_list))
		
		global position_chart # so that this variable is available for other functions (Because I don't know how to return data from this and give it to other classes, methods in other classes, because I don't know where Kivy stores implicit instances of these classes.)
		
		position_chart = libs.apa_database.assign_people_to_positions()
		
		# Not sure if it generates based on the machine list, or models currently used (i.e. not sure if it'll handle duplicates.)
		
		dropdown = []
		mmpm = []
		
		for each_machine in range(0, len(machine_list)):
			
			dropdown.append(DropDown()) # Because if I use a single DropDown instance, it'll either change every model_button, or only change one. 
			
			print('Dropdown ID: ' + str(id(dropdown[each_machine])))
			
			for model in model_list:

				btn = Button(text='{}'.format(model), size_hint_y=None, height=44)
				
				btn.bind(on_release=lambda btn: dropdown[each_machine].select(btn.text))

				dropdown[each_machine].add_widget(btn)
		
			mmpm.append(MmpModule())
			mmpm[each_machine].ids.machine_button.text = 'Wow: {}'.format(machine_list[each_machine][0])
			mmpm[each_machine].ids.model_button.text = 'Wow: {}'.format(machine_list[each_machine][1])
			mmpm[each_machine].ids.model_button.bind(on_release=dropdown[each_machine].open)	
			
			
			# # # # # # # # # # # # # # # # # # # # 

			# Add Teammates Screen

			# # # # # # # # # # # # # # # # # # # # 
			
			dropdown[each_machine].bind(on_select=lambda instance, x: setattr(mmpm[each_machine].ids.model_button, 'text', x)) # lambda - get through Unit 1
			
			# Needs to pick each item apart and analyze it for its model name. 
			# Should move onto the item immediately if the item doesn't have the model
			
			for each in position_chart:
				
				if each[0][0] == machine_list[each_machine][1]:
				
					if each[0][1] == 3:
					
						mmpm[each_machine].ids.position3.text = 'Wow: {}'.format(each[1])
						
					elif each[0][1] == 2:
					
						mmpm[each_machine].ids.position2.text = 'Wow: {}'.format(each[1])
						
					else:
					
						mmpm[each_machine].ids.position1.text = 'Wow: {}'.format(each[1])
			
			#print('\n\nThe LC result: ' + str([x for x in position_chart if (machine_list[i][1]	 in position_chart]) + '\n\n^ ^ : Trying to get the values with only the current model.\n\n')
			
			#print('\n\nID Keys: ' + str(self.ids.keys()) + '\n\n^ ^ : Trying to get the values of ids.\n\n')
			
			mymodel = mmpm[each_machine].ids.machine_button.text
			self.add_widget(mmpm[each_machine])
		
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

# # # # # # # # # # # # # # # # # # # # 

# Add Teammates Screen

# # # # # # # # # # # # # # # # # # # # 
		
class AddTeammatesScreen(Screen):

	pass

class IsSheTrained(BoxLayout):

	pass
	
class AddTeammatesLayout(BoxLayout):
	
	def __init__(self, **kwargs):

		global teammate_name
		teammate_name = ''
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
				
				libs.apa_database.insert_data(tb='teammate_modelID_positionnum', col1='teammate', \
				data1=teammate_name, col2='modelID', data2=position_chart[each][0][0], \
				col3='positionNum', data3=position_chart[each][0][1], col4='available', \
				data4='Yes', col5='restricted', data5='No')
				
				# Do db shit

		App.get_running_app().root.current = 'Victory'


# # # # # # # # # # # # # # # # # # # # 

# Added Teammates Successfully Screen

# # # # # # # # # # # # # # # # # # # # 

class AddedTeammatesSuccessfullyScreen(Screen):

	pass
	
class AddedTeammatesSuccessfullyLayout(BoxLayout):

	def __init__(self, **kwargs):
	
		print('Teammate text = ' + teammate_name)

		#print('\n\ntriggertool result: ' + triggertool + '\n\n^ ^ : Trying to get triggertool to go off\n\n')
		
		super(AddedTeammatesSuccessfullyLayout, self).__init__(**kwargs)
		
		self.victory_text = "You've added {} to your team!".format(teammate_name)
		
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####	
	
	# How do I get this to fire after AddTeammatesLayout().record_that_shit() runs?

	def trigger_text(self):
		self.victory_text = "You've added {} to your team!".format(teammate_name)
		
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
		
# # # # # # # # # # # # # # # # # # # # 

# Add Machine Screen

# # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # 

# Added Machine Successfully Screen

# # # # # # # # # # # # # # # # # # # # 
		


		
# # # # # # # # # # # # # # # # # # # # 

# Add Machine Screen

# # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # 

# Added Machine Successfully Screen

# # # # # # # # # # # # # # # # # # # # 
		
		
# # # # # # # # # # # # # # # # # # # # 

# "Boilerplate" (?)

# # # # # # # # # # # # # # # # # # # # 
	
class AutopositionerApp(App):
	def build(self):
		ScreenManagement()
		
if __name__ == '__main__':
	AutopositionerApp().run()
