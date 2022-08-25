"""
Common functions that could be useful in multiple places
"""
import datetime
import time
import os
import pyautogui
from pathlib import Path
import PIL.ImageGrab


# sleep timer that displays countdown in console
def sleep_with_countdown(amt_time):
    for it in range(amt_time):
        print('Sleep: ', it + 1, '/', amt_time)
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


def watch_click_image(image_paths, confidence=0.7, message='', right_click=False,
                      time_between_clicks=0, attempts=10, next_step_image_paths=None):
    """
    Click specified image on screen as soon as it's found
    Keep watching till it's found or timeout after specified attempt count
    Optional time between clicks and next step images to look for
    """
    print(message)

    # If next step images provided check if next step is on screen and keep trying current step till next step is
    # visible then return when next step is visible
    # Else no next step images provided just find the image we're looking for, so it can be clicked
    if next_step_image_paths is not None:
        count = 0

        # If next step is not on screen keep trying current step and checking for next step
        while is_image_on_screen(next_step_image_paths, 0.9, 1) \
                is False and count < attempts:
            # Keep looking for image till found or timeout count is reached
            # Go through list and try all current step images
            for image in image_paths:
                print('Looking for', image)
                path = get_relative_file_path(image)
                coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence)
                if coordinates is not None:
                    break

            # If image is found move mouse and click it
            if coordinates is not None:
                # Click on image coordinates
                pyautogui.moveTo(coordinates)
                if right_click:
                    pyautogui.rightClick()
                else:
                    pyautogui.click()
                sleep_with_countdown(time_between_clicks)

            count += 1

            # If images not found raise error to avoid clicking in undesired places
            # Take screenshot and show it so we can see what might've gone wrong
            if coordinates is None and count == attempts:
                im = PIL.ImageGrab.grab()
                im.show()
                raise ValueError('No image found for ', image_paths)

        return
    else:
        # Keep looking for image till found or timeout count is reached
        count = 0
        coordinates = None
        while coordinates is None and count < attempts:
            # Go through list and try all images
            for image in image_paths:
                print('Looking for', image)
                path = get_relative_file_path(image)
                coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence)
                if coordinates is not None:
                    break

            # If image is found move mouse and click it
            if coordinates is not None:
                # Click on image coordinates
                pyautogui.moveTo(coordinates)
                if right_click:
                    pyautogui.rightClick()
                else:
                    pyautogui.click()
                sleep_with_countdown(time_between_clicks)

            count += 1

        # If image not found raise error to avoid clicking in undesired places
        # Take screenshot and show it so we can see what might've gone wrong
        if coordinates is None and count == attempts:
            im = PIL.ImageGrab.grab()
            im.show()
            raise ValueError('No image found for ', image_paths)


def click_image(image_paths, confidence=0.7,
                time_before_click=0, message='', right_click=False):
    """
    Click on specified list of PNG images with specified confidence, if is right click,
    Note: Image path is relative to Common.py file
    sleep before click and console message
    If multiple images provided tries them all and stops if finds a match
    """
    sleep_with_countdown(time_before_click)
    print(message)

    coordinates = None

    # Go through list and try all images
    for image in image_paths:
        # Get and Install Pillow and opencv-python packages to get this call to work
        # If the file is not a png file it will not work
        path = get_relative_file_path(image)
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence)

        # If image not found raise error to avoid clicking in undesired places
        # Else coordinate found break to stop loop since target found
        if coordinates is None:
            print('No image found for ', image, 'trying next image')
        else:
            break

    # If image not found raise error to avoid clicking in undesired places
    # Take screenshot and show it so we can see what might've gone wrong
    if coordinates is None:
        im = PIL.ImageGrab.grab()
        im.show()
        raise ValueError('No image found for ', image_paths)

    # Click on image coordinates
    pyautogui.moveTo(coordinates)
    if right_click:
        pyautogui.rightClick()
    else:
        pyautogui.click()


def is_image_on_screen(image_paths, confidence=0.7, time_before_check=0, message=''):
    """
    Look for specified list of PNG images with specified confidence return true if found false otherwise
    Note: Image path is relative to Common.py file
    sleep before click and console message
    If multiple images provided tries them all and stops if finds a match
    """
    sleep_with_countdown(time_before_check)
    print('Are', image_paths, 'on the screen?')

    coordinates = None

    # Go through list and try all images
    for image in image_paths:
        # Get and Install Pillow and opencv-python packages to get this call to work
        # If the file is not a png file it will not work
        path = get_relative_file_path(image)
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence)

        # If image not found print and check next image
        # Else if image is found stop loop
        if coordinates is None:
            print(image, 'NOT on screen')
        else:
            print(image, 'on screen')
            break

    if coordinates is None:
        return False
    else:
        return True


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
