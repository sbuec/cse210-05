from pyray import Color

class Character:
    '''struct'''
    def __init__(self, character: str, font_size: int, color: Color):
        self.character = character
        self.font_size = font_size
        self.color = color