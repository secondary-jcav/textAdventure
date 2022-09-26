from clint.textui import prompt
from Text import introText as chapter
from utils import print_part
from chapterOne import ChapterOne as ch1


class Introduction:

    def __init__(self):
        self.next_part = ch1()
        self.scene_start()



    def scene_start(self):
        print_part(chapter.start)
        choice = prompt.options('Choose 1 or 2', chapter.start_options)
        if choice == '1':
            self.scene_a()
        elif choice == '2':
            self.scene_b()

    def scene_a(self):
        print_part(chapter.part_A)
        choice = prompt.options('Choose 1, 2 or 3', chapter.A_options)
        if choice == '1':
            self.scene_c()
        elif choice == '2':
            self.scene_d()
        elif choice == '3':
            self.scene_e()

    def scene_b(self):
        print_part(chapter.part_B)
        choice = prompt.options('Choose 1, 2 or 3', chapter.B_options)
        if choice == '1':
            self.scene_c()
        elif choice == '2':
            self.scene_d()
        elif choice == '3':
            self.scene_e()

    def scene_c(self):
        print_part(chapter.part_C)
        choice = prompt.options('Choose 1 or 2', chapter.C_options)
        if choice == '1':
            self.scene_f()
        elif choice == '2':
            self.scene_g()


    def scene_d(self):
        print_part(chapter.part_D)
        print('\n\n')
        self.next_part.scene_a()
        return True

    @staticmethod
    def scene_e():
        print_part(chapter.part_E)
        print('\n\n')
        return True

    @staticmethod
    def scene_f():
        print_part(chapter.part_F)
        print('\n\n')
        return True

    @staticmethod
    def scene_g():
        print_part(chapter.part_G)
        print('\n\n')
        return True
