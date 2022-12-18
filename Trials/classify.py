from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class classifyWindow(BoxLayout):
    pass

class classifyApp(App):
    def build(self):
        return classifyWindow()

if __name__=="__main__":
    sa = classifyApp()
    sa.run()