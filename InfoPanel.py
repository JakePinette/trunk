from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder

Builder.load_file('InfoPanel.kv')

class InfoPanel(Widget):

    vertexTextInfo = StringProperty()
    vertexOutgoingEdges = StringProperty()
    vertexIncomingEdges = StringProperty()



    def __init__(self, **kwargs):
        
        super(InfoPanel, self).__init__(**kwargs)
        
        self.vertexTextInfo = 'This is Node info'
        self.vertexOutgoingEdges = 'This is outgoing Edge List'
        self.vertexIncomingEdges = 'This is the Incoming Edge List'

    def set_vertexTextInfo(self):
        self.vertexTextInfo = "Test Complete, it works!"
        #this is where getinfo()

    def set_vertexOutgoingEdges(self):
        self.vertexOutgoingEdges = "TESTYTEST"
        #this is where getOutInfo()

    def set_vertexIncomingEdges(self):
        self.vertexIncomingEdges = "TESTYTEST TEEEST"
        #this is where getInInfo()

class buildInfoPanel(App):
    def build(self):
        return InfoPanel()

if __name__ == '__main__':
    buildInfoPanel().run()
