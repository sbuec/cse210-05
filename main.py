import pyray as pr
from Handlers.TailHandler import TailHandler
from Structs.Window import Window
from Structs.Texture import Character
from Handlers.PlayerHandler import PlayerHandler

from Services.keyboardservice import KeyboardService
from Services.videoservice import VideoService
from Directing.director import Director



FONT_SIZE = 12
WIDTH = 800
HEIGHT = 450
CAPTION = "Cycle"
FPS = 60

WINDOW = Window(HEIGHT, WIDTH, CAPTION, FPS)


def main():
    # Create video service and keyboard service instances
    vs = VideoService(WIDTH, HEIGHT, CAPTION, FPS)
    ks = KeyboardService()

    # Open the window
    vs.open_window()


    # player setup
    players = PlayerHandler(ks)
    player_char = Character('@', FONT_SIZE, pr.GREEN)
    p1 = players.add('p1', [1, player_char, WINDOW])
    p2 = players.add('p2', [2, player_char, WINDOW])

    # tail setup
    tails = TailHandler()
    TailHandler.set_tail_timer(3, WINDOW.fps_cap)
    t1 = tails.add('t1', [p1, p2, Character('#', FONT_SIZE, pr.BLUE), WINDOW])
    t2 = tails.add('t2', [p2, p1, Character('#', FONT_SIZE, pr.RED), WINDOW])


    # Start the game
    director = Director(ks, vs)
    director.start_game(p1, t1, p2, t2, players, tails)

if __name__ == "__main__":
    main()
