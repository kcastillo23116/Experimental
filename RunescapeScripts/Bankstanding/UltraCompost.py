"""
How to start:
client:             RuneLite with resizeable modern layout in runescape settings
                    and RuneLite Stretched mode enabled with Resizable scaling set to 75%
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom out all the way
Menus:              Inventory menu open
equip items:        None
items in inventory: Stack of volcanic Ash at row 1 col 1
items in bank:  1 Supercompost (bank: row 1, column 1)
                2 Volcanic Ash (bank: row 1 column 2)
"""

from Skilling import Common as Common

# Get how many from user
superCompostCountString = input("How many supercomposts do you have? ")

# Calculate how many loops needed
superCompostCount = int(superCompostCountString)
loopsTillDone = round(superCompostCount/27)

Common.move_mouse_and_left_click(1848, 1059, 5, "Click on Bank teller")

for x in range(loopsTillDone):
    Common.move_mouse_and_left_click(1188, 275, 5, "Click on supercompost to withdraw")
    Common.move_mouse_and_left_click(2216, 107, 2, "Click Close button on Bank")
    Common.move_mouse_and_left_click(3367, 1347, 4, "Click on volcanic ash")
    Common.move_mouse_and_left_click(3443, 1343, 1, "Click on super compost")
    Common.move_mouse_and_left_click(633, 1910, 2, " Click on craft button")
    Common.move_mouse_and_left_click(1840, 1071, 34, " Wait for all to finish crafting")
    Common.move_mouse_and_left_click(3455, 1361, 1, " Click bank teller")
    Common.move_mouse_and_left_click(1182, 272, 3, " Deposit all ultracompost")


