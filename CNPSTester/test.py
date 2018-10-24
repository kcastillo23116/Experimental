# TODO:
# 1 change so click coord exporter gives you wait/sleep times instead of raw times
# 2 look into figuring out how to tell if error dialog popped up
#   use ImageGrabber.py to do this (look for red pixels in certain area) (if error: pause, notify and dump screenshot)
# 3 change so script is read from txt file (refer to FuzzTester code)
# 4 Make it so script starts at workspace selection screen so no login credentials needed (IA issue with storing creds)
# notes:
#   CNPS Starts at bot left monitor or main monitor

import Common

Common.move_mouse_and_left_click (1001, 1642, 1)
Common.move_mouse_and_left_click (1334, 1614, 1)
Common.move_mouse_and_left_click (1700, 1326, 1)
Common.move_mouse_and_left_click (1944, 1116, 1)
Common.move_mouse_and_left_click (1875, 941, 1)
Common.move_mouse_and_left_click (1511, 736, 1)
Common.move_mouse_and_left_click (1148, 584, 1)
Common.move_mouse_and_left_click (2609, 121, 1)