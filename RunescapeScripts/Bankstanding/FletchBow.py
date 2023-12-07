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
                    Quantity: All
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              Inventory menu open
equip items:        None
items in inventory: Knife at row 1 col 1
items in bank:  Logs(bank: row 1, column 2)
"""

import Common as Common
import Banking as Banking

defaultTimeBeforeClick = 1

# Images
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
wood_images = ['Images/Wood.png', 'Images/Wood2.png']
banker_images = ['Images/Banker1.png', 'Images/Banker2.png',
                 'Images/Banker3.png', 'Images/Banker4.png',
                 'Images/Banker5.png', 'Images/Banker6.png',
                 'Images/Banker7.png', 'Images/Banker8.png']


def fletch_bows(item_count):
    """
    Fletch loop
    """
    try:
        # Calculate how many loops needed
        loops_till_done = round(item_count / 27)

        for x in range(loops_till_done):
            Common.print_runtime(loops_till_done, 55, x)

            Common.click_image(['Images/Wood2.png'], 0.7, defaultTimeBeforeClick, 'Get wood')
            Common.click_image(bank_close_images, 0.9, defaultTimeBeforeClick, 'Close bank')
            Common.click_image(['Images/Knife.png'], 0.5, defaultTimeBeforeClick, 'Click knife')
            Common.click_image(wood_images, 0.7, defaultTimeBeforeClick, 'Click inventory wood')
            Common.click_image(['Images/LongBow.png', 'Images/LongBow.png'], 0.7, defaultTimeBeforeClick, 'Click longbow craft menu option')
            Common.click_image(banker_images, 0.3, 49, 'Right click banker', True)
            Common.click_image(['Images/BankOption.png'], 0.7, defaultTimeBeforeClick, 'Open bank')
            Common.click_image(['Images/LongBowInventory.png'], 0.7, defaultTimeBeforeClick, 'Deposit longbows')

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Banking.open_grand_exchange_bank()
    fletch_bows(itemCount)
