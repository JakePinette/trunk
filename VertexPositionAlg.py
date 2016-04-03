import Queue
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from GraphPanel import GraphPanel
import Edge
from Vertex import Vertex

import random

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
    if len(graphPanel.listOfVertices) < 1:
        return
    v = isTree(graphPanel)
    if v == None:
        visualizeArbitraryGraph(graphPanel)
    else:
        visualizeTree(graphPanel, v)
    return

def visualizeArbitraryGraph(graph):
    width = graph.width
    height = graph.height
    
    #Determine appropriate radius
    vertexCount = len(graph.listOfVertices)
    rad = ((width*height)/(9.0*vertexCount))**(0.5)
    if rad < 10:
        rad = 10
    if rad > 25:
        rad = 25
    graph.setDefaultVertexRadius(rad)

    initialDimension = math.ceil(vertexCount**(0.5))
    xpos = graph.pos[0]
    ypos = graph.pos[1]
    xmid = xpos + width/2
    ymid = ypos + height/2

    #put all the vertices in a grid to start out
    nextX = xmid - (initialDimension/2.0)*3*rad + 1.5*rad
    nextY = ymid + (initialDimension/2.0)*3*rad - 1.5*rad
    
    for x in range(0, vertexCount):
        if x > 0 and x % initialDimension == 0:
            nextY = nextY - 3*rad
            nextX = xmid - (initialDimension/2)*3*rad + 1.5*rad
        graph.listOfVertices[x].setInitialPosition(nextX, nextY)
        nextX = nextX + 3*rad
        
    #Iterate a number of times, each time moving each vertex.  Vertices
    #get pulled by edges, and pushed away by vertices if too close.
        
    for x in range(0,5):
        factor = 1-(0.2*x)
        for v in range(0, len(graph.listOfVertices)):
            vertex = graph.listOfVertices[v]
            centerX = vertex.center_x
            centerY = vertex.center_y
            pullX = 0
            pullY = 0

            #"Edge pull" first:
            for e in vertex.getIncomingEdges():
                vFrom = e.getFromVertex()
                pullX = pullX + (vFrom.getX()-centerX)/4
                pullY = pullY + (vFrom.getY()-centerY)/4
            for e in vertex.getOutgoingEdges():
                vTo = e.getToVertex()
                pullX = pullX + (vTo.getX()-centerX)/4
                pullY = pullY + (vTo.getY()-centerY)/4
            pullX = pullX*factor
            pullY = pullY*factor

            #Set maximum displacement per itteration
            if pullX > (width*factor)/2:
                pullX = (width*factor)/2
            if pullX < -(width*factor)/2:
                pullX = -(width*factor)/2
            if pullY > (height*factor)/2:
                pullY = (height*factor)/2
            if pullY < -(height*factor)/2:
                pullY = -(height*factor)/2

            #Now apply the "pull"
            vertex.setPosition(centerX + pullX, centerY + pullY)
            
            #Now "vertex push". Nested for loops for yummy yummy complexity.
        
            pushX = 0
            pushY = 0
            for newV in range(0, len(graph.listOfVertices)):
                if v == newV:
                    continue
                newVertex = graph.listOfVertices[newV]
                centerX = vertex.getX()
                centerY = vertex.getY()
                newX = newVertex.getX()
                newY = newVertex.getY()
                
                if ((newX-centerX)**2 + (newY-centerY)**2)**(0.5) > (3*rad):
                    continue

                if newX == centerX and newY == centerY:
                    #Bump one vertex a little so they are not on top of each other.
                    if v+newV % 4 == 0:
                        newX = newX + 1
                        newY = newY + 1
                    elif v+newV % 4 == 1:
                        newX = newX + 1
                        newY = newY - 1
                    elif v+newV % 4 == 2:
                        newX = newX - 1
                        newY = newY + 1
                    else:
                        newX = newX - 1
                        newY = newY - 1

                #We now have a vertex within 3rad away from our vertex.
                #This is close enough to qualify for a "push"
                
                distance = ((newX-centerX)**2 + (newY-centerY)**2)**(0.5)
                hyp = (3*rad - distance)

                tentX = 0
                tentY = 0

                if centerX == newX: #Vertical
                    if newY > centerY:
                        pushY = pushY - hyp
                    else:
                        pushY = pushY + hyp
    
                elif centerY == newY: #Horizontal
                    if newX > centerX:
                        pushX = pushX - hyp
                    else:
                        pushX = pushX + hyp
                        
                else: #General
                    slope = (centerY - newY)/(centerX - newX)
                    tentX = ((hyp)**2/(1+(slope)**2))**(0.5)
                    tentY = slope*x
                    
                    if newX > centerX:
                        pushX = pushX - tentX
                    else:
                        pushX = pushX + tentX

                    if newY > centerY:
                        pushY = pushY - tentY
                    else:
                        pushY = pushY + tentY
            if pushX > 3*rad:
                pushX = 3*rad
            if pushX < -3*rad:
                pushX = -3*rad
            if pushY > 3*rad:
                pushY = 3*rad
            if pushY < -3*rad:
                pushY = -3*rad
            
            pushY = pushY
            pushX = pushX
            vertex.setPosition(centerX + pushX, centerY + pushY)

    #Bump vertices a little after we're done by repeating the vertex push.
    #This is to ensure no vertices are on top of each other
    for i in range(0,2):
        for v in range(0,len(graph.listOfVertices)):
            vertex = graph.listOfVertices[v]
            pushX = 0
            pushY = 0
            for newV in range(0, len(graph.listOfVertices)):
                if v == newV:
                    continue
                newVertex = graph.listOfVertices[newV]
                centerX = vertex.getX()
                centerY = vertex.getY()
                newX = newVertex.getX()
                newY = newVertex.getY()
                
                if ((newX-centerX)**2 + (newY-centerY)**2)**(0.5) > (3*rad):
                    continue

                if newX == centerX and newY == centerY:
                    #Bump one vertex a little so they are not on top of each other.
                    if v+newV % 4 == 0:
                        newX = newX + 1
                        newY = newY + 1
                    elif v+newV % 4 == 1:
                        newX = newX + 1
                        newY = newY - 1
                    elif v+newV % 4 == 2:
                        newX = newX - 1
                        newY = newY + 1
                    else:
                        newX = newX - 1
                        newY = newY - 1

                #We now have a vertex within 3rad away from our vertex.
                #This is close enough to qualify for a "push"
                
                distance = ((newX-centerX)**2 + (newY-centerY)**2)**(0.5)
                hyp = (3*rad - distance)

                tentX = 0
                tentY = 0

                if centerX == newX: #Vertical
                    if newY > centerY:
                        pushY = pushY - hyp
                    else:
                        pushY = pushY + hyp
    
                elif centerY == newY: #Horizontal
                    if newX > centerX:
                        pushX = pushX - hyp
                    else:
                        pushX = pushX + hyp
                        
                else: #General
                    slope = (centerY - newY)/(centerX - newX)
                    tentX = ((hyp)**2/(1+(slope)**2))**(0.5)
                    tentY = slope*x
                    
                    if newX > centerX:
                        pushX = pushX - tentX
                    else:
                        pushX = pushX + tentX

                    if newY > centerY:
                        pushY = pushY - tentY
                    else:
                        pushY = pushY + tentY
            if pushX > 3*rad:
                pushX = 3*rad
            if pushX < -3*rad:
                pushX = -3*rad
            if pushY > 3*rad:
                pushY = 3*rad
            if pushY < -3*rad:
                pushY = -3*rad
            
            pushY = pushY/2
            pushX = pushX/2
            vertex.setPosition(centerX + pushX, centerY + pushY)
        
    #Rescale
    yMax = graph.listOfVertices[v].center_y
    yMin = graph.listOfVertices[v].center_y
    xMax = graph.listOfVertices[v].center_x
    xMin = graph.listOfVertices[v].center_x
    for v in range(0, len(graph.listOfVertices)):
        x = graph.listOfVertices[v].center_x
        y = graph.listOfVertices[v].center_y 
        if x > xMax:
            xMax = x
        if x < xMin:
            xMin = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y

    deltaX = xMax - xMin
    deltaY = yMax - yMin
    xScale = ((deltaY/(deltaX+0.0))/(height/(0.0+width)))
    yScale = 1/xScale
    
    if xScale > yScale:
        for v in range(0, len(graph.listOfVertices)):
            x = graph.listOfVertices[v].center_x
            y = graph.listOfVertices[v].center_y
            graph.listOfVertices[v].setPosition(xScale*x,y)
    else:
        for v in range(0, len(graph.listOfVertices)):
            x = graph.listOfVertices[v].center_x
            y = graph.listOfVertices[v].center_y
            graph.listOfVertices[v].setPosition(x,yScale*y)
    #Center
    xAvg = 0
    yAvg = 0
    for v in range(0, len(graph.listOfVertices)):
        xAvg = xAvg + graph.listOfVertices[v].center_x
        yAvg = yAvg + graph.listOfVertices[v].center_y
    xAvg = xAvg/len(graph.listOfVertices)
    yAvg = yAvg/len(graph.listOfVertices)
    xBump = xmid - xAvg
    yBump = ymid - yAvg
    for v in range(0, len(graph.listOfVertices)):
        x = graph.listOfVertices[v].center_x
        y = graph.listOfVertices[v].center_y
        graph.listOfVertices[v].setPosition(x+xBump,y+yBump)

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
            self.g.newGraph(300)
            self.g.setNamesVisible()

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
