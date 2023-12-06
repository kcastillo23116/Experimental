"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite
                    - Turn on 117HD runelite plugin since took screenshots with it on
location:           East Ardougne Bakers stall right on top of the baker NPC
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
                    and zoom all the way in
Menus:              Inventory menu open
"""

import Common as Common

bakeStandImages = ['Images/BakersStall.png']
dropItemImages = ['Images/Cake.png', 'Images/Bread.png', 'Images/ChocolateCake.png']

# Get how many from user
itemCountString = input("How many items do you want to steal? ")
occupiedInvSpaces = input("How many inventory spaces do you have occupied?")

openInvSpaces = 28 - int(occupiedInvSpaces)

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / openInvSpaces)

try:
    for x in range(loopsTillDone):
        # Steal till inventory is full
        for y in range(openInvSpaces):
            Common.click_image(bakeStandImages, 0.9, 4, 'Steal from bake stand')

        # drop inventory
        for y in range(openInvSpaces):
            Common.click_image(dropItemImages, 0.9, 1, 'Right click items to drop', True)
            Common.click_image(['Images/Drop.png'], 0.9, 0, 'Drop item')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

