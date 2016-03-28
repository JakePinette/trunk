import Queue
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from GraphPanel import GraphPanel
from Vertex import Vertex
from Edge import Edge
from kivy.lang import Builder

def isTree(graphPanel):
    isTree = False
    root = Vertex()
    count = 0
    for v in graphPanel.getVertexList():
        count = count + len(v.getOutgoingEdgeIndexes())
        if len(v.getIncomingEdgeIndexes()) == 0:
            if isTree == False:
                isTree = True
                root = v
            else:
                return None
    if (count + 1) == len(graphPanel.getVertexList()):
        return root
    else:
        return None

def visualize(graphPanel):
    v = isTree(graphPanel)
    if v == None:
        visualizeArbitrairyGraph(graphPanel)
    else:
        visualizeTree(graphPanel, v)
    return

def visualizeArbitrairyGraph(graph):
    print("Sorry! Arbitrairy graphs not supported yet!")
    return

def visualizeTree(graphPanel, root):
    rows = []
    rows.append([])
    rows[0].append(root)
    q1 = Queue.Queue()
    q2 = Queue.Queue()
    q2.put(root)
    i = 0
    nextRow = False
    while True:
        if i % 2 == 0:
            currentQ = q2
            nextQ = q1
        else:
            currentQ = q1
            nextQ = q2

        if currentQ.empty(): #Parsed the whole tree
            break
        
        i = i + 1
        while currentQ.empty() == False:
            v = currentQ.get()
            for e in v.getOutgoingEdges():
                if nextRow == False:
                    nextRow = True
                    rows.append([])
                    newV = e.getToVertex()
                    rows[i].append(newV)
                    nextQ.put(newV)
                else:
                    newV = e.getToVertex()
                    rows[i].append(newV)
                    nextQ.put(newV)
        nextRow = False

    depth = len(rows)
    maxRow = len(rows[0])
    rad = graphPanel.getDefaultVertexRadius()
    for row in rows:
        if len(row) > maxRow:
            maxRow = len(row)

    height = graphPanel.height
    width = graphPanel.width

    tentativeRad1 = width/(maxRow*3 + 1)
    tentativeRad2 = height/(depth*3 + 1)

    if tentativeRad1 < tentativeRad2:
        tentativeRad = tentativeRad1
    else:
        tentativeRad = tentativeRad2

    if tentativeRad > 25:
        rad = 25
    elif tentativeRad < 10:
        graphPanel.setDefaultVertexRadius(10)
        rad = 10
    else:
        graphPanel.setDefaultVertexRadius(tentativeRad)
        rad = tentativeRad

    pos = graphPanel.pos
    topY = height + pos[1]
    leftX = pos[0]
    xBump = 3*rad
    yBump = 3*rad
    yCur = topY - rad
    xCur = leftX + rad
    
    if (rad*3*depth + rad) < height:
        yBump = height/(depth + 1)
        yCur = topY - yBump

    for row in rows:

        if (rad*3*len(row) + rad) < width:
            xBump = width/(len(row) + 1)
            xCur = + leftX + xBump
        else:
            xCur = ((width - (rad*3*len(row) + rad))/2 + 2*rad) + leftX
            xBump = 3*rad

        for v in row:
            v.setInitialPosition(xCur, yCur)
            xCur = xCur + xBump

        yCur = yCur - yBump
        
    return None

class vizButton(Widget):
    g = ObjectProperty(GraphPanel())
    
    def setGraph(self, graphPanel):
        self.g = graphPanel

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.g.newGraph(12)
            self.g.addEdge(0,1,1)
            self.g.addEdge(0,2,1)
            self.g.addEdge(1,3,1)
            self.g.addEdge(1,4,1)
            self.g.addEdge(2,5,1)
            self.g.addEdge(4,6,1)
            self.g.addEdge(4,7,1)
            self.g.addEdge(4,8,1)
            self.g.addEdge(5,9,1)
            self.g.addEdge(5,10,1)
            self.g.addEdge(7,11,1)
            visualize(self.g)
        
class TreeApp(App):
    def build(self):
        graphPanel = GraphPanel()

        btn = vizButton()
        btn.text = "hit me"
        btn.setGraph(graphPanel)
        GUI = BoxLayout()
        GUI.add_widget(btn)
        GUI.add_widget(graphPanel)
        


        return GUI

if __name__ == '__main__':
    TreeApp().run()
