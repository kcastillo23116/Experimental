"""
How to start:
client:             RuneLite with resizeable modern layout in runescape settings
                    and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    Runelite sidebar CLOSED
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom out all the way
Menus:              Inventory menu open
equip items:        None
items in inventory: Knife at row 1 col 1
items in bank:  Logs(bank: row 1, column 1)
"""

import RunescapeScripts.Common as Common

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 27)

Common.move_mouse_and_left_click(1876, 1059, 5, "Click on Bank teller")

for x in range(loopsTillDone):
    Common.move_mouse_and_left_click(1188, 275, 5, "Click on item to withdraw")
    Common.move_mouse_and_left_click(2216, 107, 2, "Click Close button on Bank")
    Common.move_mouse_and_left_click(3412, 1347, 4, "Click on knife")
    Common.move_mouse_and_left_click(3499, 1343, 1, "Click on wood")
    Common.move_mouse_and_left_click(633, 1910, 2, " Click on craft button")
    Common.move_mouse_and_left_click(1878, 1071, 51, " Wait for all to finish crafting and click bank teller")
    Common.move_mouse_and_left_click(3499, 1343, 1, "Deposit all processed items")

