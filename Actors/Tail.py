from Actors.Player import Player
from Actors.Actor import Actor
from Actors.Collision import Collision
from Actors.Segments import Segment
from pyray import Texture
from Structs.Window import Window
from Actors.Load import Load

class Tail(Actor):
    '''
    Class for Tail Segments of Player
    
    Timer (int): The amount of time a tail piece stays on screen in seconds
    '''

    Timer = 0

    def __init__(self, attached_player: Player, opponent_player: Player, texture: Texture, window: Window) -> None:
        super().__init__(texture, window)
        self._attached_player = attached_player
        self._opponent = opponent_player
        self.set_up()
    
    def set_up(self):
        self._segments = []
        self._segments.append(self._attached_player)

    def set_tail_timer(timer):
        Tail.Timer = timer

    def update_tail(self):
        self.tail_collision()
        self.update_tail_timer()
    
    def tail_collision(self):
        '''Checks for collision between last placed tail and possible new tail'''
        pos_x = self._attached_player.pos_x
        pos_y = self._attached_player.pos_y
        width = self._attached_player.texture.width
        height = self._attached_player.texture.height

        new_segment = Tail.create_new_tail(pos_x, pos_y, width, height, self.texture)

        if self._segments.index(self._segments[-1]) != 0:
            if not Collision.tail_collide_check(self._segments[-1], new_segment):
                self._segments.append(new_segment)
        else:
            self._segments.append(new_segment)

    def player_collision(self) -> bool:
        '''Checks for collision of opponent and attached player tail'''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                if Collision.player_collide_check( segment, self._opponent):
                    return True
        return False
    
    def create_new_tail(pos_x, pos_y, width, height, texture):
        '''Creates new tail segment'''
        timer = Tail.Timer * 60
        return Segment(pos_x, pos_y, width, height, texture, timer)
    
    def update_tail_timer(self):
        '''updates segments on screen timer'''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                segment.update_timer()
                if segment.screen_time == 0:
                    self._segments.remove(segment)

    def draw_tail(self):
        '''Draws tail'''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                Load.draw_rectangle(segment)