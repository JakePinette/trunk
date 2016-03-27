from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

Builder.load_file('InfoPanel.kv')

class InfoPanel(Widget):

    vertexName = StringProperty()
    vertexTextInfo = StringProperty()
    vertexOutgoingEdges = StringProperty()
    vertexIncomingEdges = StringProperty()



    def __init__(self, **kwargs):
        
        super(InfoPanel, self).__init__(**kwargs)
        self.vertexName = 'this is Node Name' #this is where getInfo(for name)
        self.vertexTextInfo = 'This is Node info'
        self.vertexOutgoingEdges = 'This is outgoing Edge List'
        self.vertexIncomingEdges = 'This is the Incoming Edge List'


    def set_vertexName(self):
        self.vertexName = "Name set"
        
        
    def set_vertexTextInfo(self):
        self.vertexTextInfo = "Text Info Set"
        #this is where getinfo() for text info

    def set_vertexOutgoingEdges(self):
        self.vertexOutgoingEdges = "Outgoing Edges Set"
        #this is where getOutInfo() for outEdges
        
    def set_vertexIncomingEdges(self):
        self.vertexIncomingEdges = "Incoming Edges Set"
        #this is where getInfo() for InEdges

#----------------------------------------------------------------------------

class buildInfoPanel(App):
    def build(self):
        return InfoPanel()

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    buildInfoPanel().run()
