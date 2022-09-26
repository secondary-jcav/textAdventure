from clint.textui import prompt
from Text import chapterOne as chapter
from utils import print_part


class ChapterOne:

    def __init__(self):
        self.example = True

    def scene_a(self):
        print_part(chapter.part_A1)
        choice = prompt.options('Choose 1 or 2', chapter.A1_options)
        if choice == 1:
            print('Chose 1')
        elif choice == 2:
            print('Chose 2')

