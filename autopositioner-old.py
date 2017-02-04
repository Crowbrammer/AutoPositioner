import libs.apa_database
import inspect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, Property
#from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class AutoPositionerRoot(BoxLayout):
	def __init__(self, **kwargs):
		super(AutoPositionerRoot, self).__init__(**kwargs)
		# for i in all_active_machines:
			# check the model_in_the_machine
			# check the positions required for the model_in_the_machine
			# generate a tuple of positions ID's mach_model_pos
		# for num_machines in machine_list:
			# self.add_widget(MmpModule())
			# current_module_machine_name = machine_list[num_machine]
			# current_module_model_name = dropdown_list_of_models
			# list_view_thing = ready_to_be_updated
					
		machine_list = libs.apa_database.get_data('machineID_modelID_status', 				order_by_column='machineID')
		
		
		
		
		for i in range(0, len(machine_list)):
		
			mmpm[] = "mmpm%d" % (i + 1)
			exec(mmpm + "= MmpModule()")
			exec("mymodel = " + mmpm + ".ids.machine_button.text")
			exec(mmpm + ".ids.machine_button.text = 'Wow: %s'" % machine_list[i][0])
			exec(mmpm + ".ids.model_button.text = 'Wow: %s'" % machine_list[i][1])
			exec("mymodel = " + mmpm + ".ids.machine_button.text")
			print(mymodel))
			
			#positions_to_fill = libs.apa_database.get_data(
			#table_name='modelID_position', column_name='modelID', model=mymodel, #order_by_column='position_num')
			
			#for i in range(0, len(positions_to_fill)):
				#print(positions_to_fill[i][0] + str(positions_to_fill[i][1]))
				#exec(mmpm + ".ids.position%d.text = '%s'" % i + 1, positions_to_fill[i][0] + positions_to_fill[i][1])
				
			exec("self.add_widget(" + mmpm + ")")

	def position_people(self):
		
		# Get a list of all the available people
		
		# c.execute('SELECT teammate FROM teammate_modelID_position WHERE modelID=current_model AND position_num=current_position')
			
		# available_people = c.fetchall
		
		# print(available_people)
		
		# # Compare the training of each person with the list 
		# c.execute('SELECT * FROM teammate_modelID_position WHERE modelID=current_position)
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
		
class AutopositionerApp(App):
	def build(self):
		AutoPositionerRoot()
		
		
if __name__ == '__main__':
	AutopositionerApp().run()
