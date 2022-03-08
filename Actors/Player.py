from Actors.Actor import Actor
from Structs.Window import Window
from Structs.Texture import Character


class Player(Actor):
	'''Class for players'''


	def __init__(self, player_num: int, dispay_char: Character, window: Window) -> None:
		super().__init__(dispay_char, window)
		self.player_num = player_num
		self.direction = '-y' # This is the player start direction
		self.set_position()

	def set_position(self) -> None:
		''' Sets start position of player '''
		if self.player_num == 1:
			self.pos_x = self.window.width//3 - self.texture.width
			self.pos_y = self.window.height//2 - self.texture.height

		elif self.player_num == 2:
			self.pos_x = (self.window.width//3 * 2) - self.texture.width
			self.pos_y = self.window.height//2 - self.texture.height