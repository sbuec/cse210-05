class Segment:
    '''Class for the Segments in Each Player's Tail'''

    def __init__(self, pos_x, pos_y, width, height, texture, screen_time) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen_time = screen_time
        self.texture = texture

    def update_timer(self) -> None:
        '''Updates segment "on screen time" timer'''
        self.screen_time -= 1