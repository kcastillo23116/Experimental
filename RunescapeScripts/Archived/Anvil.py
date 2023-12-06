"""
start at south most bank teller in west varrock bank (last from the top) with camera zoomed out all the way and camera
at north default ban open to smithing tab
Hammer in first slot of inventory and empty inventory
"""
from Skilling import Common

for x in range(1):
    Common.move_mouse_and_right_click(757, 156, 2, "right click bars row one col 3 of smithing tab (tab 5) in bank")
    Common.move_mouse_and_left_click(771, 226, 2, "withdraw inv full of bars")
    Common.move_mouse_and_left_click(1843, 157, 2, "move to anvil")
    Common.move_mouse_and_left_click(1823, 762, 5, "click bar in inv")
    Common.move_mouse_and_left_click(1036, 539, 2, "click anvil")
    Common.move_mouse_and_right_click(940, 404, 2, "right click item to smith") # change this if want to smith something else
    Common.move_mouse_and_left_click(927, 488, 2, "select smith all") # change this if want to smith something else
    Common.move_mouse_and_left_click(1827, 77, 65, "move back to bank teller")
    Common.move_mouse_and_left_click(1036, 511, 5, "click bank teller")
