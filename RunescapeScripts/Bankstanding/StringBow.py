"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75% and performance mode enabled
                    - Runelite sidebar CLOSED
                    - NPC Indicators plugin: Highlight hull, highlight outline, highlight color: FF00FFFF, Border width: 2
                    - Turn on NPC Indicators plugin, Shift+Right click banker and click Tag All
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite
                    - 117HD OFF
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: Default quantity set to Withdraw 14 as Item
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              Inventory menu open
equip items:        None
items in inventory: None
items in bank:  Bow String and unstrung bow: top row
"""

import Common as Common

defaultTimeBeforeClick = 1

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 14)

try:
    # Open bank to start
    banker_images = ['Images/Banker1.png', 'Images/Banker2.png',
                     'Images/Banker3.png', 'Images/Banker4.png',
                     'Images/Banker5.png', 'Images/Banker6.png',
                     'Images/Banker7.png', 'Images/Banker8.png']
    bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
    bow_string_images = ['Images/Fletching/Bowstring.png']
    unstrung_bow_images = ['Images/Fletching/UnstrungBow.png']
    string_bow_images = ['Images/Fletching/StringBow.png']
    bow_images = ['Images/Fletching/Bow.png']

    Common.click_image(banker_images, 0.3, defaultTimeBeforeClick, 'Right click banker', True)
    Common.click_image(['Images/BankOption.png'], 0.7, defaultTimeBeforeClick, 'Open bank')

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, 24, x)

        Common.click_image(bow_string_images, 0.7, defaultTimeBeforeClick, 'Get bow strings')
        Common.click_image(unstrung_bow_images, 0.7, defaultTimeBeforeClick, 'Get unstrung bows')
        Common.click_image(bank_close_images, 0.9, defaultTimeBeforeClick, 'Close bank')
        Common.click_image(bow_string_images, 0.7, defaultTimeBeforeClick, 'Click inventory bowstring')
        Common.click_image(unstrung_bow_images, 0.7, defaultTimeBeforeClick, 'Click inventory unstrung bow')
        Common.click_image(string_bow_images, 0.7, defaultTimeBeforeClick, 'Click string bow')
        Common.click_image(banker_images, 0.3, 18, 'Right click banker', True)
        Common.click_image(['Images/BankOption.png'], 0.7, defaultTimeBeforeClick, 'Open bank')
        Common.click_image(bow_images, 0.7, defaultTimeBeforeClick, 'Deposit longbows')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

