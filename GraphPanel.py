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
    currentEdge = 0

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
            self.listOfVertices.append(vertex)
            self.add_widget(vertex)
        
    def modifyVertex(self, vertexNo, name):
        pass

    def modifyVertex(self, vertexNo, name, info):
        pass

    def setNamesVisible(self):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameVisible()

    def setNamesInvisible(self):
        for v in range(0, len(self.listOfVertices)):
            self.listOfVertices[v].setNameInvisible()

    def setVertexPosition(self, vertexNo, x, y):
        self.listOfVertices[vertexNo].setInitialPosition(x,y)
        self.listOfVertices[vertexNo].setAlpha(1)

    def addEdge(self, vertexFromIndex, vertexToIndex, weight):
        edge = Edge()
        self.add_widget(edge)
        edge.setVertices(self.listOfVertices[vertexFromIndex], self.listOfVertices[vertexToIndex])
        self.listOfEdges.append(edge)
        self.listOfVertices[vertexFromIndex].addOutgoingEdge(self.currentEdge)
        self.listOfVertices[vertexToIndex].addIncomingEdge(self.currentEdge)
        self.currentEdge = self.currentEdge + 1

    def printVertexEdges(self):
        for v in range(0,len(self.listOfVertices)):
            print("vertex Number")
            print(v)
            print("edges incoming")
            print(self.listOfVertices[v].getIncomingEdgeIndexes())
            print("edges outgoing")
            print(self.listOfVertices[v].getOutgoingEdgeIndexes())
            
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
