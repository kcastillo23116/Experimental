"""
Common functions that could be useful in multiple places
"""
import datetime
import time
from random import randrange

import pyautogui
from pathlib import Path
import PIL.ImageGrab
from PIL import ImageGrab, Image, ImageOps
from pytesseract import pytesseract
from win32api import GetSystemMetrics

import Common

# Turn off PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen
# Accidentally triggering when moving out of VM window
pyautogui.FAILSAFE = False

# Regions to be used by  pyautogui functions
All_game_screen_region = None
Main_game_screen_region = None
Bottom_right_game_screen_region = None
Top_half_game_screen_region = None
Bottom_half_game_screen_region = None
Center_game_screen_region = None

Inventory_region = None
Inventory_bar_region = None
Inventory_last_slot_region = None

Minimap_region = None
Minimap_vitals_region = None

Bank_region = None
Bank_bottom_options_region = None

Chatbox_region = None
Chatbox_options_region = None

Status_message_top_left = None

# Images
empty_inventory_images = ['Images/General/EmptyInventory.png']
low_hp_images = ['Images/General/LowHealth.png']


def set_regions():
    """
    Sets game regions based on current main monitor resolutions
    """
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    global All_game_screen_region
    global Main_game_screen_region
    global Bottom_right_game_screen_region
    global Top_half_game_screen_region
    global Bottom_half_game_screen_region
    global Center_game_screen_region

    global Inventory_region
    global Inventory_bar_region
    global Inventory_last_slot_region

    global Minimap_region
    global Minimap_vitals_region

    global Bank_region
    global Bank_bottom_options_region

    global Chatbox_region
    global Chatbox_options_region

    global Status_message_top_left

    # Set regions for 3K or 4K laptop resolution if neither resolution is set raise an error
    # Use RegionFinder.py script to get these
    if width == 3000:
        All_game_screen_region = (9, 47, 2926, 1882)
        Bottom_right_game_screen_region = (1354, 1048, 1048, 788)
        Top_half_game_screen_region = (3, 41, 2932, 1078)
        Bottom_half_game_screen_region = (5, 591, 2418, 1341)
        Center_game_screen_region = (765, 589, 1303, 840)

        Inventory_region = (2262, 1079, 671, 758)
        Inventory_bar_region = (1812, 1833, 1131, 99)

        Minimap_region = (2363, 74, 570, 418)
        Minimap_vitals_region = (2336, 107, 330, 420)

        Bank_region = (564, 241, 1193, 1140)
        Bank_bottom_options_region = (557, 1392, 1263, 101)

        Chatbox_region = (12, 1522, 1343, 412)
        Chatbox_options_region = (4, 1862, 1361, 73)
    elif width == 3840:
        All_game_screen_region = (8, 43, 3774, 2038)
        Main_game_screen_region = (4, 90, 3234, 1893)  # Without minimap, inventory and space between them and menu bar
        Bottom_right_game_screen_region = (1403, 1235, 1846, 754)
        Top_half_game_screen_region = (3, 38, 3244, 1574)
        Bottom_half_game_screen_region = (5, 812, 3775, 1267)
        Center_game_screen_region = (765, 589, 1303, 840)

        Inventory_region = (3190, 1230, 586, 756)
        Inventory_bar_region = (2651, 1994, 1133, 92)
        Inventory_last_slot_region = (3644, 1872, 85, 90)

        Minimap_region = (3353, 86, 424, 416)
        Minimap_vitals_region = (3200, 139, 283, 357)

        Bank_region = (987, 248, 1188, 1280)
        Bank_bottom_options_region = (985, 1528, 1263, 120)

        Chatbox_region = (7, 1671, 1347, 355)
        Chatbox_options_region = (6, 2016, 1357, 68)

        Status_message_top_left = (19, 92, 326, 133)
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


# click item in inventory based on row and column
# NOTE: top left is 0, 0
# NOTE: Row is Y-axis and Column is X-axis
def click_inv_item(row, col, time_after_click=0.0):
    # coordinates of top left item to use as starting point
    first_item_x = 3352
    first_item_y = 1347

    # X coordinate of second item to calculate distance between items in x-axis
    second_item_x = 3462

    # Y coordinate of fifth item to calculate distance between items in y-axis
    fifth_item_y = 1442

    # distance between row/col in pixels
    row_dist = fifth_item_y - first_item_y
    col_dist = second_item_x - first_item_x

    # calculate where to move mouse to by adding the distance between rows/columns multiplied by row/col index
    xcoord = first_item_x + (col_dist * col)
    ycoord = first_item_y + (row_dist * row)

    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.click()

    time.sleep(time_after_click)


def click_whole_inv_items(time_after_click=0.0):
    for row in range(0, 7):
        for col in range(0, 4):
            click_inv_item(row, col, time_after_click)


def drop_inventory(time_after_click=0.4):
    pyautogui.keyDown('shift')
    click_whole_inv_items(time_after_click)
    pyautogui.keyUp('shift')


def move_mouse_and_left_click(xcoord, ycoord, timebeforeclick=0, message=""):
    sleep_with_countdown(timebeforeclick)
    print(message)
    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.click()


# Move mouse and click withing specified region
# Use values from RegionFinder.py
def move_mouse_and_click_in_region(xcoord, ycoord, width, height, time_before_click=0, right_click=False, message=""):
    sleep_with_countdown(time_before_click)
    print(message)

    x_range_start = xcoord
    x_range_end = xcoord + width
    y_range_start = ycoord
    y_range_end = ycoord + height

    # Generate random x and y coordinates within specified region
    x = randrange(x_range_start, x_range_end)
    y = randrange(y_range_start, y_range_end)

    pyautogui.moveTo(x, y)

    if right_click:
        pyautogui.rightClick()
    else:
        pyautogui.click()


def move_mouse_and_right_click(xcoord, ycoord, timebeforeclick=0, message=""):
    sleep_with_countdown(timebeforeclick)
    print(message)
    pyautogui.moveTo(xcoord, ycoord)
    pyautogui.rightClick()


def watch_click_image(image_paths, confidence=0.7, message='', right_click=False,
                      sleep_time_after_click=0, attempts=10, next_step_image_paths=None,
                      current_step_region=All_game_screen_region, next_step_region=All_game_screen_region,
                      next_step_confidence=0.7, current_step_grayscale=False, next_step_grayscale=False,
                      double_click=False):
    """
    Click specified image on screen as soon as it's found
    Keep watching till next step is found or timeout after specified attempt count
    Returns true if image was clicked and false otherwise
    Optional time after click sets seconds to sleep after each click
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
                is_next_step_image_on_screen is False:
            image_was_clicked = click_image_helper(image_paths, confidence, current_step_region,
                                                   sleep_time_after_click, right_click,
                                                   current_step_grayscale, double_click)
            # Check for next step image if one is provided
            if next_step_image_paths is not None:
                is_next_step_image_on_screen = is_image_on_screen(next_step_image_paths, next_step_confidence, 0, "",
                                                                  next_step_region, next_step_grayscale)
            # Next step is visible no need to keep looking
            if is_next_step_image_on_screen:
                break
            # If image not found after all attempts raise error to avoid clicking in undesired places
            # Take screenshot and show it, so we can see what might've gone wrong
            elif count == attempts:
                im = PIL.ImageGrab.grab()
                im.show()
                raise ValueError('\t No image found for ', image_paths)

            count += 1

        return image_was_clicked
    except ValueError as val_error:
        raise val_error


def click_image_helper(image_paths, confidence, current_step_region, time_between_clicks=0, right_click=False,
                       grayscale=False, double_click=False):
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
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence, region=current_step_region,
                                                     grayscale=grayscale)

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

            if double_click:
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


def is_image_on_screen(image_paths, confidence=0.7, time_before_check=0, message='', region=All_game_screen_region,
                       grayscale=False):
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
        coordinates = pyautogui.locateCenterOnScreen(path, confidence=confidence, region=region, grayscale=grayscale)

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


def is_hp_low():
    ret = is_image_on_screen(low_hp_images, 0.9, 0, 'Check if HP is low', Minimap_vitals_region)

    return ret


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
    return runtime


# Drop all specified items from inventory
def drop_inventory_items(items_to_drop_images, grayscale=False):
    pyautogui.keyDown('shift')

    # Keep dropping items till they're no longer seen in inventory
    while is_image_on_screen(items_to_drop_images, 0.7, 0, 'Looking for items to drop',
                             Inventory_region):
        watch_click_image(items_to_drop_images, 0.7,
                          'Shift Click drop iron and gems in inventory',
                          False, 0, 10, None,
                          Inventory_region, current_step_grayscale=grayscale)
    pyautogui.keyUp('shift')


def open_inventory(expected_item_image_paths):
    inventory_tab_images = ['Images/Common/InventoryTab.png']

    Common.watch_click_image(inventory_tab_images, 0.7,
                             'Click inventory tab while looking for expected item',
                             False, 1, 10,
                             current_step_region=Common.Inventory_bar_region,
                             next_step_image_paths=expected_item_image_paths,
                             next_step_region=Common.Inventory_region,
                             next_step_confidence=0.7)


def open_spellbook(expected_spell_image_paths):
    inventory_tab_images = ['Images/Common/Spellbook.png']

    Common.watch_click_image(inventory_tab_images, 0.7,
                             'Click spellbook while looking for expected spell',
                             False, 1, 10,
                             current_step_region=Common.Inventory_bar_region,
                             next_step_image_paths=expected_spell_image_paths,
                             next_step_region=Common.Inventory_region,
                             next_step_confidence=0.7)



# WARNING: Doesn't read numbers correctly consistently
# Reads HP from Runelite mini bars plugin and returns current HP number
# Note: Make sure that region for bounding box does not contain any white or lighter colors
#       since it can mess up reading the white numbers. Use debug code below to check
# Note: Runelite Mini Bars plugin with setup:
#   - Show health: enabled
#   - Health Size: 78 x 1
#   - Total Labels: disabled
#   - Health color: black, #00000
def read_hp():
    # Path of tesseract executable
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # Bottom left HP bar coordinates x1, y1, x2, y2
    hp_bounding_box = (1192, 1844, 1299, 1916)

    # ImageGrab-To capture the screen image
    hp_image = ImageGrab.grab(bbox=hp_bounding_box)

    # Grey scale and contrast image to make easier to identify numbers
    hp_image_greyscale = ImageOps.grayscale(hp_image)
    hp_image_greyscale_contrast = ImageOps.autocontrast(hp_image_greyscale, cutoff=3, ignore=1)

    # DEBUG
    # hp_image_greyscale_contrast.show()

    # Set up page segmentation to 11 for Sparse Text, white list for only digits and
    # OCR Engine mode 3 for default OCR Engine
    config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789'

    # Run twice in case there's a misread
    hp_text = (pytesseract.image_to_string(hp_image_greyscale_contrast, config=config))

    return hp_text


def get_hp():
    max_hp = 64

    # Run twice in case there's a misread
    hp_text1 = read_hp()
    hp_text2 = read_hp()

    # If hp is read the same twice and not blank convert it to integer value and return
    # otherwise try one more time and assume max hp
    if hp_text1 == hp_text2:
        if hp_text1 != '':
            hp = int(hp_text1)
            return hp
        else:
            return max_hp
    else:
        hp_text1 = read_hp()
        hp_text2 = read_hp()
        if hp_text1 == hp_text2:
            if hp_text1 != '':
                hp = int(hp_text1)
                return hp
            else:
                return max_hp

