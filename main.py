import pyray as pr
from Actors.Player import Player
from Actors.Tail import Tail
from Structs.Window import Window
from Structs.Texture import Character
from Movement.KeyboardInput import KeyInput

WINDOW = Window(height = 450, width = 800, caption = "Greed", fps_cap = 60)

def main():

    pr.init_window(WINDOW.width, WINDOW.height, WINDOW.caption)
    pr.set_target_fps(WINDOW.fps_cap)

    Tail.set_tail_timer(5)

    player1_char = Character('@', 12, pr.GREEN)
    player2_char = Character('@', 12, pr.GREEN)

    Player1_tail_char = Character('#', 12, pr.BLUE)
    Player2_tail_char = Character('#', 12, pr.RED)
    
    player1 = Player(1, player1_char, WINDOW)
    player2 = Player(2, player2_char, WINDOW)

    player1_tail = Tail(player1, player2, Player1_tail_char, WINDOW)
    player2_tail = Tail(player2, player1, Player2_tail_char, WINDOW)


    while not pr.window_should_close():

        KeyInput.update_direction(player1)
        KeyInput.update_player_position(player1)

        KeyInput.update_direction(player2)
        KeyInput.update_player_position(player2)

        player1_tail.update_tail()
        player2_tail.update_tail()

        p1_collide = player1_tail.player_collision()
        p2_collide = player2_tail.player_collision()

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        player1_tail.draw_tail()
        player2_tail.draw_tail()

        player1.draw()
        player2.draw()

        pr.end_drawing()

        if p1_collide:
            print('p1 collided')

        if p2_collide:
            print('p2 collided')

    pr.close_window()

if __name__ == "__main__":
    main()