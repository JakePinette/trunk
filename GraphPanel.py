from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.properties import ObjectProperty
from Edge import Edge
from Vertex import Vertex
from InfoPanel import InfoPanel
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')

class GraphPanel(Widget):

    currentVertex = NumericProperty( -1 )
    listOfVertices = ListProperty( [] )
    listOfEdges = ListProperty( [] )
    dataColector = ObjectProperty(InfoPanel())

    defaultRadius = NumericProperty(25)
    red = NumericProperty(1)
    green = NumericProperty(1)
    blue = NumericProperty(1)

    lastX = NumericProperty(-1)
    lastY = NumericProperty(-1)
    dragging = BooleanProperty(False)
    namesOn = BooleanProperty(False)
    currentEdge = 0

    firstClick = BooleanProperty( False )
    lastSelected = ObjectProperty( None )

    dragSensitivity = NumericProperty(0.5)

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
            vertex.setID(x)
            vertex.pos = self.pos
            vertex.setID(x)
            self.listOfVertices.append(vertex)
            self.add_widget(vertex)

    #SET DATA COLECTOR
    def setDataColector(self, colector):
        self.dataColector = colector

    
    #MAKE GRAPH FROM FILE
    def loadGraph(self, filePath):
        numDeclaredEdges = -1
        numAddedEdges = 0
        verticesLoaded = False
        edgeNumLoaded = False
        f = open(filePath)
        for line in f.readlines():
            if(verticesLoaded == False):
                self.newGraph(int(line))
                verticesLoaded = True
            elif(edgeNumLoaded == False):
                numDeclaredEdges = int(line)
                edgeNumLoaded = True
            else:
                vertexFromIndex = -1
                vertexToIndex = -1
                edgeWeight = 0
                numStart = -1
                for i in range(0, len(line)-1):
                    if(line[i]!=" "):
                            if(numStart<0):
                                numStart = i
                    else:
                        if(numStart > -1):
                            if(vertexFromIndex<0):
                                vertexFromIndex = int(line[numStart:i])
                                numStart = -1
                                
                            elif(vertexToIndex<0):
                                vertexToIndex = int(line[numStart:i])
                                numStart = -1

                            else:
                                
                                vertexToIndex = float(line[numStart:i])
                                numStart = -1
                        
                self.addEdge(vertexFromIndex, vertexToIndex, edgeWeight)

    #DRAG SENSITIVITY
    def setDragSensitivity(self, sensitivity):
        self.dragSensitivity = sensitivity

    def getDragSensitivity(self):
        return self.dragSensitivity
    
    #RADIUS
    def setDefaultVertexRadius(self, radius):
        self.defaultRadius = radius
        arrowWidth = max(3,(int)(round(radius/5.0)))
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setRadius(radius)
        for e in range(0, len(self.listOfEdges)):
            self.listOfEdges[e].arrowWidth = arrowWidth
            self.listOfEdges[e].updateArrow()

    def getDefaultVertexRadius(self):
        return self.defaultRadius

    def setVertexRadius(self, vertexNo, radius):
        self.listOfVertices[vertexNo].setRadius(radius)

    def getVertexRadius(self, vertexNo):
        return self.listOfVertices[vertexNo].getRadius()

    #WEIGHT OF EDGES
    def getEdgeWeight(self, edgeNo):
        return self.listOfEdges[edgeNo].getWeight()

    def setEdgeWeight(self, edgeNo, weight):
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
        self.namesOn = True
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameVisible()

    def setNamesInvisible(self):
        self.namesOn = False
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameInvisible()

    #SET POSITION OF VERTEX
    def setVertexPosition(self, vertexNo, x, y):
        self.listOfVertices[vertexNo].setAlpha(1)
        self.listOfVertices[vertexNo].setInitialPosition(x,y)
        
        for e in self.listOfVertices[vertexNo].getIncomingEdgeIndexes():
            self.listOfEdges[e].changeToCoordinates(x,y)
            
        for e in self.listOfVertices[vertexNo].getOutgoingEdgeIndexes():
            self.listOfEdges[e].changeFromCoordinates(x,y)
            
        
        if (self.namesOn):
            self.listOfVertices[vertexNo].setNameVisible()

    #ADD EDGE
    def addEdge(self, vertexFromIndex, vertexToIndex, weight):
        edge = Edge()
        self.add_widget(edge)
        edge.setWeight(weight)
        edge.setVertices(self.listOfVertices[vertexFromIndex], self.listOfVertices[vertexToIndex])
        self.listOfEdges.append(edge)
        self.listOfVertices[vertexFromIndex].addOutgoingEdgeIndex(self.currentEdge)
        self.listOfVertices[vertexToIndex].addIncomingEdgeIndex(self.currentEdge)
        self.currentEdge = self.currentEdge + 1

    #TRAVERSAL METHODS
    def getVertexList(self):
        return self.listOfVertices

    def getEdgeList(self):
        return self.listOfEdges

    def getOutgoingEdges(self, vertexNo):
        return self.listOfVertices[vertexNo].getOutgoingEdges()

    def getIncomingEdges(self, vertexNo):
        return self.listOfVertices[vertexNo].getIncomingEdges()

    def getVertex(self, vertexNo):
        return self.listOfVertices[vertexNo]

    def getEdge(self, edgeNo):
        return self.listOfEdges[edgeNo]


    #DRAG VERTICES/GRAPH
    def on_touch_down(self, touch):
        for v in range(0, len(self.listOfVertices)):
            if self.listOfVertices[v].collide(touch.x, touch.y):
                self.currentVertex = v
                self.dataColector.getData(self.listOfVertices[v])
                if self.firstClick == False:
                    self.firstClick = True
                    self.lastSelected = self.listOfVertices[v]
                    self.lastSelected.select()
                else:
                    self.lastSelected.unSelect()
                    self.lastSelected = self.listOfVertices[v]
                    self.lastSelected.select()
                return
        self.dragging = True
        self.lastX = touch.x
        self.lastY = touch.y
            
    def on_touch_up(self, touch):
        if self.currentVertex != (-1):
            self.currentVertex = -1
            
        self.dragging = False
        
    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y) == False:
            return
        if self.dragging == True:
            dragX = touch.x - self.lastX
            dragY = touch.y - self.lastY
            self.lastX = touch.x
            self.lastY = touch.y
            for v in range(0, len(self.listOfVertices)):
                vertex = self.listOfVertices[v]
                newX = vertex.getX() + dragX*self.dragSensitivity
                newY = vertex.getY() + dragY*self.dragSensitivity
                
                vertex.setPosition(newX, newY)
                
                for e in vertex.getIncomingEdges():
                    e.changeToCoordinates(newX, newY)
                
                for e in vertex.getOutgoingEdges():
                    e.changeFromCoordinates(newX, newY)

                
        if self.currentVertex != (-1):
            v = self.currentVertex
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
        graphPanel.addEdge(1, 0 ,2)
        graphPanel.addEdge(0, 3, 8)

        graphPanel.listOfVertices[1].setRadius(10)
        graphPanel.listOfVertices[0].setRGB(1,0,0)
        graphPanel.listOfVertices[2].setName("Hello")
        graphPanel.setNamesVisible()

        graphPanel.listOfVertices[1].highlight()

        return graphPanel

if __name__ == '__main__':
    GraphPanelApp().run()
