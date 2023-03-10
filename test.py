import kivy
 
from kivy.app import App
 
from kivy.uix.button import Button
 
class ButtonApp(App):
     
    def build(self):
         
        btn = Button(text ="Push Me !")
        return btn
 
root = ButtonApp()
 
root.run()
