from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty
from kivy.properties import BooleanProperty, StringProperty
from kivy.properties import ObjectProperty
from Edge import Edge
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')


class Vertex(Widget):
    
    red = NumericProperty(0.3)
    green = NumericProperty(1)
    blue = NumericProperty(0)
    alpha = NumericProperty(0.8)
    radius = NumericProperty(25)

    incomingEdges = ListProperty([])
    outgoingEdges = ListProperty([])

    name = StringProperty("")
    info = StringProperty("")
    label = ObjectProperty( None )

    clickState = BooleanProperty(False)

    #Getter setter for vertex radius
    def setRadius(self, radius):
        x = self.center_x
        y = self.center_y
        self.radius = radius
        self.center_x = x
        self.center_y = y

    def getRadius(self):
        return self.radius
    
    #Getter/Setters for Name/Info
    def setName(self, name):
        self.name = name

    def setInfo(self, info):
        self.info = info

    def setNameInfo(self, name, info):
        self.name = name
        self.info = info

    def getName(self):
        return self.name

    def getInfo(self):
        return self.info

    def setNameVisible(self):
        self.label = Label(color=(0,0,0,1), text=self.name, center_x = self.center_x, center_y = self.center_y)
        self.add_widget(self.label)

    def setNameInvisible(self):
        self.remove_widget(self.label)
        self.label = None

    #Getter/Setter For Colors
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

    def getRed(self):
        return self.red

    def getGreen(self):
        return self.green

    def getBlue(self):
        return self.blue

    def getAlpha(self):
        return self.alpha

    #Vertex clickstate for touch events
    def click(self):
        self.clickState = True

    def unClick(self):
        self.clickState = False

    def isClicked(self):
        return self.clickState

    #Getter/Setter for vertex Position
    def setPosition(self, x, y):
        if self.isClicked():
            self.center_x = x
            self.center_y = y

            if self.label != None:
                self.label.center_x = x
                self.label.center_y = y

    def setInitialPosition(self,x,y):
        self.center_x = x
        self.center_y = y

    def getX(self):
        return self.center_x

    def getY(self):
        return self.center_y

    #Add/Get incoming/outgoing edges
    def addIncomingEdge(self, edgeIndex):
        self.incomingEdges.append(edgeIndex)

    def addOutgoingEdge(self, edgeIndex):
        self.outgoingEdges.append(edgeIndex)

    def getIncomingEdgeIndexes(self):
        return self.incomingEdges

    def getOutgoingEdgeIndexes(self):
        return self.outgoingEdges

    def collide(self, x, y):
        if ((self.center_x - x)**(2) + (self.center_y - y)**(2)) <= self.radius**2:
            return True
        return False


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
