import libs.apa_database
import inspect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, Property

class AutoPositionerRoot(BoxLayout):

	def __init__(self, **kwargs):
	
		super(AutoPositionerRoot, self).__init__(**kwargs)
		machine_list = libs.apa_database.get_data('machineID_modelID_status', 				order_by_column='machineID')
		
		for i in range(0, len(machine_list)):
		
			mmpm = "mmpm%d" % (i + 1)
			exec(mmpm + "= MmpModule()")
			
			# - - - - - - - - - - - - - - - - - - - - - - - - 
			
			# Why is this exec() function not working?
			
			# - - - - - - - - - - - - - - - - - - - - - - - - 
			
			exec("mymodel = 'hello'")
			print(mymodel)
			
			# - - - - - - - - - - - - - - - - - - - - - - - - 
			
			# Output: NameError: name 'mymodel' is not defined
			
			# - - - - - - - - - - - - - - - - - - - - - - - - 
			
			exec(mmpm + ".ids.machine_button.text = 'Wow: %s'" % machine_list[i][0])
			exec(mmpm + ".ids.model_button.text = 'Wow: %s'" % machine_list[i][1])
			exec("mymodel = " + mmpm + ".ids.machine_button.text")
			print(mymodel)				
			exec("self.add_widget(" + mmpm + ")")

	def position_people(self):
		
		pass
	
	def prioritize_position_by_training(self):
		
		pass
		
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
