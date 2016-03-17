from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from Edge import Edge
from Vertex import Vertex
from GraphPanel import GraphPanel
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')

class buttontest(Widget):

    graph = ObjectProperty( GraphPanel())

    def attatchGraph(self, graph):
        self.graph = graph

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            print("button hit")
            self.graph.setBackgroundRGB(0.5, 0.5, 0.5)

class testApp(App):
    def build(self):
        btn = buttontest()
        graphPanel = GraphPanel()
        graphPanel.newGraph(4)
        btn.attatchGraph(graphPanel)

        graphPanel.setVertexPosition(0, 100, 100)
        graphPanel.setVertexPosition(1, 200, 200)
        graphPanel.setVertexPosition(2, 300, 100)
        graphPanel.setVertexPosition(3, 200, 300)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        graphPanel.addEdge(2, 1, 6)
        graphPanel.addEdge(1, 3, 7)
        graphPanel.addEdge(0, 3, 8)

        panel = BoxLayout();
        panel.add_widget(graphPanel)
        panel.add_widget(btn)

        return panel

if __name__ == '__main__':
    testApp().run()
