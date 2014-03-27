from kivy.logger import Logger
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from random import random
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
import pprint

gameboardrows = 5
gameboardcols = 6
gameboardarray = []

class GameBoardSpace(Widget):
	def __init__(self, row=0, col=0, **kwargs):
		super(GameBoardSpace, self).__init__(**kwargs)
		self.row = row
		self.col = col
		with self.canvas:
			'''
			# add your instruction for main canvas here
			color = (random(), random(), random())
			Color(*color)
			Rectangle(size=self.size)
			'''
			Color(.5, .5, .5)
			Rectangle(pos=self.pos, size=self.size)
			Color(1, 1, 1)
			cx = self.center_x - self.size[0] / 2.
			cy = self.center_y - self.size[1] / 2.
			Rectangle(pos=(cx, cy), size=self.size)
		with self.canvas.before:
			# you can use this to add instructions rendered before
			pass
		with self.canvas.after:
			# you can use this to add instructions rendered after
			pass
	
	def on_touch_down(self, touch):
		with self.canvas:
			# add your instruction for main canvas here
			Color(1, 1, 1, .5, mode='rgba')
			Rectangle(pos=self.pos, size=self.size)
		return True


class CTFApp(App):
	def build(self):
		gameboard = GridLayout(rows=gameboardrows, cols=gameboardcols, spacing=[1,1])
		for row in range(gameboardrows):
			gameboardarray.append([])
			for col in range(gameboardcols):
				space = GameBoardSpace(row=row, col=col)
				with space.canvas.before:
					Color(rgba=(1,0,0,0))
				gameboardarray[row].append(space)
				gameboard.add_widget(space)
				print "Added new GameBoardSpace"
		pprint.pprint(gameboardarray)
		return gameboard

if __name__ == '__main__':
	CTFApp().run()
