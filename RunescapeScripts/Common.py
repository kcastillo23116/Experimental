"""
Common functions that could be useful in multiple places
"""
import datetime
import time
import os
import pyautogui
from pathlib import Path
import PIL.ImageGrab
from win32api import GetSystemMetrics

# Regions to be used by  pyautogui functions
All_game_screen_region = None
Bottom_right_game_screen_region = None

Minimap_region = None
Inventory_region = None
Bank_region = None
Bank_bottom_options_region = None

Chatbox_region = None


def set_regions():
    """
    Sets game regions based on current main monitor resolutions
    """
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    global All_game_screen_region
    global Bottom_right_game_screen_region

    global Minimap_region
    global Inventory_region
    global Bank_region
    global Bank_bottom_options_region

    global Chatbox_region


    # Set regions for 3K or 4K laptop resolution if neither resolution is set raise an error
    if width == 3000:
        All_game_screen_region = (9, 47, 2926, 1882)
        Bottom_right_game_screen_region = (1354, 1048, 1048, 788)

        Minimap_region = (2363, 74, 570, 418)
        Inventory_region = (2432, 1145, 499, 690)

        Bank_region = (564, 241, 1193, 1140)
        Bank_bottom_options_region = (985, 1528, 1263, 120)

        Chatbox_region = (16, 1666, 1333, 356)
    elif width == 3840:
        All_game_screen_region = (8, 43, 3774, 2038)
        Bottom_right_game_screen_region = (1403, 1235, 1846, 754)

        Minimap_region = (3353, 86, 424, 416)
        Inventory_region = (3259, 1288, 514, 692)

        Bank_region = (987, 248, 1188, 1280)
        Bank_bottom_options_region = (985, 1528, 1263, 120)

        Chatbox_region = (16, 1666, 1333, 356)
    else:
        raise ValueError('\t Unsupported resolution unable to set regions correctly ', width, height)


try:
    set_regions()
except ValueError as error:
    raise error


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
                      time_between_clicks=0, attempts=10, next_step_image_paths=None,
                      current_step_region=All_game_screen_region, next_step_region=All_game_screen_region,
                      next_step_confidence=0.7):
    """
    Click specified image on screen as soon as it's found
    Keep watching till next step is found or timeout after specified attempt count
    Optional time between clicks and next step images to look for
    Optional region parameters that default to whole game screen
    """
    print(message)

    try:
        count = 0
        image_was_clicked = False

        # If next step images not provided set to True since we don't care if it's on the screen
        if next_step_image_paths is None:
            is_next_step_image_on_screen = True
        else:
            is_next_step_image_on_screen = False

        # Look for and click specified image
        # If image was not already clicked or next step image is not on screen and max attempts not reached
        while image_was_clicked is False or \
                is_next_step_image_on_screen is False \
                and count < attempts:
            image_was_clicked = click_image_helper(image_paths, confidence, current_step_region,
                                                   time_between_clicks, right_click)
            # Check for next step image if one is provided
            if next_step_image_paths is not None:
                is_next_step_image_on_screen = is_image_on_screen(next_step_image_paths, next_step_confidence, 0, "",
                                                                  next_step_region)
            # Next step is visible no need to keep looking
            if is_next_step_image_on_screen:
                break
            # Break if at max attempts
            if count > attempts:
                break

            count += 1

        # If image not found after all attempts raise error to avoid clicking in undesired places
        # Take screenshot and show it, so we can see what might've gone wrong
        if count == attempts:
            im = PIL.ImageGrab.grab()
            im.show()
            raise ValueError('\t No image found for ', image_paths)

        return

    except ValueError as val_error:
        raise val_error


def click_image_helper(image_paths, confidence, current_step_region, time_between_clicks=0, right_click=False):
    """
    Updated click image helper function to be used by the watch_click_image function above
    Click specified image on screen as soon as it's found
    Optional timeout after specified attempt count
    Optional time between clicks and next step images to look for
    Optional region parameters that default to whole game screen
    """

    coordinates = None

    # Go through list and try all images
    for image in image_paths:
        print('\t Looking for', image)
        path = get_relative_file_path(image)
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence, region=current_step_region)

        # if coordinates found break loop no need to look at rest of images
        if coordinates is not None:
            break

    # If image is found move mouse and click it and return True
    # Else return false to let know we didn't find anything to click
    if coordinates is not None:
        # Click on image coordinates
        print('\t\tClicking on', image_paths)
        pyautogui.moveTo(coordinates)
        if right_click:
            pyautogui.rightClick()
            sleep_with_countdown(time_between_clicks)
            return True
        else:
            pyautogui.click()
            sleep_with_countdown(time_between_clicks)
            return True
    else:
        return False


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
    # Take screenshot and show it, so we can see what might've gone wrong
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


def is_image_on_screen(image_paths, confidence=0.7, time_before_check=0, message='', region=All_game_screen_region):
    """
    Look for specified list of PNG images with specified confidence return true if found false otherwise
    Note: Image path is relative to Common.py file
    sleep before click and console message
    If multiple images provided tries them all and stops if finds a match
    Optional region parameter that defaults to whole game screen
    """
    coordinates = None
    sleep_with_countdown(time_before_check)

    # Go through list and try all images
    for image in image_paths:
        # Get and Install Pillow and opencv-python packages to get this call to work
        # If the file is not a png file it will not work
        path = get_relative_file_path(image)
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence, region=region)

        # If image not found print and check next image
        # Else if image is found stop loop
        if coordinates is None:
            print(image, '\t NOT on screen')
        else:
            print(image, '\t on screen')
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


def print_runtime(total_loops, loop_runtime_seconds, current_loop):
    """
    Prints estimated runtime based on loop counts and loop runtime
    """
    print("Loop: ", current_loop, "/", total_loops)
    runtime = ((total_loops - current_loop) * loop_runtime_seconds)
    dtg = str(datetime.timedelta(seconds=runtime))
    print("Approx time till done: ", dtg)
