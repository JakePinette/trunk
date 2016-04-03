from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty
from kivy.properties import BooleanProperty, StringProperty
from kivy.properties import ObjectProperty
import Edge
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')

class Highlight(Widget):
    LW = NumericProperty(1)
    radius = NumericProperty(25)
    
class Vertex(Widget):
    
    red = NumericProperty(0.3)
    green = NumericProperty(1)
    blue = NumericProperty(0)
    alpha = NumericProperty(0.5)
    radius = NumericProperty(25)
    ID = NumericProperty(1)

    #Properties for use in Bellman Ford Searching
    bFParentExists = BooleanProperty(False)
    bFParent = ObjectProperty(None)
    bFDistanceExists = BooleanProperty(False)
    bFDistance = NumericProperty(0)

    incomingEdgeIndexes = ListProperty([])
    outgoingEdgeIndexes = ListProperty([])
    incomingEdges = ListProperty([])
    outgoingEdges = ListProperty([])

    name = StringProperty("")
    labelName = StringProperty('1')
    info = StringProperty("")
    
    label = ObjectProperty( None )
    highlight = ObjectProperty( None )
    
    namesOn = BooleanProperty(False)
    highlighted = BooleanProperty(False)
    selected = BooleanProperty(False)

    def select(self):
        if self.selected == False:
            if self.highlighted == False:
                h = Highlight()
                h.radius = self.radius
                self.highlight = h
                self.add_widget(self.highlight)
            self.highlight.pos[0] = self.center_x - self.radius
            self.highlight.pos[1] = self.center_y - self.radius
            self.selected = True
            self.highlight.LW = 2


    def unSelect(self):
        self.selected = False
        self.highlight.LW = 1
        if self.highlighted == False:
            self.remove_widget(self.highlight)

    def highlight(self):
        if self.highlighted == False:
            if self.selected == False:
                h = Highlight()
                self.highlight = h
                h.radius = self.radius
                self.add_widget(self.highlight)
            self.highlight.pos[0] = self.center_x - self.radius
            self.highlight.pos[1] = self.center_y - self.radius

            self.highlighted = True

    def unHighlight(self):
        self.highlighted = False
        if self.selected == False:
            self.remove_widget(self.highlight)
            
    #Get/Set Bellman Ford properties
    def setBFParentExists(self, truthValue):
        self.bFParentExists = truthValue

    def getBFParentExists(self):
        return self.bFParentExists

    def setBFParent(self, newParent):
        self.bFParent = newParent

    def getBFParent(self):
        return self.bFParent

    def setBFDistanceExists(self, truthValue):
        self.bFDistanceExists = truthValue

    def getBFDistanceExists(self):
        return self.bFDistanceExists

    def setBFDistance(self, newDist):
        self.bFDistance = newDist

    def getBFDistance(self):
        return self.bFDistance 
        
    #Get/Set ID
    def setID(self, num):
        if self.ID != num:
           self.ID = num
           self.setName(self.name)

    def getID(self):
        return self.ID

    #Getter setter for vertex radius
    def setRadius(self, radius):
        x = self.center_x
        y = self.center_y
        self.radius = radius
        self.center_x = x
        self.center_y = y

        if self.highlighted == True or self.selected == True:
            self.highlight.radius = self.radius

    def getRadius(self):
        return self.radius
    
    #Getter/Setters for Name/Info
    def setName(self, name):
        self.name = name
        if name == '':
            self.labelName = str(self.ID)
        else:
            self.labelName = str(self.ID) + "-" + name
        if self.namesOn == True:
            self.setNameInvisible()
            self.setNameVisible()

    def setInfo(self, info):
        self.info = info

    def setNameInfo(self, name, info):
        self.name = name
        if name == '':
            self.labelName = str(self.ID)
        else:
            self.labelName = str(self.ID) + "-" + name
        self.info = info

    def getName(self):
        return self.name

    def getInfo(self):
        return self.info

    def setNameVisible(self):
        self.namesOn = True
        self.label = Label(color=(0,0,0,1), text=self.labelName, center_x = self.center_x, center_y = self.center_y)
        self.add_widget(self.label)

    def setNameInvisible(self):
        if self.namesOn == True:
            self.namesOn = False
            self.remove_widget(self.label)

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

    #Getter/Setter for vertex Position
    def setPosition(self, x, y):
        self.center_x = x
        self.center_y = y

        for edge in self.incomingEdges:
            edge.changeToCoordinates(x,y)

        for edge in self.outgoingEdges:
            edge.changeFromCoordinates(x,y)
            
        if self.label != None:
            self.label.center_x = x
            self.label.center_y = y

        if self.selected == True or self.highlighted == True:
            self.highlight.pos[0] = self.center_x - self.radius
            self.highlight.pos[1] = self.center_y - self.radius

    def setInitialPosition(self,x,y):
        self.center_x = x
        self.center_y = y
        
        if self.label != None:
            self.label.center_x = x
            self.label.center_y = y

        for edge in self.incomingEdges:
            edge.changeToCoordinates(x,y)

        for edge in self.outgoingEdges:
            edge.changeFromCoordinates(x,y)

        if self.selected == True or self.highlighted == True:
            self.highlight.pos[0] = self.center_x - self.radius
            self.highlight.pos[1] = self.center_y - self.radius

    def getX(self):
        return self.center_x

    def getY(self):
        return self.center_y

    #Add/Get incoming/outgoing edge INDEXES
    def addIncomingEdgeIndex(self, edgeIndex):
        self.incomingEdgeIndexes.append(edgeIndex)

    def addOutgoingEdgeIndex(self, edgeIndex):
        self.outgoingEdgeIndexes.append(edgeIndex)

    def getIncomingEdgeIndexes(self):
        return self.incomingEdgeIndexes

    def getOutgoingEdgeIndexes(self):
        return self.outgoingEdgeIndexes

    #Add/Get incoming/outgoing edge OBJECTS
    def addIncomingEdge(self, edge):
        self.incomingEdges.append(edge)

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.append(edge)

    def getIncomingEdges(self):
        return self.incomingEdges

    def getOutgoingEdges(self):
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
