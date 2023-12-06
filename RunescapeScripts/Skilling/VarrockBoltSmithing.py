"""
How to start:
client:             RuneLite with resizeable modern layout in runescape settings
                    and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    Runelite sidebar CLOSED
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           East Varrock Bank, directly in front of the bottommost bank teller box
                    click compass, so it's at default north and zoom out all the way and hold up arrow key to move
                    camera up
Menus:              None
equip items:        None
items in inventory: Hammer
items in bank:  Metal Bars (bank: row 1, column 1)
"""

from Skilling import Common as Common
import datetime

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 27)

Common.move_mouse_and_left_click(1978, 1030, 2, "Click Bank Teller")

for x in range(loopsTillDone):
    print("Loop: ", x, "/", loopsTillDone)
    runtime = ((loopsTillDone - x) * 102)
    dtg = str(datetime.timedelta(seconds=runtime))
    print("Approx time till done: ", dtg)

    Common.move_mouse_and_left_click(1168, 292, 2, "Get Bars")
    Common.move_mouse_and_left_click(2152, 1786, 2, "Click on anvil")
    Common.move_mouse_and_left_click(1910, 583, 7, "Select bolt tips")
    Common.move_mouse_and_left_click(1813, 592, 82, "Wait for smithing to end and click bank")
    Common.move_mouse_and_left_click(3446, 1382, 9, "Deposit tips")

