"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn on object markers plugin and Shift+Right click bank to mark it
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
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

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 27)

try:
    # Open bank to start
    banker_images = ['Images/Banker.png', 'Images/Banker2.png',
                     'Images/Banker3.png', 'Images/Banker4.png',
                     'Images/Banker5.png']
    bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
    wood_images = ['Images/Wood.png', 'Images/Wood2.png']
    Common.click_image(banker_images, 0.2, 1, 'Right click banker', True)

    Common.click_image(['Images/BankOption.png'], 0.7, 1, 'Open bank')

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, 55, x)

        Common.click_image(['Images/Wood2.png'], 0.7, 1, 'Get wood')
        Common.click_image(bank_close_images, 0.9, 1, 'Close bank')
        Common.click_image(['Images/Knife.png'], 0.5, 1, 'Click knife')
        Common.click_image(wood_images, 0.7, 1, 'Click inventory wood')
        Common.click_image(['Images/LongBow.png'], 0.7, 1, 'Click longbow craft menu option')
        Common.click_image(banker_images, 0.2, 49, 'Right click banker', True)
        Common.click_image(['Images/BankOption.png'], 0.7, 1, 'Open bank')
        Common.click_image(['Images/LongBowInventory.png'], 0.7, 1, 'Deposit longbows')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

