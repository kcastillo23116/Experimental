"""
exports coordinates on click to  (middle click to stop)
"""
from pynput import mouse
import pyautogui as pyauto
import time

startTime = time.time()


def on_click(x, y, button, pressed):
    if not pressed and button == mouse.Button.left:
        # Declare global variable, so we can update the variable's value in this function
        global startTime

        # calculate time elapsed between clicks and print:
        # function name with coordinates
        # time between clicks in seconds for sleeps
        # Empty quotes for message output
        elapsed = time.time() - startTime
        mouse_coords = pyauto.position();
        x_coordinate = mouse_coords[0]
        y_coordinate = mouse_coords[1]
        print("Common.move_mouse_and_left_click(", x_coordinate, ",", y_coordinate, ",", elapsed, ",",  "\"", "\"", ")")

        # Update start time so we get elapsed time between clicks
        startTime = time.time()


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
