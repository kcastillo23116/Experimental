import pyHook
import pythoncom

import win32api, ctypes, time


def left_click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

class Mouse:
    """It simulates the mouse"""
    MOUSEEVENTF_MOVE = 0x0001 # mouse move
    MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
    MOUSEEVENTF_LEFTUP = 0x0004 # left button up
    MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down
    MOUSEEVENTF_RIGHTUP = 0x0010 # right button up
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
    MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up
    MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled
    MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
    SM_CXSCREEN = 0
    SM_CYSCREEN = 1

    def _do_event(self, flags, x_pos, y_pos, data, extra_info):
        """generate a mouse event"""
        x_calc_temp = 65536 * x_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CXSCREEN) + 1
        y_calc__temp = 65536 * y_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CYSCREEN) + 1
        x_calc = int(x_calc_temp)
        y_calc = int(y_calc__temp)
        return ctypes.windll.user32.mouse_event(flags, x_calc, y_calc, data, extra_info)

    def _get_button_value(self, button_name, button_up=False):
        """convert the name of the button into the corresponding value"""
        buttons = 0
        if button_name.find("right") >= 0:
            buttons = self.MOUSEEVENTF_RIGHTDOWN
        if button_name.find("left") >= 0:
            buttons = buttons + self.MOUSEEVENTF_LEFTDOWN
        if button_name.find("middle") >= 0:
            buttons = buttons + self.MOUSEEVENTF_MIDDLEDOWN
        if button_up:
            buttons = buttons << 1
        return buttons

    def move_mouse(self, pos):
        """move the mouse to the specified coordinates"""
        (x, y) = pos
        old_pos = self.get_position()
        x =  x if (x != -1) else old_pos[0]
        y =  y if (y != -1) else old_pos[1]
        self._do_event(self.MOUSEEVENTF_MOVE + self.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

    def press_button(self, pos=(-1, -1), button_name="left", button_up=False):
        """push a button of the mouse"""
        self.move_mouse(pos)
        self._do_event(self.get_button_value(button_name, button_up), 0, 0, 0, 0)

    def click(self, pos=(-1, -1), button_name= "left"):
        """Click at the specified placed"""
        self.move_mouse(pos)
        self._do_event(self._get_button_value(button_name, False)+self._get_button_value(button_name, True), 0, 0, 0, 0)

    # def double_click (self, pos=(-1, -1), button_name="left"):
    #     """Double click at the specifed placed"""
    #     for i in xrange(2):
    #         self.click(pos, button_name)

    def get_position(self):
        """get mouse position"""
        return win32api.GetCursorPos()


def OnKeyboardEvent(event):

    # halbard switch
    if event.Key == 'P':
        print("P hit")

        mouse = Mouse()
        mouse.click((1030, 360), "left")
        time.sleep(1.0)
        mouse.click((1268, 262), "left")
        time.sleep(1)
        mouse.click((1268, 262), "left")
        time.sleep(1)
        mouse.click((1268, 262), "left")
        time.sleep(1)

        # PressKey(0x01)
        # time.sleep(2)
        # ReleaseKey(0x01)
        # left_click(1030, 360)
        # time.sleep(1)
        # left_click(1268, 262)
        # time.sleep(1)
        # pyautogui.press('down')
        # pyautogui.press('enter')
        # pyautogui.press('right')
        # pyautogui.press('right')
        # pyautogui.press('right')
        # pyautogui.press('right')
        # pyautogui.press('down', 1, 0, None, True)
        # pyautogui.press('down', 1, 0, None, True)

        # pyautogui.press('down', 1, 0, None, True)

        # startingpos = pyautogui.position()
        # Common.move_mouse_and_left_click(1030, 360, 1)
        # Common.move_mouse_and_left_click(1268, 262, 1)
        # Common.move_mouse_and_left_click(1268, 262, 1)
        # Common.move_mouse_and_left_click(1268, 262, 1)
        # # pyautogui.click()
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(1269, 349, 1)
        # Common.move_mouse_and_left_click(967, 867, 1)
        # Common.move_mouse_and_left_click(956, 503, 1)
        # Common.move_mouse_and_left_click(1738, 763, 1)
        # Common.move_mouse_and_left_click(1701, 728, 1)
        # Common.move_mouse_and_left_click(1847, 805, 1)
        # Common.move_mouse_and_left_click(1798, 729, 1)
        # pyautogui.moveTo(startingpos)

    # dagger switch
    # if event.Key == 'W':
    #     print("W hit")
    #     startingpos = pyautogui.position()
    #     Common.move_mouse_and_left_click(1738, 763)
    #     Common.move_mouse_and_left_click(1701, 728)
    #     Common.move_mouse_and_left_click(1766, 813)
    #     Common.move_mouse_and_left_click(1798, 729)
    #     pyautogui.moveTo(startingpos)

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
