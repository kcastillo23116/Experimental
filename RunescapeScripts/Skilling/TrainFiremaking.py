"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn on object markers plugin and Shift+Right click bank to mark it
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players
                    - 117HD OFF
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           Grand exchange, in front of the left teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
                    and zoom all the way out
Menus:              Inventory menu open
equip items:        None
items in inventory: Tinderbox
items in bank: Oak Logs
"""

import RunescapeScripts.Common as Common

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 15)

try:
    # Open bank to start
    grandexchange_bank_images = ['Images/GrandexchangeBank.png',
                                 'Images/GrandexchangeBank.png',
                                 'Images/GrandexchangeBank.png']
    bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
    wood_images = ['Images/WillowLogs.png', 'Images/WillowLogs.png']
    bank_pillar_images = ['Images/GrandexchangePillar.png']
    firemaking_tree_images = ['Images/GrandexchangeFiremakingTree.png', 'Images/GrandexchangeFiremakingTreeStump.png']

    Common.click_image(grandexchange_bank_images, 0.7, 1, 'Click bank booth')

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, 65, x)

        Common.click_image(['Images/Wood2.png'], 0.7, 1, 'Get wood')
        Common.click_image(bank_close_images, 0.9, 1, 'Close bank')
        Common.click_image(['Images/GrandexchangeVoteMapIcon.png'], 0.9, 1, 'Move to vote icon')
        Common.click_image(firemaking_tree_images, 0.9, 6, 'Move to tree')

        for x in range(15):
            Common.click_image(['Images/Tinderbox.png'], 0.7, 4, 'Click tinderbox')
            Common.click_image(wood_images, 0.7, 1, 'Click inventory wood')

        Common.click_image(['Images/GrandexchangeVoteMapIcon.png'], 0.9, 1, 'Move to vote icon')
        Common.click_image(bank_pillar_images, 0.9, 6, 'Move to bank using pillars')
        Common.click_image(grandexchange_bank_images, 0.7, 5, 'Click bank booth')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

