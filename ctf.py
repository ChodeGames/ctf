from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color
from kivy.graphics.instructions import Canvas
from kivy.core.window import Window

class CTFGame(Widget):
    def __init__(self, **kwargs):
        super(CTFGame, self).__init__(**kwargs)
        self.grass_texture = Image(source='grass.jpg').texture
        self.player_texture = Image(source='player.jpg').texture
        self.player_position = self.center

        with self.canvas:
            self.board = Rectangle(texture=self.grass_texture,pos=self.pos,size=self.size)
            self.player = Rectangle(texture=self.player_texture,pos=self.player_position,size=(50,50))
        self.bind(size=self.update_size)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def update_size(self, *largs):
        self.board.size = self.size

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.player_move(x_direction=-1)
        elif keycode[1] == 'right':
            self.player_move(x_direction=1)
        elif keycode[1] == 'up':
            self.player_move(y_direction=1)
        elif keycode[1] == 'down':
            self.player_move(y_direction=-1)
        return True

    def player_move(self,x_direction=0,y_direction=0,step=50):
        x,y = self.player.pos
        if x_direction:
            x += (x_direction * step)
        if y_direction:
            y += (y_direction * step)
        self.player.pos = (x,y)


class CTFApp(App):
    def build(self):
        return CTFGame()

if __name__ == '__main__':
    CTFApp().run()