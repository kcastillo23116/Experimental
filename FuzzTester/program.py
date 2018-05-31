"""
Open text file with fuzzy testing script and dump to a textbox then press enter after each line
sql injection, long text, bad formatted text, only numbers, only symbols, only text, etc.
"""
import pyautogui
import re


def focus_window(window_name):
    """
    Get window and move it to front

   Args:
        window_name (str): Name of the window i.e. Untitled - Notepad
    """
    window = pyautogui.getWindow(window_name)
    window.set_foreground()


def write(words="", keypress=""):
    """
    Write what you want in window

   Args:
        words (str): Words to write (optional)
        keypress (str): Key presses that come after written words (optional)
    """
    pyautogui.typewrite(words)
    pyautogui.press(keypress)


# TODO: need to learn how to read/use regex
# 'with' keyword is like the 'using' keyword in C#
# open file, read and follow script
# first line is window to bring to front and following lines are what to write to that window
# first word is text input, second word is keypress
with open("test.txt") as file:
    focus_window(file.readline().strip('\n'))
    for line in file:
        inputs = re.split(r'"([^"]*)"', line)
        write(inputs[1], inputs[2].strip('\n').strip(' '))
