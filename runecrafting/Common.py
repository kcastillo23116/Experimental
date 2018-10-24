"""
Common functions that could be useful in multiple places
"""
import time
import os
import pyautogui


# sleep timer that displays countdown in console
def sleep_with_countdown(amt_time):
    for it in range(amt_time):
        os.system("cls")
        print(it)
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

# for row in range(1, 8):
#     for col in range(1, 5):
#         print("{", row, " ", col, "}")
#         click_inv_item(row, col)
#         time.sleep(1)
#         # sleep_with_countdown(1)
#         # pyautogui.click()

