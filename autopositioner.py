from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MachineWidget(Widget):
    def __init__(self, **kwargs):
        super(MachineWidget, self).__init__(**kwargs)

class ContainerBox(GridLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class autopositioner(App):
	def build(self):
		return MachineWidget()
		
if __name__ == "__main__":
	autopositioner().run()