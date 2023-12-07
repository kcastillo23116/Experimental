"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - 117HD OFF and GPU ON
                    - Turn off runelite Mouse Tooltips plugin
                    - Turn on Menu Entry Swapper runelite plugin, shift right click alch item and select
                      "swap left click Use"
Monitors:           4k or 3K display
bank settings:      - Withdraw as: Item, Quantity: All
                    - Set Withdraw-X quantity to 14
location:           - Right bankers at Grand Exchange
Menus:              - Inventory open
                    - Set Spell filters to uncheck "show spells you lack the runes to cast"
equip items:        - Fire staff
items in inventory: - Knife
items in bank:      - Logs
                    - Nature runes
                    - Items to be alched
Setup:              - Zoom all the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common
import Banking as Banking
import FletchBow as FletchBow
import StringBow as StringBow
import MagicAlch as MagicAlch

# Only run code below if running this script
if __name__ == '__main__':
    # Get how many items from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    itemToAlchImages = MagicAlch.select_item_to_alch()

    Banking.open_grand_exchange_bank()

    FletchBow.fletch_bows(itemCount)

    # Deposit knife
    Common.watch_click_image(['Images/Knife.png'], 0.7, 'Deposit knife',
                             False, 1, 10, None,
                             Common.Inventory_region)

    # Change withdraw quantity to X
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

    StringBow.string_bows(itemCount)

    # TODO Change withdraw quantity to All
    # TODO Change withdraw type to Note
    # TODO Click strung bows and nature runes
    # TODO Open magic tab
    # TODO Uncomment code below when todos above are done
    #MagicAlch.alch_items(itemCount, itemToAlchImages)
