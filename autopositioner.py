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
		
		machine_list = ['I-41', 'I-40', 'I-39', 'I-38', 'I-37']
		mmpm = ("mmpm%d = MmpModule()" % (1 + 1));
		print(mmpm)
		for i in range(0, len(machine_list)):
			mmpm = "mmpm%d" % (i + 1)
			exec(mmpm + "= MmpModule()")
			exec(mmpm + ".ids.model_button.text = 'Wow: %d'" % i)
			exec("self.add_widget(" + mmpm + ")")
			# exec("mmp%d = MmpModule()" % (i + 1, repr(prices[i])));
		
		# machine_list[0].ids.machine_name.text = 'Wow'
		# machine_list[1].ids.machine_name.text = 'Neat'
		# self.add_widget(machine_list[0])
		# self.add_widget(machine_list[1])
			
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
