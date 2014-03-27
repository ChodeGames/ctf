from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color
from kivy.graphics.instructions import Canvas

class CTFGame(Widget):
    def __init__(self, **kwargs):
        super(CTFGame, self).__init__(**kwargs)
        self.grass_texture = Image(source='grass.jpg').texture
        self.player_texture = Image(source='player.jpg').texture

        with self.canvas:
            self.board = Rectangle(texture=self.grass_texture,pos=self.pos,size=self.size)
            self.player = Rectangle(texture=self.player_texture,pos=self.center,size=(50,50))
        self.bind(size=self.update_size)

    def update_size(self, *largs):
        self.board.size = self.size

    def player_move(self):
        pass


class CTFApp(App):
    def build(self):
        return CTFGame()

if __name__ == '__main__':
    CTFApp().run()