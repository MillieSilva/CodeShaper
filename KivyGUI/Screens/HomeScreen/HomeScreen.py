## System Imports


## Application Imports
from KivyGUI import utils, App
from Library.Managers import Shaping
from Library.Shaping.Project.data import ShapingConfiguration, ShapingProject


## Library Imports
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase


class HomeScreen(Screen):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def on_kv_post(self, base_widget):
		self.ids.screens.current = 'project_details_screen'
		self.ids.screens.current = 'recent_projects_screen'
		
		for configuration in Shaping.configurations:
			self.ids.configurations_layout.add_widget(ConfigurationItem(configuration))
		
		for project in Shaping.projects:
			self.ids.projects_layout.add_widget(ProjectItem(project))
	
	def show_configuration(self, configuration):
		self.ids.screens.current = 'project_details_screen'
		self.ids.screens.current_screen.show_configuration(configuration)


class Tab(FloatLayout, MDTabsBase):
	pass


class ConfigurationItem(ScrollView):
	
	def __init__(self, configuration: ShapingConfiguration):
		super().__init__()
	
		self.configuration = configuration
		
		self.ids.name.text = configuration.name
		self.ids.path.text = configuration.target
	
	def on_open(self):
		App.get_running_app().root.screens[0].show_configuration(self.configuration)


class ProjectItem(ScrollView):
	
	def __init__(self, project: ShapingProject):
		super().__init__()
		
		self.project = project
		
		self.ids.name.text = project.configuration.name
		self.ids.path.text = project.configuration.target

