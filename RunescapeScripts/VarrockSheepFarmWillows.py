import Common

for x in range(100):
    Common.move_mouse_and_left_click(858, 482, 4, "click left tree")  #time:  1533093943.017743
    Common.move_mouse_and_left_click(1057, 598, 20, "click right tree")  #time:  1533093959.184732
    if x % 2 == 0:
        Common.move_mouse_and_left_click(1726, 767, 20, "click knife") #time: 1533094010.194656
        Common.move_mouse_and_left_click(1823, 753, 2, "click logs") #time: 1533094011.1739223
        Common.move_mouse_and_left_click(59, 970, 1, "click amount of logs to fletch into shafts")
    Common.move_mouse_and_left_click(877, 523, 35, "click in front of left tree")
