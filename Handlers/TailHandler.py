from Handlers.Handler import Handler
from Actors.Tail import Tail

class TailHandler(Handler):

    def set_tail_timer(time, window_fps):
        '''Sets timer for player tail. Measured in seconds.'''
        Tail.Timer = time * window_fps

    def load(self, name, setup_info):
        '''
        name: dictionary key
        setup_info: attached_player (Player), opponent_player (Player), texture (Texture), window (Window)
        '''
        tail = Tail(*setup_info)
        self._input[name].insert(0, tail)
    
    def draw(self):
        for tail_info in self._input.values():
            tail_info[0].draw_tail()

    def update(self):
        for tail_info in self._input.values():
            tail_info[0].update_tail()