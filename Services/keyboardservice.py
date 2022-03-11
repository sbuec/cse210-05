'''
Keyboard service provides will receive input from players
and manipulate/return values appropriately

Player one moves using the W, S, A and D keys
Player two moves using the I, K, J and L keys
'''

import pyray as pr

class KeyboardService:

    # Sets up key assignments
    def receive_input(self):
        dx = 0
        dy = 0

        # Payer 1 x direction
        if pr.is_key_down(pr.KEY_A):
            dx = -1

        if pr.is_key_down(pr.KEY_D):
            pass

        # Player 1 y direction
        if pr.is_key_down(pr.KEY_W):
            pass

        if pr.is_key_down(pr.KEY_S):
            pass
        

        # Player 2 x direction
        if pr.is_key_down(pr.KEY_J):
            pass

        if pr.is_key_down(pr.KEY_L):
            pass
        
        # Player 2 y direction
        if pr.is_key_down(pr.KEY_L):
            pass

        if pr.is_key_down(pr.KEY_I):
            pass



    # Changes character's direction when specific keys are pressed
    def update_direction(player_info):
        self._player_info = player_info
        #player_info[0]
    
    def update_player_position(player_info):
        pass