from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from Edge import Edge
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')


class Vertex(Widget):
    
    red = NumericProperty(0.3)
    green = NumericProperty(1)
    blue = NumericProperty(0)
    alpha = NumericProperty(0.8)
    radius = NumericProperty(25)

    incomingEdges = []
    outgoingEdges = []

    name = StringProperty("")
    info = StringProperty("")

    def setName(self, name):
        self.name = name

    def setInfo(self, info):
        self.info = info

    def setNameInfo(self, name, info):
        self.name = name
        self.info = info

    def setRGB(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def setRGBA(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def setRed(self, red):
        self.red = red

    def setGreen(self, green):
        self.green = green

    def setBlue(self, blue):
        self.blue = blue

    def setAlpha(self, alpha):
        self.alpha = alpha

    def setPosition(self, x, y):
        self.center_x = x
        self.center_y = y

    def getX(self):
        return self.center_x

    def getY(self):
        return self.center_y

    def addIncomingEdge(self, edgeIndex):
        self.incomingEdges.append(edgeIndex)

    def addOutgoingEdge(self, edgeIndex):
        self.outgoingEdges.append(edgeIndex)

    def getIncomingEdgeIndexes(self):
        return self.incomingEdges

    def getOutgoingEdgeIndexes(self):
        return self.outgoingEdges


class MainPanel(Widget):
    pass

class VertexApp(App):
    def build(self):
        mainPanel = MainPanel()
        vertex1 = Vertex(pos = (100,100), radius = 25)
        vertex2 = Vertex(pos = (200,200), radius = 25)
        edge = Edge()
        edge.setVertices(vertex1, vertex2)
        mainPanel.add_widget(edge)
        mainPanel.add_widget(vertex1)
        mainPanel.add_widget(vertex2)
        return mainPanel

if __name__ == '__main__':
    VertexApp().run()
