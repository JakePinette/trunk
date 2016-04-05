from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from GraphPanel import GraphPanel
from BellmanFord import BellmanFord

Builder.load_file('SearchPanel.kv')

class SearchPanel(Widget):

    currentVertex = ObjectProperty(Vertex())
    currentVertexNo = StringProperty()
    
    nextVertex = ObjectProperty(Vertex())
    nextVertexNo = StringProperty()

    workingGraph = ObjectProperty(GraphPanel())

    path = StringProperty()

    listpath = ListProperty()
    
    def __init__(self, **kwargs):
        super(SearchPanel, self).__init__(**kwargs)
        self.currentVertexNo = "0"
        self.nextVertexNo = "0"
        self.path =  "Path Will Be Displayed Here"

    def isInt(self, num):
        try: 
            int(num)
            return True
        except ValueError:
            return False

    def set_fromVertex(self, graph):
        value = self.ids.fromBox.text
        self.currentVertexNo = value
        if self.isInt(value):
            if  int(self.currentVertexNo) < 0 or int(self.currentVertexNo) >= len(graph.listOfVertices):
                self.path = "invalid Index entered"
                print len(graph.listOfVertices)
                return False
            
            graphArray = graph.getVertexList()
            self.currentVertex = graphArray[int(self.currentVertexNo)]
        else:
            self.path = "non Integer value given please use Integer Values"

    def set_toVertex(self, graph):
        value = self.ids.toBox.text
        self.nextVertexNo = value
        if self.isInt(value):
            if  int(self.nextVertexNo) < 0 or int(self.nextVertexNo) >= len(graph.listOfVertices):
                self.path = "invalid Index entered"
                print len(graph.listOfVertices)
                return False
            
            graphArray = graph.getVertexList()
            self.nextVertex = graphArray[int(self.nextVertexNo)]
        else:
            self.path = "non Integer value given please use Integer Values"

    def set_workingGraph(self, graph):
        self.workingGraph = graph

    def initialize(self, graph):
        self.workingGraph = graph
        
        
    def doSearch(self, graph, fromN, toN):
        bfsearch = BellmanFord()
        self.listPath = bfsearch.findShortestPath(self.workingGraph, self.currentVertex.getID(), self.nextVertex.getID())

    def performTask(self, graph, fromN, toN):
        if self.set_fromVertex(self.workingGraph) == False:
            return
        if self.set_toVertex(self.workingGraph) == False:
            return
        self.doSearch(self.workingGraph, self.currentVertex, self.nextVertex)
        print self.currentVertex.getID()
        print self.nextVertex.getID()
        
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
        graphPanel.setNamesVisible()
        search = SearchPanel()
        search.set_workingGraph(graphPanel)
        
        box.add_widget(search)
        box.add_widget(graphPanel)
        
        return box

if __name__ == '__main__':
    buildSearchPanel().run()
