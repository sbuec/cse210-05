from Structs.Texture import Character
from Structs.Window import Window
from Actors.Load import Load

class Actor:
    '''
    Holds Initialization and base functions for Images to Objects
    '''

    def __init__(self, display_char: Character, window: Window) -> None:
        self.display_char = display_char
        self.window = window
        self.Load_texture()

    def Load_texture(self):
        '''Loads in Actor Texture'''
        self.texture = Load.text_to_texture(self.display_char.character, self.display_char.font_size, self.display_char.color)

    def draw(self):
        '''Draws Actor'''
        Load.draw_rectangle(self)