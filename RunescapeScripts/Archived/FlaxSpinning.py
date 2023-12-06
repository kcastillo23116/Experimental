"""
start at top of lumbridge castle with full inventory of flax and more flax in row 8 col 2 of bank
at third teller from the left with camera zommed out all the way and camera at north default
"""
import Common

for x in range(25):
    Common.move_mouse_and_left_click(717, 991, 2, "move closer to stairs")  #time:  1532916720.1801012
    Common.move_mouse_and_left_click(849, 1000, 4, "click on stairs")  #time:  1532916724.1832943
    Common.move_mouse_and_left_click(1738, 772, 2, "click top left flax in inventory")  #time:  1532916734.4144297
    Common.move_mouse_and_left_click(1145, 337, 2, "use flax on spinning wheel")  #time:  1532916735.6453571
    Common.move_mouse_and_left_click(251, 986, 4, "click the make button at bottom left")  #time:  1532916736.9923828
    Common.move_mouse_and_left_click(631, 914, 60, "click on stairs")  #time:  1532916789.2496238
    Common.move_mouse_and_left_click(298, 937, 5, "click go up menu item")  #time:  1532916794.224347
    Common.move_mouse_and_left_click(1854, 71, 6, "click mini map to move into bank")  #time:  1532916798.2728307
    Common.move_mouse_and_left_click(970, 343, 6, "click bank teller")  #time:  1532916803.9209704
    Common.move_mouse_and_left_click(1015, 819, 6, "dump all items in bank")  #time:  1532916807.2347581
    Common.move_mouse_and_right_click(709, 402, 6, " get full stack of flax from bank (row 8 col 2)")
    Common.move_mouse_and_left_click  (736, 470, 3, "click the withdraw X amount context menu item") #time:  1532916811.7635884