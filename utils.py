"""
Set of tools
"""
import time
from pyfiglet import Figlet
from clint.textui import puts, colored


def print_title(title, font):
    """
    prints the story in cli
    :param title: Title of the story
    :param font: font to be used by Figlet
    """
    f = Figlet(font=font)
    puts(colored.red(f.renderText(title)))
    time.sleep(3)


def print_part(text, splitter='\n'):
    """
    splits paragraphs into lines and prints them
    :param text: text chunk to split
    :param splitter: character to use as divider
    """
    for line in text.split(splitter):
        print(line)
        time.sleep(4)
    time.sleep(4)


def print_end(end_message, font):
    """
    prints story's end card in cli
    :param end_message: End title
    :param font: font used in figlet
    """
    f = Figlet(font=font)
    puts(colored.red(f.renderText(end_message)))
