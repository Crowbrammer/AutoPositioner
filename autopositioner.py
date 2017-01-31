from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class AutoPositionerRoot(BoxLayout):
	pass

class ComboMeal(BoxLayout):
	machine_name = StringProperty()
	def __init__(self, **kwargs):
		super(ComboMeal, self).__init__(**kwargs)
		self.machine_name = 'Hello'

class MyListItemButton(ListItemButton):
	pass	
	
class AutopositionerApp(App):
	def build(self):
		AutoPositionerRoot()
		
if __name__ == '__main__':
	AutopositionerApp().run()
