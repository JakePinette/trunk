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

Builder.load_file('NbhPanel.kv')

class NbhPanel(Widget):
    
    currentVertex = ObjectProperty(Vertex())
    currentVertexNo = StringProperty()

    nbhSize = StringProperty()

    workingGraph = ObjectProperty(GraphPanel())

    
    def __init__(self, **kwargs):
        super(NbhPanel, self).__init__(**kwargs)
        currentVertexNo = ''

    def isInt(self, num):
        try: 
            int(num)
            return True
        except ValueError:
            return False

    def set_NbhSize(self, graph):
        value = self.ids.sizeBox.text
        
        if self.isInt(value):
            self.nbhSize = value
        else:
            print("non Integer value given please use Integer Values")

    def set_workingGraph(self, graph):
        self.workingGraph = graph

        
class buildNbhPanel(App):
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
        
        nbh = NbhPanel()
        nbh.set_workingGraph(graphPanel)
        
        box.add_widget(nbh)
        box.add_widget(graphPanel)
        
        return box

if __name__ == '__main__':
    buildNbhPanel().run()

