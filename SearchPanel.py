from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from GraphPanel import GraphPanel

Builder.load_file('SearchPanel.kv')

class SearchPanel(Widget):

    currentVertex = ObjectProperty(Vertex())
    currentVertexNo = StringProperty()
    
    nextVertex = ObjectProperty(Vertex())
    nextVertexNo = StringProperty()

    workingGraph = ObjectProperty(GraphPanel())

    path = StringProperty()
    
    def __init__(self, **kwargs):
        super(SearchPanel, self).__init__(**kwargs)
        self.currentVertexNo = "0"
        self.nextVertexNo = "0"
        self.path =  "blank"

    def isInt(self, num):
        try: 
            int(num)
            return True
        except ValueError:
            return False

    def set_fromVertex(self, graph):
        value = self.ids.fromBox.text
        if self.isInt(value):
            self.currentVertexNo = value
            graphArray = graph.getVertexList()
            self.currentVertex = graphArray[int(self.currentVertexNo)]
        else:
            self.path = "non Integer value given please use Integer Values"

    def set_toVertex(self, graph):
        value = self.ids.toBox.text
        if self.isInt(value):
            self.nextVertexNo = value
            graphArray = graph.getVertexList()
            self.currentVertex = graphArray[int(self.currentVertexNo)]
        else:
            self.path = "non Integer value given please use Integer Values"

    def set_workingGraph(self, graph):
        self.workingGraph = graph

    def initialize(self, graph):
        self.set_fromVertex(graph)
        self.set_toVertex(graph)
        
        
class buildSearchPanel(App):
    def build(self):
        box = BoxLayout()
        graphPanel = GraphPanel()
        
        graphPanel.newGraph(4)
        graphPanel.setVertexPosition(0, 600, 100)
        graphPanel.setVertexPosition(1, 650, 200)
        graphPanel.setVertexPosition(2, 700, 100)
        graphPanel.setVertexPosition(3, 600, 300)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        graphPanel.addEdge(1, 0 ,2)
        graphPanel.addEdge(0, 3, 8)
        
        search = SearchPanel()
        search.set_workingGraph(graphPanel)
        
        box.add_widget(search)
        box.add_widget(graphPanel)
        
        return box

if __name__ == '__main__':
    buildSearchPanel().run()
