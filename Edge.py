from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty
from kivy.lang import Builder
from Vertex import Vertex
import math


class Edge(Widget):

    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(0)
    alpha = NumericProperty(1)
    weight = NumericProperty(1)

    x = NumericProperty(0)
    y = NumericProperty(0)
    xx = NumericProperty(0)
    yy = NumericProperty(0)
    points = ReferenceListProperty(x, y, xx, yy)

    x1 = NumericProperty(0)
    y1 = NumericProperty(0)
    x2 = NumericProperty(0)
    y2 = NumericProperty(0)
    x3 = NumericProperty(0)
    y3 = NumericProperty(0)
    
    arrowWidth = NumericProperty(4)
    arrowPoints = ReferenceListProperty( x1, y1, x2, y2, x3, y3)

    fromVertex = ObjectProperty(Vertex())
    toVertex = ObjectProperty(Vertex())

    def getFromVertex(self):
        return self.fromVertex

    def getToVertex(self):
        return self.toVertex
    
    #COLORS
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

    #WEIGHT
    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    #MOVE FUNCTIONS
    def changeFromCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
        self.updateArrow()
        
    def changeToCoordinates(self, newX, newY):
        self.xx = newX
        self.yy = newY
        self.updateArrow()

    def updateArrow(self):
        if self.x == self.xx: #vertical line
            self.x1 = self.x
            self.x2 = self.x + self.arrowWidth
            self.x3 = self.x - self.arrowWidth
            midY = (self.yy + self.y)/2
            self.y1 = self.yy
            self.y2 = midY
            self.y3 = midY
            self.arrowPoints = [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]
            return

        if self.y == self.yy: #horizontal line
            self.y1 = self.y
            self.y2 = self.y + self.arrowWidth
            self.y3 = self.y - self.arrowWidth
            midX = (self.x + self.xx)/2
            self.x1 = self.xx
            self.x2 = midX
            self.x3 = midX
            self.arrowPoints = [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]
            return

        w = self.arrowWidth*self.arrowWidth
        midX = (self.x + self.xx)/2
        midY = (self.y + self.yy)/2
        slope = (self.yy - self.y + 0.0)/(self.xx - self.x)
        invSlope = -1.0/slope
        xMove = (int)(w/(1 + invSlope*invSlope))**(0.5)
        yMove = (int)(w - (w/(1 + invSlope*invSlope)))**(0.5)
        
        if slope > 0:
            self.x1 = midX + xMove
            self.x2 = midX - xMove
            self.y1 = midY - yMove
            self.y2 = midY + yMove
        else:
            self.x1 = midX + xMove
            self.x2 = midX - xMove
            self.y1 = midY + yMove
            self.y2 = midY - yMove
            
        self.x3 = self.xx
        self.y3 = self.yy
        self.arrowPoints = [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]

    #INITIALIZATION
    def setVertices(self, vertexFrom, vertexTo):
        self.fromVertex = vertexFrom
        self.toVertex = vertexTo
        vertexFrom.addOutgoingEdge(self)
        vertexTo.addIncomingEdge(self)
        self.x = vertexFrom.getX()
        self.y = vertexFrom.getY()
        self.xx = vertexTo.getX()
        self.yy = vertexTo.getY()
        self.points = (self.x, self.y, self.xx, self.yy)
        self.updateArrow()
        
class TestPanel(Widget):
    pass

class EdgeApp(App):
    def build(self):
        mainPanel = TestPanel()
        mainPanel.add_widget(Edge())
        return mainPanel

if __name__ == '__main__':
    EdgeApp().run()
