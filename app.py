"""
Launches the game
"""

from utils import print_title, print_end
from introduction import Introduction as Intro


def main():
    print_title('The Woods of Darkness', 'slant')
    game = Intro()
    if game:
        print_end('The End', 'slant')


if __name__ == '__main__':
    main()
