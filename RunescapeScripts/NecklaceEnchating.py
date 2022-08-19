"""
start with air staff equipt inventory full of jade necklaces and cosmic runes in first slot and magic tab open
stand directly in front of a bank teller
"""
import Common
import time
import  pyautogui

for row in range(1, 8):
    for col in range(1, 5):
        if row == 1 and col == 1:
            continue
        else:
            print("{", row, " ", col, "}")
            Common.move_mouse_and_left_click(1772, 818, 2)
            Common.click_inv_item(row, col)
