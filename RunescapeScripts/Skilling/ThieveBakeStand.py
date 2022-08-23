"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn on object markers plugin and Shift+Right click bank to mark it
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              Inventory menu open
equip items:        None
items in inventory: Knife at row 1 col 1
items in bank:  Logs(bank: row 1, column 2)
"""

import RunescapeScripts.Common as Common

bakeStandImages = ['Images/BakersStall.png']
dropItemImages = ['Images/Cake.png', 'Images/Bread.png', 'Images/ChocolateCake.png']

# Get how many from user
itemCountString = input("How many times do you want to steal? ")
occupiedInvSpaces = input("How many inventory spaces do you have occupied?")

openInvSpaces = 28 - int(occupiedInvSpaces)

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / openInvSpaces)

try:
    # Steal till inventory is full
    for x in range(openInvSpaces):
        Common.click_image(bakeStandImages, 0.9, 4, 'Steal from bake stand')

    # drop inventory
    for x in range(openInvSpaces):
        Common.click_image(dropItemImages, 0.9, 1, 'Right click drop item')
        Common.click_image(['Images\Drop.png'], 0.9, 1, 'Drop item')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

