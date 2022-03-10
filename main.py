import pyray as pr
from Handlers.TailHandler import TailHandler
from Structs.Window import Window
from Structs.Texture import Character
from Handlers.PlayerHandler import PlayerHandler

WINDOW = Window(height = 450, width = 800, caption = "Greed", fps_cap = 60)

FONT_SIZE = 12

def main():

    pr.init_window(*WINDOW.pr_window_setup())
    pr.set_target_fps(WINDOW.fps_cap)

    # player setup
    players = PlayerHandler()
    player_char = Character('@', FONT_SIZE, pr.GREEN)
    p1 = players.add('p1', [1, player_char, WINDOW])
    p2 = players.add('p2', [2, player_char, WINDOW])

    # tail setup
    tails = TailHandler()
    TailHandler.set_tail_timer(3, WINDOW.fps_cap)
    t1 = tails.add('t1', [p1, p2, Character('#', FONT_SIZE, pr.BLUE), WINDOW])
    t2 = tails.add('t2', [p2, p1, Character('#', FONT_SIZE, pr.RED), WINDOW])


    while not pr.window_should_close():

        # collision detection (True = Hit, False = No Hit)
        p1_collide = t1.player_collision()
        p2_collide = t2.player_collision()

        # movement updates
        # players.update()
        tails.update()

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # draw onscreen
        tails.draw()
        players.draw()

        pr.end_drawing()

        if p1_collide:
            print('p1 collided')
        if p2_collide:
            print('p2 collided')

    pr.close_window()

if __name__ == "__main__":
    main()
