from GraphPanel import GraphPanel
from Edge import Edge
from Vertex import Vertex
from Queue import Queue

class BellmanFord():
    
    def findShortestPath(Graph, startNodeIndex, endNodeIndex):
        path = []
        c = True
        nodeInFocus = Graph.getVertex(endNodeIndex)
        Graph.clearHighlights()
        nodeInFocus.highlight()
        for v in Graph.getVertexList():
            v.setBFParentExists(False)
        (Graph.getVertex(startNodeIndex)).setBFDistance(0)
        
        for itNum in Graph.getVertexList():
            for node in Graph.getVertexList():
                if(node.getBFParentExists() == True or node.getID() == startNodeIndex):
                    for e in node.getOutgoingEdges():
                        if((e.getToVertex()).getBFParentExists() == False and node.getID() != startNodeIndex):
                            (e.getToVertex()).setBFParent(e)
                            (e.getToVertex()).setBFDistance(node.getBFDistance()+e.getWeight())
                            (e.getToVertex()).setBFParentExists(True)
                        elif((e.getToVertex()).getBFDistance() > node.getBFDistance()+e.getWeight()):
                            (e.getToVertex()).setBFParent(e)
                            (e.getToVertex()).setBFDistance(node.getBFDistance()+e.getWeight())
        while(c == True):
            edgeInFocus = nodeInFocus.getBFParent()
            nodeInFocus = edgeInFocus.getFromVertex()
            nodeInFocus.highlight()
            path.append(edgeInFocus)
            if(nodeInFocus.getID == startNodeIndex):
                c = False
        path.reverse()
        return path 
        
                        
                    



