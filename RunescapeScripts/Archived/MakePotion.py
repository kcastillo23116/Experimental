from Skilling import Common

# start by withdrawing from bank in this order/amt: 9 herbs, 9 non-herb ingredients, 9 vials of water
for x in range(75):
    Common.move_mouse_and_left_click(1736, 760, 2, "click herb in inv row 1 col 1")  # time:  1533194241.8055615
    Common.move_mouse_and_left_click(1821, 909, 1, "click vial of water in inv row 5 col 3")  # time:  1533194242.9495502
    Common.move_mouse_and_left_click(288, 962, 2, "click the make all button")   # time:  1533194244.9877594
    Common.move_mouse_and_left_click(1777, 849, 8, "click the non-herb ingredient in inv row 3 col 2")  # time:  1533194251.6725729
    Common.move_mouse_and_left_click(1734, 840, 2, "click the unfinished potion in inv row 5 col 3")  # time:  1533194252.3385282
    Common.move_mouse_and_left_click(256, 963, 1, "click the make all button")   # time:  1533194253.7885673
    Common.move_mouse_and_left_click(910, 510, 15, "click the bank")   # time:  1533194267.8530343
    Common.move_mouse_and_left_click(1022, 827, 2, "dump inv into bank")  # time:  1533194272.0688334
    Common.move_mouse_and_right_click(656, 149, 2, "right click the herb in herblore bank tab row 1 col 1")  # time:  1533194275.760182
    Common.move_mouse_and_left_click(658, 221, 1, "withdraw 9 herbs")   # time:  1533194281.0017793
    Common.move_mouse_and_right_click(707, 147, 1, "right click the non-herb ingredient in herblore bank tab row 1 col 2")  # time:  1533194281.7701294
    Common.move_mouse_and_left_click(699, 216, 1, "withdraw 9 non-herb ingredients")   # time:  1533194282.5778341
    Common.move_mouse_and_right_click(748, 142, 1, "right click the vials of water in herblore bank tab row 1 col 3")  # time:  1533194283.282879
    Common.move_mouse_and_left_click(724, 217, 1, "withdraw 9 vials of water")   # time:  1533194284.0583737
    Common.move_mouse_and_left_click(1065, 68, 1, "close bank")   # time:  1533194287.4439895
