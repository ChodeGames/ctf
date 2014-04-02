from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color
from kivy.graphics.instructions import Canvas
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.clock import Clock

class Flag(Widget):
    def __init__(self, color ,**kwargs):
        super(Flag, self).__init__(**kwargs)
        self.bind(size=self.update,pos=self.update)
        with self.canvas:
            Color(1,0,0)
            self.flag_pole = Rectangle()
            self.flag = Rectangle()

    def update(self, *largs):
        # Flag pole
        self.flag_pole.size = (self.width/8,self.height)
        self.flag_pole.pos = self.pos
        print self.flag_pole.pos
        # Flag
        self.flag.size = (self.width,self.height/2)
        self.flag.pos = (self.x,self.center_y)
        print self.flag.pos

class CTFGame(Widget):
    def __init__(self, **kwargs):
        super(CTFGame, self).__init__(**kwargs)
        self.grass_texture = Image(source='grass.jpg').texture
        self.player_texture = Image(source='player.jpg').texture
        self.player_position = self.center

        with self.canvas:
            self.board = Rectangle(texture=self.grass_texture,pos=self.pos,size=self.size)
            self.player = Rectangle(texture=self.player_texture,pos=self.player_position,size=(50,50))
            self.red_flag = Flag(color="red",pos=(self.center_x,self.center_y),size=(self.height/5,self.width/5))

        self.bind(size=self.update_size)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def update_size(self, *largs):
        Logger.info("CTFGame: update_size()")
        self.board.size = self.size
        print "red_flag (%s,%s)" % (self.red_flag.x,self.red_flag.y)
        self.red_flag.pos = self.center_x,self.center_y
        print "red_flag (%s,%s)" % (self.red_flag.x,self.red_flag.y)

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
        game = CTFGame()
        # Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    CTFApp().run()