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

    x = NumericProperty(0)
    y = NumericProperty(0)
    xx = NumericProperty(0)
    yy = NumericProperty(0)
    points = ReferenceListProperty(x, y, xx, yy)

    def update(self):
        self.canvas.ask_update()
    
    def changeFromCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
        #points = (self.x, self.y, self.xx, self.yy)
        
    def changeToCoordinates(self, newX, newY):
        self.xx = newX
        self.yy = newY
        #points = (self.x, self.y, self.xx, self.yy)
        
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
