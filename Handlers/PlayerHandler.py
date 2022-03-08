from Handlers.Handler import Handler
from Actors.Player import Player
from Movement.KeyboardInput import KeyInput

class PlayerHandler(Handler):

    def load(self, name, setup_info):
        '''
        name: dictionary key
        setup_info: player_num (int), dispay_char (Character), window (Window)
        '''
        player = Player(*setup_info)
        self._input[name].insert(0, player)
    
    def draw(self) -> None:
        for player_info in self._input.values():
            player_info[0].draw()
    
    def update(self) -> None:
        for player_info in self._input.values():
            KeyInput.update_direction(player_info[0])
            KeyInput.update_player_position(player_info[0])