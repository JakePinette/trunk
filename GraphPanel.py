from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')

class GraphPanel(Widget):

    currentVertex = NumericProperty( -1 )
    listOfVertices = ListProperty( [] )
    listOfEdges = ListProperty( [] )
    red = NumericProperty(1)
    green = NumericProperty(1)
    blue = NumericProperty(1)
    currentEdge = 0

    #NEW GRAPH
    def newGraph(self, numVertices):
        #First, tear down the old graph
        self.currentVertex = -1
        self.currentEdge = 0
        for e in range(0, len(self.listOfEdges)):
            self.remove_widget(self.listOfEdges[e])

        for v in range(0, len(self.listOfVertices)):
            self.remove_widget(self.listOfVertices[v])
            
        self.listOfEdges = []
        self.listOfVertices = []

        #Now initialize the new graph
        for x in range(0, numVertices):
            vertex = Vertex()
            vertex.setName(str(x))
            self.listOfVertices.append(vertex)
            self.add_widget(vertex)

    #WEIGHT OF EDGES

    def getEdgeWeight(edgeNo):
        return self.listOfEdges[edgeNo].getWeight()

    def setEdgeWeight(edgeNo, weight):
        self.listOfEdges[edgeNo].setWeight(weight)
        
    #NAME/INFO OF VERTICES
    def setVertexName(self, vertexNo, name):
        self.listOfVertices[vertexNo].setName(name)

    def setVertexNameInfo(self, vertexNo, name, info):
        self.listOfVertices[vertexNo].setNameInfo(name, info)

    def setVertexInfo(self, vertexNo, info):
        self.listOfVertices[vertexNo].setInfo(info)

    def getVertexName(self, vertexNo):
        return self.listOfVertices[vertexNo].getName()

    def getVertexInfo(self, vertexNo):
        return self.listOfVertices[vertexNo].getName()

    #SINGLE VERTEX COLOR
    def setVertexRed(self, vertexNo, red):
        self.listOfVertices[vertexNo].setRed(red)
        
    def setVertexGreen(self, vertexNo, green):
        self.listOfVertices[vertexNo].setGreen(green)
        
    def setVertexBlue(self, vertexNo, blue):
        self.listOfVertices[vertexNo].setBlue(blue)
        
    def setVertexAlpha(self, vertexNo, alpha):
        self.listOfVertices[vertexNo].setAlpha(alpha)

    def setVertexRGB(self, vertexNo, red, green, blue):
        self.listOfVertices[vertexNo].setRGB(red, green, blue)
        
    def setVertexRGBA(self, vertexNo, red, green, blue, alpha):
        self.listOfVertices[vertexNo].setRGBA(red, green, blue, alpha)
        
    def getVertexRed(self, vertexNo):
        return self.listOfVertices[vertexNo].getRed()
    
    def getVertexGreen(self, vertexNo):
        return self.listOfVertices[vertexNo].getGreen()
    
    def getVertexBlue(self, vertexNo):
        return self.listOfVertices[vertexNo].getBlue()

    def getVertexAlpha(self, vertexNo):
        return self.listOfVertices[vertexNo].getAlpha()

    #MODIFY COLOR FOR ALL VERTICES
    def setAllVertexRed(self, red):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setRed(red)
            
    def setAllVertexGreen(self, green):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setGreen(green)
        
    def setAllVertexBlue(self, blue):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setBlue(blue)
            
    def setAllVertexAlpha(self, alpha):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setAlpha(alpha)
            
    def setAllVertexRGB(self, red, green, blue):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setRGB(red, green, blue)
            
    def setAllVertexRGBA(self, red, green, blue, alpha):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setRGBA(red, green, blue, alpha)
        
    
    #MODIFY BACKGROUND COLOR
    def setBackgroundRed(self, red):
        self.red = red
        
    def setBackgroundGreen(self, green):
        self.green = green
        
    def setBackgroundBlue(self, blue):
        self.blue = blue
        
    def setBackgroundRGB(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def getBackgroundRed(self):
        return self.red
    
    def getBackgroundGreen(self):
        return self.green
    
    def getBackgroundBlue(self):
        return self.blue

    #MODIFY EDGE COLOR
    def setEdgeRed(self, edgeNo, red):
        self.listOfEdges[edgeNo].setRed(red)

    def setEdgeGreen(self, edgeNo, green):
        self.listOfEdges[edgeNo].setGreen(green)

    def setEdgeBlue(self, edgeNo, blue):
        self.listOfEdges[edgeNo].setBlue(blue)

    def setEdgeRGB(self, edgeNo, red, green, blue):
        self.listOfEdges[edgeNo].setRGB(red, green, blue)

    def setEdgeRGBA(self, edgeNo, red, green, blue, alpha):
        self.listOfEdges[edgeNo].setRGBA(red, green, blue, alpha)

    def getEdgeRed(self, edgeNo):
        return self.listOfEdges[edgeNo].getRed()

    def getEdgeGreen(self, edgeNo):
        return self.listOfEdges[edgeNo].getGreen()

    def getEdgeBlue(self, edgeNo):
        return self.listOfEdges[edgeNo].getBlue()

    def getEdgeAlpha(self, edgeNo):
        return self.listOfEdges[edgeNo].getAlpha()

    #MODIFY COLOR OF ALL EDGES

    def setAllEdgeRed(self, red):
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].setRed(red)

    def setAllEdgeGreen(self, green):
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].setGreen(green)

    def setAllEdgeBlue(self, blue):
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].setBlue(blue)

    def setAllEdgeRGB(self, red, green, blue):
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].setRGB(red, green, blue)

    def setAllEdgeRGBA(self, red, green, blue, alpha):
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].setRGBA(red, green, blue, alpha)
    
    #SET NAMES VISIBLE/INVISIBLE
    def setNamesVisible(self):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameVisible()

    def setNamesInvisible(self):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameInvisible()

    #SET POSITION OF VERTEX
    def setVertexPosition(self, vertexNo, x, y):
        self.listOfVertices[vertexNo].setInitialPosition(x,y)
        self.listOfVertices[vertexNo].setAlpha(1)

    #ADD EDGE
    def addEdge(self, vertexFromIndex, vertexToIndex, weight):
        edge = Edge()
        self.add_widget(edge)
        edge.setWeight(weight)
        edge.setVertices(self.listOfVertices[vertexFromIndex], self.listOfVertices[vertexToIndex])
        self.listOfEdges.append(edge)
        self.listOfVertices[vertexFromIndex].addOutgoingEdge(self.currentEdge)
        self.listOfVertices[vertexToIndex].addIncomingEdge(self.currentEdge)
        self.currentEdge = self.currentEdge + 1


    #DRAG VERTICES
    def on_touch_down(self, touch):
        for v in range(0, len(self.listOfVertices)):
            if self.listOfVertices[v].collide_point(touch.x, touch.y):
                self.currentVertex = v
                self.listOfVertices[v].click()
                break
            
    def on_touch_up(self, touch):
        if self.currentVertex != (-1):
            self.listOfVertices[self.currentVertex].unClick()
            self.currentVertex = -1
        
    def on_touch_move(self, touch):
        if self.currentVertex != (-1):
            v = self.currentVertex
            if self.listOfVertices[v].isClicked():
                self.listOfVertices[v].setPosition(touch.x, touch.y)
                for e in self.listOfVertices[v].getIncomingEdgeIndexes():
                    self.listOfEdges[e].changeToCoordinates(touch.x, touch.y)
                
                for j in self.listOfVertices[v].getOutgoingEdgeIndexes():
                    self.listOfEdges[j].changeFromCoordinates(touch.x, touch.y)
    

class GraphPanelApp(App):
    def build(self):
        graphPanel = GraphPanel()
        graphPanel.newGraph(4)
        graphPanel.setVertexPosition(0, 100, 100)
        graphPanel.setVertexPosition(1, 200, 200)
        graphPanel.setVertexPosition(2, 300, 100)
        graphPanel.setVertexPosition(3, 200, 300)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        graphPanel.addEdge(2, 1, 6)
        graphPanel.addEdge(1, 3, 7)
        graphPanel.addEdge(0, 3, 8)

        graphPanel.listOfVertices[1].setRadius(10)
        graphPanel.listOfVertices[0].setRGB(1,0,0)
        graphPanel.listOfVertices[2].setName("Hello")
        graphPanel.setNamesVisible()

        return graphPanel

if __name__ == '__main__':
    GraphPanelApp().run()
