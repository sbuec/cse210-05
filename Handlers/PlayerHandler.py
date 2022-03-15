from Handlers.Handler import Handler
from Actors.Player import Player

class PlayerHandler(Handler):
    '''
    Description: Handles all player actions
    '''

    def __init__(self, keyboardservice) -> None:
        super().__init__()
        self._ks = keyboardservice

    def load(self, name: str, setup_info: list):
        '''
        Description: Creates an instance of a Player

        Args:
        - name (str): The name of an object already in the Handler
        - setup_info (list): player_num (int), dispay_char (Character), window (Window)
        '''
        player = Player(*setup_info)
        self._input[name].insert(0, player)
    
    def draw(self) -> None:
        for player_info in self._input.values():
            player_info[0].draw()
    
    def update(self) -> None:
        '''
        for player_info in self._input.values():
            self._ks.update_direction(player_info[0])
            self._ks.update_player_position(player_info[0])
        '''
        pass