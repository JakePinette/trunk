
import sys

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout


#class ToolBar(TabbedPanel):
 #   def build(self):
  #      tabPanel = TabbedPanel()
        
        #creating the tabs
   #     graphTab = TabbedPanelHeader(text='Graph')
    #    graphTab.content = Button(text='Content')
#
 #       nodeTab = TabbedPanelHeader(text='Node')
  #      nodeTab.content = Button(text='Node content')

        
   #     tabPanel.add_widget(nodeTab)
    #    tabPanel.add_widget(graphTab)

     #   return tabPanel

        
class BuildLayout(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='top')

        TopBarHolder = AnchorLayout(anchor_x='left', anchor_y='top',
                                    size_hint=(1, 0.05))
        RemainingHolder = AnchorLayout(anchor_x='left', anchor_y='bottom')
        ToolBarHolder = AnchorLayout(anchor_x='right', andchor_y='bottom')
        
        TopBar = BoxLayout(size_hint=(0.75, 1))
        
        Vis = Button(text='Graph area', size_hint=(0.75, 0.95))
        
        ToolBar = TabbedPanel(size_hint=(0.25, 1))

        btntest = Button(text='topBar')
   
       
        layout.add_widget(TopBarHolder)
        layout.add_widget(RemainingHolder)
        layout.add_widget(ToolBarHolder)
        
        
        
        ToolBarHolder.add_widget(ToolBar)
        TopBarHolder.add_widget(TopBar)
        TopBar.add_widget(btntest)
        RemainingHolder.add_widget(Vis)
        
        return layout

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    app = BuildLayout()
    app.run()
