"""
Common functions that could be useful in multiple places
"""
import datetime
import time
import os
import pyautogui
from pathlib import Path

# sleep timer that displays countdown in console
def sleep_with_countdown(amt_time):
    for it in range(amt_time):
        print('Sleep: ', it+1, '/', amt_time)
        time.sleep(1)

# click item in inventory based on row and column (top left is 1, 1)
def click_inv_item(row, col):
    # distance between row/col in pixels
    row_dist = 35
    col_dist = 40

    # coordinates of top left item to use as starting point
    top_left_item_x = 1733
    top_left_item_y = 770

    # calculate where to move mouse to by adding the distance between rows/columns multiplied by row/col index - 1
    # subtracting 1 so it's not zero based grid (so top left point won't be 0,0)
    xcoord = top_left_item_x + (col_dist * (col - 1))
    ycoord = top_left_item_y + (row_dist * (row - 1))

    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.click()


def move_mouse_and_left_click(xcoord, ycoord, timebeforeclick=0, message=""):
    sleep_with_countdown(timebeforeclick)
    print(message)
    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.click()


def move_mouse_and_right_click(xcoord, ycoord, timebeforeclick=0, message=""):
    sleep_with_countdown(timebeforeclick)
    print(message)
    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.rightClick()


def click_image(image_path, confidence=0.7,
                time_before_click=0, message='', right_click=False):
    """
    Click on specified PNG image with specified confidence, if is right click,
    Note: Image path is relative to Common.py file
    sleep before click and console message
    """
    sleep_with_countdown(time_before_click)
    print(message)

    # Get and Install Pillow and opencv-python packages to get this call to work
    # If the file is not a png file it will not work
    path = get_relative_file_path(image_path)
    coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence)

    # If image not found raise error to avoid clicking in undesired places
    if coordinates is None:
        raise ValueError('No image found for ', image_path)

    pyautogui.moveTo(coordinates)
    if right_click:
        pyautogui.rightClick()
    else:
        pyautogui.click()


def get_relative_file_path(path):
    """Get path relative to project file"""
    base_path = Path(__file__).parent

    # Resolve relative path and convert to posix for forward slashes
    # Backslashes caused files to not be found in pyautogui calls
    return (base_path / path).resolve().as_posix()


def print_runtime(total_loops, loop_runtime, current_loop):
    """
    Prints estimated runtime based on loop counts and loop runtime
    """
    print("Loop: ", current_loop, "/", total_loops)
    runtime = ((total_loops - current_loop) * loop_runtime)
    dtg = str(datetime.timedelta(seconds=runtime))
    print("Approx time till done: ", dtg)