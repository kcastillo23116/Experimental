"""
How to start:
location:           at east varrock bank, directly in front of the fourth bank teller box from the left with bag slot open
                    with compass in default north position zoomed all the way out and hold up arrow key till max tilt
equip items:        earth tiara and binding necklace (make note of how many charges binding necklace has, for loop)
items in inventory: water talisman in first slot, stack of water runes in second slot, inventory full of rune essence
items in bank: rune essence (bank: row 7, column 2), water talisman (bank: row 7 column 3),
"""
import pyautogui
import Common


for x in range(16):

    Common.sleep_with_countdown(2)
    print("move to front of range")
    pyautogui.moveTo(1491, 419)
    pyautogui.click()

    Common.sleep_with_countdown(9)
    print("click on item to be cooked in inventory (first slot in inventory)")
    pyautogui.moveTo(1737, 767)
    pyautogui.click()

    Common.sleep_with_countdown(2)
    print("click on range to cook")
    pyautogui.moveTo(982, 462)
    pyautogui.click()

    Common.sleep_with_countdown(3)
    print("click on cook quantity menu item to start cooking")
    pyautogui.moveTo(262, 963)
    pyautogui.click()

    Common.sleep_with_countdown(65)
    print("click on middle bank teller (fourth from the left)")
    pyautogui.moveTo(370, 583)
    pyautogui.click()

    Common.sleep_with_countdown(10)
    print("dump inventory into bank")
    pyautogui.moveTo(1023, 829)
    pyautogui.click()

    Common.sleep_with_countdown(2)
    print("right click cooking item to retrieved from bank (row 11, column 1)")
    pyautogui.moveTo(662, 535)
    pyautogui.rightClick()

    Common.sleep_with_countdown(2)
    print("get full inventory of item")
    pyautogui.moveTo(644, 638)
    pyautogui.click()

