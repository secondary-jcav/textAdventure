from clint.textui import prompt


class StoryHandler:
    def __init__(self):
        pass

    @staticmethod
    def start_chapter(chapter):
        """

        :param chapter:
        :return:
        """
        print(chapter.start)

    @staticmethod
    def choice_prompt(chapter, part="", part_choices=""):
        choice = prompt.options('Choose 1 or 2', chapter.start_options)
        if choice == '1':
            print(chapter.part_A)
        else:
            pass



