from GraphPanel import GraphPanel
from Edge import Edge
from Vertex import Vertex

class BellmanFord():
    
    def findShortestPath(self, Graph, startNodeIndex, endNodeIndex):
        path = []
        c = True
        numVert = len(Graph.listOfVertices)

        if startNodeIndex < 0 or startNodeIndex >= numVert:
            return False
        if endNodeIndex < 0 or endNodeIndex >= numVert:
            return False
        
        nodeInFocus = Graph.getVertex(endNodeIndex)
        Graph.clearHighlights()
        nodeInFocus.highlight()
        globalTraversalCost = 0
        for v in Graph.getVertexList():
            v.setBFParentExists(False)
            v.setBFDistance(float("inf"))
        (Graph.getVertex(startNodeIndex)).setBFDistance(0)
        
        for itNum in Graph.getVertexList():
            for node in Graph.getVertexList():
                if(node.getBFParentExists() == True or node.getID() == startNodeIndex):
                    for e in node.getOutgoingEdges():
                        if((e.getToVertex()).getBFParentExists() == False) :
                            (e.getToVertex()).setBFParent(e)
                            (e.getToVertex()).setBFDistance(node.getBFDistance() + e.getWeight())
                            (e.getToVertex()).setBFParentExists(True) 
                        elif((e.getToVertex()).getBFDistance() > node.getBFDistance()+e.getWeight()):
                            (e.getToVertex()).setBFParent(e)
                            (e.getToVertex()).setBFDistance(node.getBFDistance()+e.getWeight())
        while(c == True):
            nodeInFocus.highlight()
            if nodeInFocus.getID() == startNodeIndex:
                break
            if nodeInFocus.getBFParent() == None:
                return []
            edgeInFocus = nodeInFocus.getBFParent()
            
            nodeInFocus = edgeInFocus.getFromVertex()
            path.append(edgeInFocus)
            globalTraversalCost = globalTraversalCost+1
            if(globalTraversalCost >= len(Graph.getVertexList())):
               return False
            if(nodeInFocus.getID == startNodeIndex):
                c = False
        path.reverse()
        return path
        
                        
                    



