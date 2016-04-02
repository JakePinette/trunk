
import sys

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
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

class ColorButton(Widget):

    graph = ObjectProperty( GraphPanel())
    popupp = ObjectProperty( Popup())
    clrpkr = ObjectProperty(ColorPicker())
    box = ObjectProperty(BoxLayout())
    button = ObjectProperty(Button())

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.popupp.open()
    
    def initialize(self, graph):
        self.graph = graph
        self.box = BoxLayout(orientation='vertical', size_hint=(1,1))
        self.clrpkr = ColorPicker(size_hint=(1,0.9)) 
        self.button = Button(text='Done', size_hint=(1,0.1))
        self.button.bind(on_press=self.close)
        self.box.add_widget(self.clrpkr)
        self.box.add_widget(self.button)
        self.popupp = Popup(title='Choose your color', content=self.box,size_hint=(None, None), size=(400, 450))
    
    def on_color(self):
        listColor = self.clrpkr.color
        r = listColor[0]
        g = listColor[1]
        b = listColor[2]
        self.graph.setBackgroundRGB(r,g,b)

    def close(self, touch):
        self.on_color()
        self.popupp.dismiss()


class testApp(App):
    def build(self):
        content = BoxLayout()
        colorP = ColorButton()
        graphPanel = GraphPanel()
    
        graphPanel.newGraph(4)
        graphPanel.setVertexPosition(0, 500, 100)
        graphPanel.setVertexPosition(1, 600, 200)
        graphPanel.setVertexPosition(2, 700, 100)
        graphPanel.setVertexPosition(3, 600, 300)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        graphPanel.addEdge(1, 0 ,2)
        graphPanel.addEdge(0, 3, 8)

        colorP.initialize(graphPanel)

        content.add_widget(colorP)
        content.add_widget(graphPanel)

        return content

if __name__ == "__main__":
    app = testApp()
    app.run()
