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
import Banking as Banking

defaultTimeBeforeClick = 1

# Images
banker_images = ['Images/Banker1.png', 'Images/Banker2.png',
                 'Images/Banker3.png', 'Images/Banker4.png',
                 'Images/Banker5.png', 'Images/Banker6.png',
                 'Images/Banker7.png', 'Images/Banker8.png']
withdraw_x_images = ['Images/Banking/WithdrawX.png', 'Images/Banking/WithdrawXSelected.png']
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
bow_string_images = ['Images/Fletching/Bowstring.png']
unstrung_bow_images = ['Images/Fletching/UnstrungBow.png']
string_bow_images = ['Images/Fletching/StringBow.png']
bow_images = ['Images/Fletching/Bow.png']


def string_bows(item_count):
    try:
        loops_till_done = round(item_count / 14)

        for x in range(loops_till_done):
            Common.print_runtime(loops_till_done, 24, x)

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


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Banking.open_grand_exchange_bank()

    # Sleep a second longer to give bank more time to come up so we can click the X quantity option
    Common.sleep_with_countdown(1)

    # Change withdraw quantity to X
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

    string_bows(itemCount)