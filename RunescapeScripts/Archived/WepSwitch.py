"""
Switch between weapons on hotkey presses
"""
from Skilling import Common
import pyHook
import pythoncom
import pyautogui


def OnKeyboardEvent(event):
    # halbard switch
    if event.Key == 'Q':
        print("Q hit")
        startingpos = pyautogui.position()
        Common.move_mouse_and_left_click(1738, 763)
        Common.move_mouse_and_left_click(1701, 728)
        Common.move_mouse_and_left_click(1847, 805)
        Common.move_mouse_and_left_click(1798, 729)
        pyautogui.moveTo(startingpos)

    # dagger switch
    if event.Key == 'W':
        print("W hit")
        startingpos = pyautogui.position()
        Common.move_mouse_and_left_click(1738, 763)
        Common.move_mouse_and_left_click(1701, 728)
        Common.move_mouse_and_left_click(1766, 813)
        Common.move_mouse_and_left_click(1798, 729)
        pyautogui.moveTo(startingpos)

    # stop script
    if event.Key == 'Escape':
        raise SystemExit(0)

    return True


# When the user presses a key down anywhere on their system
# the hook manager will call OnKeyboardEvent function.
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# hm.SubscribeKeyDown()

# Here we register the same function to the KeyUp event.
# Probably in practice you will create a different function to handle KeyUp functionality
# hm.KeyUp = OnKeyboardEqvent
hm.HookKeyboard()
pythoncom.PumpMessages()
hm.UnhookKeyboard()
