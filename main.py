import sys
from contoller.game_controller import GameController


def main():
    game_controller = GameController()
    game_controller.start()


if __name__ == '__main__':
    sys.exit(main())

