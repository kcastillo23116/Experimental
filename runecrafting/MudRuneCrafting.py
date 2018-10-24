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

# TODO: port sleep_with_countdown to this script
# TODO: test walking to make sure all good
# TODO: create loop and set iteration count to how many charges binding necklace has
# TODO: put moves to locations into functions
# TODO: add randomization to click location and timings
# TODO: make it so mouse moves to location instead of snapping (use the pyautogui.moveRel() function)
# TODO: consider creating some functions for common things like clicking item in bank row/column or edges of minimap/screen

for x in range(16):

    # on way to portal
    Common.sleep_with_countdown(15)
    print("start way to portal")
    pyautogui.moveTo(1876, 74)
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("keep going to portal 1")
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("keep going to portal 2")
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("keep going to portal 3")
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("keep going to portal 4")
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("keep going to portal 5")
    pyautogui.moveTo(963, 172)
    pyautogui.click()

    # click the portal to enter
    Common.sleep_with_countdown(17)
    print("enter portal")
    pyautogui.moveTo(1066, 155)
    pyautogui.click()

    # move closer to runecrafting stone
    Common.sleep_with_countdown(13)
    print("move closer to runecrafting stone")
    pyautogui.moveTo(1007, 248)
    pyautogui.click()

    # click on talisman in inventory (first slot in inventory)
    Common.sleep_with_countdown(18)
    print("click on talisman in inventory (first slot in inventory)")
    pyautogui.moveTo(1737, 767)
    pyautogui.click()

    # right click the altar
    Common.sleep_with_countdown(2)
    print("right click the altar")
    pyautogui.moveTo(964, 176)
    pyautogui.rightClick()

    # click the use talisman on altar context menu item
    Common.sleep_with_countdown(2)
    print("click the use talisman on altar context menu item")
    pyautogui.moveTo(967, 205)
    pyautogui.click()

    # move down to see exit portal
    Common.sleep_with_countdown(10)
    print("move down to see exit portal")
    pyautogui.moveTo(966, 863)
    pyautogui.click()

    # click exit portal
    Common.sleep_with_countdown(6)
    print("click exit portal")
    pyautogui.moveTo(793, 880)
    pyautogui.click()

    # start moving back toward bank
    Common.sleep_with_countdown(8)
    print("start moving back toward bank")
    pyautogui.moveTo(1795, 160)
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("move toward bank 1")
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("move toward bank 2")
    pyautogui.moveTo(1822, 177)
    pyautogui.click()

    Common.sleep_with_countdown(15)
    print("move toward bank 3")
    pyautogui.moveTo(1770, 135)
    pyautogui.click()

    # at this point player has arrived at bank
    Common.sleep_with_countdown(15)
    print("enter bank")
    pyautogui.moveTo(1816, 139)
    pyautogui.click()

    # # click bank
    Common.sleep_with_countdown(15)
    print("click bank teller box")
    pyautogui.moveTo(949, 588)
    pyautogui.click()

    # # right click the rune essence (bank: row 7, column 2)
    Common.sleep_with_countdown(10)
    print("right click the rune essence (bank: row 7, column 2)")
    pyautogui.moveTo(715, 365)
    pyautogui.rightClick()

    # # withdraw all rune essence
    Common.sleep_with_countdown(2)
    print("withdraw all rune essence")
    pyautogui.moveTo(708, 461)
    pyautogui.click()

    # # right click mud runes in inventory (first slot in inventory)
    Common.sleep_with_countdown(2)
    print("right click mud runes in inventory (first slot in inventory)")
    pyautogui.moveTo(1737, 767)
    pyautogui.rightClick()

    # # deposit all mud runes
    Common.sleep_with_countdown(2)
    print("deposit all mud runes")
    pyautogui.moveTo(1743, 871)
    pyautogui.click()

    # # get water talisman from bank (bank: row 7 column 3)
    Common.sleep_with_countdown(2)
    print("get water talisman from bank (bank: row 7 column 3)")
    pyautogui.moveTo(760, 360)
    pyautogui.click()
