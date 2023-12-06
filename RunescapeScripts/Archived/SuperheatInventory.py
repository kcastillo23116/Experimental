"""
start with air staff equipt inventory ores to smelt and nat runes in first slot and magic tab open
stand directly in front of a grand exchange right top bank teller with camera north default all zoomed out
"""
from Skilling import Common

for x in range(10):
    # super heat inv
    for row in range(1, 5):
        for col in range(1, 5):
            if row == 1 and col == 1 or row == 4 and col == 3 or row == 4 and col == 4:
                continue
            else:
                print("{", row, " ", col, "}")
                Common.move_mouse_and_left_click(1822, 837, 2)
                Common.click_inv_item(row, col)

    # deposit all bars and get more ores in inv from bank and switch back to magic tab
    Common.move_mouse_and_left_click(891, 515, 2, "click bank")
    Common.move_mouse_and_right_click(1781, 761, 2, "right click first bar in inv")
    Common.move_mouse_and_left_click(1785, 834, 2, "click deposit all")
    Common.move_mouse_and_right_click(904, 361, 2, "right click ore in bank")  # change if ore location is different
    Common.move_mouse_and_left_click(889, 436, 2, "click get x amt")  # change if ore location is different
    Common.move_mouse_and_right_click(948, 362, 2, "right click 2nd ore in bank")  # change if ore location is different
    Common.move_mouse_and_left_click(930, 433, 2, "click get x amt")  # change if ore location is different
    Common.move_mouse_and_left_click(1062, 68, 2, "close bank")
    Common.move_mouse_and_left_click(1896, 729, 2, "open spell tab")
