"""
exports coordinates on click to  (middle click to stop)
"""
import pyHook
import pythoncom
import time


def onleftclick(event):
    print("Common.move_mouse_and_left_click", event.Position, " time: ", time.time())
    return True


def onrightclick(event):
    print("Common.move_mouse_and_right_click", event.Position, " time: ", time.time())
    return True


# on middle click stop script
def onmidclick(event):
    raise SystemExit(0)
    return True


hm = pyHook.HookManager()
hm.SubscribeMouseLeftDown(onleftclick)
hm.SubscribeMouseRightDown(onrightclick)
hm.SubscribeMouseMiddleDown(onmidclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()
