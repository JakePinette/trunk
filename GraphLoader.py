#code partially gotten from the kivy api

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from GraphPanel import GraphPanel
from InfoPanel import InfoPanel
from VertexPositionAlg import visualize
from kivy.lang import Builder

Builder.load_file("Editor.kv")
import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
   


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = StringProperty("")
    graph = ObjectProperty(GraphPanel())
    def set_graph(self, g):
        self.graph = g
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self, touch):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):

        self.dismiss_popup()
        self.graph.loadGraph(filename[0])
        visualize(self.graph)
        self.graph.setNamesVisible()
      




class Editor(App):
	def build(self):
	#layout for graph and button
		layout = BoxLayout()
		#root is the root class as above
		root = Root()
		graph = GraphPanel()
		#sets the root's graph as the graph that was made
		root.set_graph(graph)
		
		btnLoad = Button(text = "Load graph")
		btnLoad.bind(on_release=root.show_load)
		
		
		
		
		layout.add_widget(graph)
		layout.add_widget(btnLoad)
	
		return layout

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)



if __name__ == '__main__':
    Editor().run()
