
import sys

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from GraphPanel import GraphPanel
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

class ColorPopup(App):
    
	
	
    def build(self):
        clrpkr =  ColorPicker()
        #this is the popup window
        popupp = Popup(title='Choose your color', content=clrpkr,size_hint=(None, None), size=(400, 400))
       
        #this is the layout for the popup to be in
        TopBar = BoxLayout()


        btnDisplay = Button(text='Display')
        btnDisplay.bind(on_press=popupp.open)
        TopBar.add_widget(btnDisplay)
        

        return TopBar
    #this is the method that will change the color when the color is picked
    def on_color(ColorPicker, GraphPanel, bkgrndBln):
        r = ColorPicker.r
        b = ColorPicker.b
        g = ColorPicker.g 
        if bkgrndBln == true :
            GraphPanel.setBackgroundRGB(GraphPanel, r,g,b)
        else:
            GraphPanel.setAllVertexRGB(GraphPanel, r, g, b)
		

    


if __name__ == "__main__":
    app = ColorPopup()
    app.run()
