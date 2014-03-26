from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class CTFGame(Widget):
    pass

class CTFApp(App):
    def build(self):
        layout = GridLayout(cols=4,rows=4)
        for i in xrange(0,16):
            if i is 0:
                layout.add_widget(Image(source='player.jpg'))
            else:
                layout.add_widget(Image(source='grass.jpg'))
        return layout

if __name__ == '__main__':
    CTFApp().run()