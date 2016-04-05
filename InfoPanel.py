from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Builder.load_file('InfoPanel.kv')

class InfoPanel(Widget):
    
    currentVertex = ObjectProperty(Vertex())    
    vertexName = StringProperty()
    vertexTextInfo = StringProperty()
    vertexOutgoingEdges = StringProperty()
    vertexIncomingEdges = StringProperty()



    def __init__(self, **kwargs):
        
        super(InfoPanel, self).__init__(**kwargs)
        self.vertexName = ''
        self.vertexTextInfo = ''
        self.vertexOutgoingEdges = 'This is outgoing Edge List'
        self.vertexIncomingEdges = 'This is the Incoming Edge List'


    def getData(self, v):
        self.currentVertex = v
        
        self.vertexName = v.getName()
        self.vertexTextInfo = v.getInfo()
        outgoing = v.getOutgoingEdges()
        incoming = v.getIncomingEdges()
        StringOutgoing = ""
        StringIncoming = ""

        for e in outgoing:
            fromV = e.getFromVertex()
            toV = e.getToVertex()
            StringOutgoing = StringOutgoing + str(fromV.getID())
            StringOutgoing = StringOutgoing + " -> "
            StringOutgoing = StringOutgoing + str(toV.getID())+ '  (Weight:' + str(e.getWeight()) + ')' + '\n'
            
        self.vertexOutgoingEdges = StringOutgoing

        for e in incoming:
            fromV = e.getFromVertex()
            toV = e.getToVertex()
            StringIncoming = StringIncoming + str(fromV.getID())
            StringIncoming = StringIncoming + " -> "
            StringIncoming = StringIncoming + str(toV.getID())+ '  (Weight: ' + str(e.getWeight()) + ')' + '\n'
        
        
    
        self.vertexIncomingEdges = StringIncoming
            

    def set_vertexName(self):
        self.vertexName = self.ids.nameBox.text 
        self.currentVertex.setName(self.vertexName)
        #print(self.currentVertex.getName())
        
        
    def set_vertexTextInfo(self):
        self.vertexTextInfo = self.ids.infoBox.text
        self.currentVertex.setInfo(self.vertexTextInfo)
        #print(self.currentVertex.getInfo())

    def set_vertexOutgoingEdges(self):
        self.vertexOutgoingEdges = ""
        #this is where getOutInfo() for outEdges
        
    def set_vertexIncomingEdges(self):
        self.vertexIncomingEdges = ""
        #this is where getInfo() for InEdges

#----------------------------------------------------------------------------

class buildInfoPanel(App):
    def build(self):
        box = BoxLayout()
        btn = Button(text = "testeroni")
        info = InfoPanel()
        box.add_widget(btn)
        box.add_widget(info)
        return box

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    buildInfoPanel().run()
