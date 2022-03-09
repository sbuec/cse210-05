from pyray import Color

class Character:
    '''
    struct
    
    Args:
    - character (str): Text character
    - font_size (int): Text font size
    - color (pr.Color): Text font color
    '''
    
    def __init__(self, character: str, font_size: int, color: Color):
        self.character = character
        self.font_size = font_size
        self.color = color
    
    def __repr__(self) -> str:
        return f'Character("{self.character}","{self.font_size}", "{self.color}")'
    
    def __str__(self) -> str:
        return f'({self.character}, {self.font_size}, {self.color})'