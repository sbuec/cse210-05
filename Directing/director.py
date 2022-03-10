import pyray as pr

class Director:
    def __init__(self, keyboardservice, videoservice):
        self._ks = keyboardservice
        self._vs = videoservice

    
    def start_game(self, p1, t1, p2, t2, players, tails):
        #self._vs.open_window()
        while self._vs.is_window_open():
            self.check_collision(t1, t2)
            self.update_movement(players, tails)
            self.display_output(players, tails)
        self._vs.close_window()


    def check_collision(self, t1, t2):
        # collision detection (True = Hit, False = No Hit)
        p1_collide = t1.player_collision()
        p2_collide = t2.player_collision()
        if p1_collide:
            print('p1 collided')
        if p2_collide:
            print('p2 collided')


    def display_output(self, players, tails):
        # Clears screen and starts drawing
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        
        # draw onscreen
        tails.draw()
        players.draw()

        # Ends current frame
        pr.end_drawing()

    def update_movement(self, players, tails):
        # movement updates
        #players.update()
        #tails.update()
        pass


    '''
  


    pr.close_window()
'''