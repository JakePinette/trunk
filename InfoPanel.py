from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder

from kivy.event import EventDispatcher

Builder.load_file('InfoPanel.kv')


class InfoPanel(Widget):

    vertexTextInfo = StringProperty( '' )
    vertexOutgoingEdges = StringProperty( '' )
    vertexIncomingEdges = StringProperty( '' )



    def __init__(self): #*args, **kwargs
        super(InfoPanel, self).__init__() #*args, **kwargs
        self.vertexTextInfo = 'This is Node info'
        self.vertexOutgoingEdges = 'This is outgoing Edge List'
        self.vertexIncomingEdges = 'This is the Incoming Edge List'
        
        self.bind(vertexTextInfo=self.set_vertexTextInfo)
        self.bind(vertexOutgoingEdges=self.set_vertexOutgoingEdges)
        self.bind(vertexIncomingEdges=self.set_vertexIncomingEdges)

    def set_vertexTextInfo(self, instance, value):
        self.vertexTextInfo = 'Test Complete, it works!' #this is where getinfo()

    def set_vertexOutgoingEdges(self, instance, value):
        self.vertexOutgoingEdges = 'TESTYTEST' #this is where getOutInfo()

    def set_vertexIncomingEdges(self, instance, value):
        self.vertexIncomingEdges = 'TESTYTEST TEEEST' #this is where getInInfo()

class buildInfoPanel(App):
    def build(self):
        panel = InfoPanel()
        self.add_widget(panel)
        return InfoPanel()
    
