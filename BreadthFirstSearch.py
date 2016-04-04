
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from GraphPanel import GraphPanel
from InfoPanel import InfoPanel
import Queue
from VertexPositionAlg import visualize


#the class containg the depth first search algorithm


    #root is a vertex, and depth is an integer
def bfs(root, depth, graphPanel):
	graphPanel.clearHighlights()
	q = Queue.Queue()
	q.put(root)
		
	root.highlight()
	added = []
	for x in range(0, len(graphPanel.listOfVertices)):
                added.append(False)

        for x in range(0, depth+1):
                nodes = []
                while q.empty() == False:
                        nodes.append(q.get())
                for x in nodes:
                        x.highlight()
                        for e in x.getOutgoingEdges():
                                newV = e.getToVertex()
                                ID = newV.getID()
                                if added[ID] == False:
                                        added[ID] = True
                                        q.put(newV)
class testButton(Button):
	g = ObjectProperty(GraphPanel())
	
	def setGraph(self, graph):
		self.g = graph
		self.text = "hit me"
		
	def on_touch_down(self, touch):
		if self.collide_point(touch.x, touch.y):
			vertex = self.g.listOfVertices[9]
			visualize(self.g)
			bfs(vertex,3, self.g)
	
class testApp(App):
	def build(self):
		layout = BoxLayout()
		btn = testButton()

		graph = GraphPanel()
		graph.loadGraph("treeExample.txt")
		graph.setNamesVisible()
		btn.setGraph(graph)
		layout.add_widget(graph)
		layout.add_widget(btn)
		return layout
		
if __name__ == "__main__":
	testApp().run()
