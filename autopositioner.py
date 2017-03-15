# AutoPositionerApp for Kyle Woodsworth
# Name: Aaron Bell
# Collaborators: None
# Time Spent: 35:00

import libs.apa_database
import inspect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen#, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock


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

		dropdown = [DropDown()]
		mmpm = []

		'''
		Get the list of machines into a SV:

		Put everything that would've gone into a BoxLayout into a GridLayout
		Set the size_hint_y to None, and make its minimum height into actual height(?)
		Put that GridLayout into a SV
		Set the height of SV (Optional)
		Put the SV into the current layout
		'''




		# Put everything that would've gone into a BoxLayout into a GridLayout (P1/2)
		# Set the size_hint_y to None, and make its minimum height into actual height(?)
		hold_mmpms = GridLayout(cols=1, size_hint_y=None, height=700)
		hold_mmpms.bind(minimum_height = hold_mmpms.setter('height'))

		for each_machine in range(len(machine_list)):

			dropdown.append(DropDown()) # Because if I use a single DropDown instance, it'll either change every model_button, or only change one.

			for model in model_list:

				btn = Button(text='{}'.format(model), size_hint_y=None, height=44)

				btn.bind(on_release=lambda btn, dropdown=dropdown[each_machine]: dropdown.select(btn.text))

				dropdown[each_machine].add_widget(btn)

			mmpm.append(MmpModule())
			mmpm[each_machine].ids.machine_button.text = 'Wow: {}'.format(machine_list[each_machine][0])
			mmpm[each_machine].ids.model_button.text = 'Wow: {}'.format(machine_list[each_machine][1])
			mmpm[each_machine].ids.model_button.bind(on_release=dropdown[each_machine].open)


			# # # # # # # # # # # # # # # # # # # #

			# WHY

			# # # # # # # # # # # # # # # # # # # #


			dropdown[each_machine].bind(on_select=lambda instance, x, mmpm=mmpm[each_machine]: setattr(mmpm.ids.model_button, 'text', x)) # lambda - get through Unit 1

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

			# Put everything that would've gone into a BoxLayout into a GridLayout (P1/2)
			hold_mmpms.add_widget(mmpm[each_machine])

		# Put that GridLayout into a SV
		scroll_mmpms = ScrollView(size_hint_y=10)
		scroll_mmpms.add_widget(hold_mmpms)

		# Put the SV into the current layout
		self.add_widget(scroll_mmpms)



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

	#def function_that_should_be_unnecessary(self):

		#self.text =

class MmpModule(BoxLayout):

	pass


# # # # # # # # # # # # # # # # # # # #

# Add Teammates Screen

# # # # # # # # # # # # # # # # # # # #

class AddTeammatesScreen(Screen):

	pass

class IsSheTrained(BoxLayout):

	pass

class AddTeammatesLayout(BoxLayout):

	def __init__(self, **kwargs):

		super(AddTeammatesLayout, self).__init__(**kwargs)

		global teammate_name
		teammate_name = ''

		positions = libs.apa_database.get_data(table_name='modelID_positionnum')

		global lsm
		lsm = [] # Label-Switch Module
		for i in range(0, len(positions)):

			lsm.append(IsSheTrained())
			lsm[i].ids.position_label.text = '{}-{}'.format(positions[i][0], positions[i][1])
			self.add_widget(lsm[i])
			# Needs to pick each item apart and analyze it for its model name.
			# Should move onto the item immediately if the item doesn't have the model

	def record_that_shit(self):

		teammate_name = self.ids.teammate_name.text
		libs.apa_database.insert_data(tb='teammate_modelID_positionnum', col1='teammate', \
		data1=teammate_name, col2='modelID', data2=None, \
		col3='positionNum', data3=None, col4='available', \
		data4=None, col5='restricted', data5=None)

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

# Model Add Screen

# # # # # # # # # # # # # # # # # # # #

class ModelAddScreen(Screen):
	pass

class ModelAddLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(ModelAddLayout, self).__init__(**kwargs)
		Clock.schedule_once(self.late_init, 0)

	def late_init(self, key, **largs):
		# print(dir(self.ids.num_positions))
		test = self.ids.model_add_name.text
		# print('test: ',str(test))
		# create a dropdown with 10 buttons
		dropdown = DropDown()
		for index in range(1,11):
			# When adding widgets, we need to specify the height manually
			# (disabling the size_hint_y) so the dropdown can calculate
			# the area it needs.

			btn = Button(text='%d' % index, size_hint_y=None, height=44)

			# for each button, attach a callback that will call the select() method
			# on the dropdown. We'll pass the text of the button as the data of the
			# selection.
			btn.bind(on_release=lambda btn: dropdown.select(btn.text))

			# then add the button inside the dropdown
			dropdown.add_widget(btn)

		self.ids.num_positions.bind(on_release=dropdown.open)
		dropdown.bind(on_select=lambda instance, x, e=self.ids.num_positions: setattr(e, 'text', x))



	def record_new_model(self):
		model_name = self.ids.model_add_name.text
		try:
			num_positions = int(self.ids.num_positions.text)
		except ValueError:
			self.ids.num_positions.text = 'Please select # of positions for model:'
			return

		for i in range(1, num_positions + 1):
			libs.apa_database.insert_data(tb='modelID_positionnum', col1='modelID', \
			 		data1=model_name, col2='positionNum', data2=i)

class PrimaryOverlay(ScrollView):
	pass

# # # # # # # # # # # # # # # # # # # #

# NavigationHUD

# # # # # # # # # # # # # # # # # # # #

class NavigationHUD(BoxLayout):
	pass

































# # # # # # # # # # # # # # # # # # # #

# Added Teammates Successfully Screen

# # # # # # # # # # # # # # # # # # # #


class AddedTeammatesSuccessfullyScreen(Screen):

	pass

class AddedTeammatesSuccessfullyLayout(BoxLayout):

	def __init__(self, **kwargs):

		#print('\n\ntriggertool result: ' + triggertool + '\n\n^ ^ : Trying to get triggertool to go off\n\n')

		super(AddedTeammatesSuccessfullyLayout, self).__init__(**kwargs)

		self.victory_text = "You've added {} to your team!".format(teammate_name)

	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

	# How do I get this to fire after AddTeammatesLayout().record_that_shit() runs?

	# Call an instance of a class, call the method or invoke the property, get
	# set a variable equal to it.

	def trigger_text(self):
		self.victory_text = "You've added {} to your team!".format(teammate_name)

	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
	#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####


# # # # # # # # # # # # # # # # # # # #

# Unused Machines Screen

# # # # # # # # # # # # # # # # # # # #

class UnusedMachineScreen(Screen):
	pass

class UnusedMachineLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(UnusedMachineLayout, self).__init__(**kwargs)
		dd_s = [DropDown(), DropDown()]
		easy_layouts = []
		# (C)
		machine_list = libs.apa_database.get_data('machineID_modelID_status', order_by_column='machineID')

		# (B)
		for each_machine in range(len(machine_list)):
			dd_s.append(DropDown())

			# D/2

			btn = Button(text='Up', size_hint_y=None, height=44)
			btn.bind(on_release=lambda btn, d=dd_s[each_machine]: d.select(btn.text))
			dd_s[each_machine].add_widget(btn)

			btn = Button(text='Down', size_hint_y=None, height=44)
			btn.bind(on_release=lambda btn, d=dd_s[each_machine]: d.select(btn.text))
			dd_s[each_machine].add_widget(btn)
			easy_layouts.append(ItemLayout())

			if machine_list[each_machine][2] == 'Down':

				easy_layouts[each_machine].ids.machine_id.text = machine_list[each_machine][0]
				# D
				easy_layouts[each_machine].ids.machine_id.bind(on_release=dd_s[each_machine].open)
				self.add_widget(easy_layouts[each_machine])

			# The issue is with this line, I think.
			# E
				dd_s[each_machine].bind(on_select=lambda instance, x, e=easy_layouts[each_machine]: (setattr(e.ids.machine_status, 'text', x), self.change_machine_status(x, e))) # lambda - get through Unit 1

	def change_machine_status(self, machine_status, machine_id):
		'''
		Change the machine list
		Change the database
		Remove 'changed-to-use' machines from screen
		Add unused machines to screen
		'''
		machineID = machine_id.ids.machine_id.text

		libs.apa_database.update_machine_status(machineID, machine_status)

class ItemLayout(BoxLayout):
	pass

# If a machine is tapped, have the option to select what model is there

# Have an entirely new screen for managing models

# # # # # # # # # # # # # # # # # # # #

# Added Machine Successfully Screen

# # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # #

# Add Machine Screen

# # # # # # # # # # # # # # # # # # # #

class MachineAddScreen(Screen):
	pass

class MachineAddLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(MachineAddLayout, self).__init__(**kwargs)
		Clock.schedule_once(self.late_init, 0)

	def late_init(self, key, **largs):
		# print(dir(self.ids.num_positions))
		test = self.ids.machine_add_name.text
		# print('test: ',str(test))
		# create a dropdown with 10 buttons
		dropdown = DropDown()
		btn = Button(text='Up', size_hint_y=None, height=44)
		btn.bind(on_release=lambda btn, d=dropdown: d.select(btn.text))
		dropdown.add_widget(btn)

		btn = Button(text='Down', size_hint_y=None, height=44)
		btn.bind(on_release=lambda btn, d=dropdown: d.select(btn.text))
		dropdown.add_widget(btn)
			# then add the button inside the dropdown

		self.ids.status.bind(on_release=dropdown.open)
		dropdown.bind(on_select=lambda instance, x, e=self.ids.status: setattr(e, 'text', x))



	def record_new_model(self):
		machine_name = self.ids.machine_add_name.text
		status = self.ids.status.text
		print(machine_name)

		libs.apa_database.insert_data(tb='machineID_modelID_status', col1='machineID', \
			 		data1=machine_name, col2='modelID', data2=None, \
					col3='machine_status', data3=status)

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
