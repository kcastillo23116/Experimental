from Skilling import Common

for x in range(85):
    Common.move_mouse_and_left_click (1774, 761, 2)  #time:  1533023776.4740582
    Common.move_mouse_and_left_click (1821, 764, 1)  #time:  1533023777.1862652
    Common.move_mouse_and_left_click (231, 935, 1)  #time:  1533023778.4372737
    Common.move_mouse_and_left_click(891, 515, 40, "click bank")
    Common.move_mouse_and_right_click(855, 181, 2, "right bolt material in bank (row 2 col 5)")  # change if ore location is different
    Common.move_mouse_and_left_click(826, 279, 2, "click get x amt")  # change if ore location is different
    Common.move_mouse_and_left_click(1062, 68, 2, "close bank")
