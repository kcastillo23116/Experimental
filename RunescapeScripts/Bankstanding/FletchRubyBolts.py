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
items in inventory: Chisel, Adamant bolts
items in bank:  Rubies anywhere in bank tab but first slot
"""

from Skilling import Common as Common

# Get how many rubies we're chiseling from user
itemCountString = input("How many rubies do you have? ")

# Calculate how many loops needed to chisel rubies
itemCount = int(itemCountString)
chiselRubyLoopsTillDone = round(itemCount / 25)

# Get how many bolts from user
itemCountString = input("How many adamant bolts do you have? ")

# Calculate how many loops needed to craft bolts
itemCount = int(itemCountString)
craftBoltLoopsTillDone = round(itemCount / 100)

try:
    # Open bank to start
    banker_images = ['Images/Banker.png', 'Images/Banker2.png',
                     'Images/Banker3.png', 'Images/Banker4.png',
                     'Images/Banker5.png']
    bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
    Common.click_image(banker_images, 0.2, 1, 'Right click banker', True)

    Common.click_image(['Images/BankOption.png'], 0.7, 1, 'Open bank')

    for x in range(chiselRubyLoopsTillDone):
        Common.print_runtime(chiselRubyLoopsTillDone, 55, x)

        Common.click_image(['Images/Ruby.png'], 0.7, 1, 'Get rubies')
        Common.click_image(bank_close_images, 0.9, 1, 'Close bank')
        Common.click_image(['Images/Chisel.png'], 0.7, 1, 'Click Chisel')
        Common.click_image(['Images/Ruby.png'], 0.7, 1, 'Click inventory ruby')
        Common.click_image(['Images/RubyTipsCraftIcon.png'], 0.5, 1, 'Click ruby tips craft menu option')
        Common.click_image(banker_images, 0.2, 72, 'Right click banker', True)
        Common.click_image(['Images/BankOption.png'], 0.7, 1, 'Open bank')

    # Close bank so don't deposit items in next loop
    Common.click_image(bank_close_images, 0.9, 1, 'Close bank')

    for x in range(craftBoltLoopsTillDone):
        Common.print_runtime(craftBoltLoopsTillDone, 40, x)

        Common.click_image(['Images/RubyBoltTips.png'], 0.7, 13, 'Click ruby bolt tips')
        Common.click_image(['Images/AdamantBolts.png'], 0.7, 1, 'Click adamant bolts')
        Common.click_image(['Images/RubyBoltsCraftIcon.png'], 0.5, 1, 'Click ruby bolts craft menu option')


# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

