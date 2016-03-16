from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')


class Edge(Scatter):

    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(0)
    alpha = NumericProperty(1)
    width = NumericProperty(1)
    weight = NumericProperty(1)

    x = NumericProperty(0)
    y = NumericProperty(0)
    xx = NumericProperty(0)
    yy = NumericProperty(0)
    points = ReferenceListProperty(x, y, xx, yy)

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

    #WIDTH
    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    #WEIGHT
    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self, weight):
        return self.weight

    #MOVE FUNCTIONS
    def changeFromCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
        
    def changeToCoordinates(self, newX, newY):
        self.xx = newX
        self.yy = newY

    #INITIALIZATION
    def setVertices(self, vertexFrom, vertexTo):
        self.x = vertexFrom.getX()
        self.y = vertexFrom.getY()
        self.xx = vertexTo.getX()
        self.yy = vertexTo.getY()
        self.points = (self.x, self.y, self.xx, self.yy)    
        
class TestPanel(Widget):
    pass

class EdgeApp(App):
    def build(self):
        mainPanel = TestPanel()
        mainPanel.add_widget(Edge())
        return mainPanel

if __name__ == '__main__':
    EdgeApp().run()
