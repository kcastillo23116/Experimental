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
items in inventory: - None
items in bank:      - In starting tab
                        - Knife
                        - Logs
                    - In Tab with Gold coin icon
                        - Nature runes
                        - Strung bows
Setup:              - Zoom all the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common
import Banking as Banking
import FletchBow as FletchBow
import StringBow as StringBow
import MagicAlch as MagicAlch

withdraw_all_images = ['Images/Banking/WithdrawAll.png', 'Images/Banking/WithdrawAllSelected.png']
withdraw_note_images = ['Images/Banking/WithdrawNote.png', 'Images/Banking/WithdrawNoteSelected.png']
gold_tab_images = ['Images/Banking/GoldTab.png']
nature_rune_images = ['Images/Runes/NatureRune.png']
spellbook_images = ['Images/Magic/SpellbookTab.png']
knife_images = ['Images/Knife.png']
bank_bow_images = ['Images/Fletching/BankBow.png']  # Need separate image for bank bow since it's cutoff by numbers
noted_bow_images = ['Images/Magic/NotedBows.png']
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']

# Only run code below if running this script
if __name__ == '__main__':
    # Get how many items from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Banking.open_grand_exchange_bank()

    Common.watch_click_image(knife_images, 0.7, 'Withdraw knife and make sure it is in inventory',
                             False, 1, 10,
                             current_step_region=Common.Bank_region,
                             next_step_image_paths=knife_images, next_step_region=Common.Inventory_region)

    FletchBow.fletch_bows(itemCount)

    Common.watch_click_image(knife_images, 0.7, 'Deposit knife',
                             False, 1, 10, None,
                             Common.Inventory_region)
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

    StringBow.string_bows(itemCount)

    # Setup for alching items
    Common.watch_click_image(withdraw_all_images, 0.7, 'Change Withdraw Quantity to All',
                             current_step_region=Common.Bank_bottom_options_region)
    Common.watch_click_image(withdraw_note_images, 0.7, 'Change Withdraw Type to Note',
                             current_step_region=Common.Bank_bottom_options_region)
    Common.watch_click_image(gold_tab_images, 0.7, 'Switch to Gold Tab',
                             current_step_region=Common.Top_half_game_screen_region)
    Common.watch_click_image(nature_rune_images, 0.7, 'Withdraw Nature Runes',
                             current_step_region=Common.Bank_region)
    Common.watch_click_image(bank_bow_images, 0.7,
                             'Withdraw strung bows and make sure they are in inventory as noted bows',
                             current_step_region=Common.Bank_region,
                             next_step_image_paths=noted_bow_images, next_step_region=Common.Inventory_region)
    Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)
    Common.watch_click_image(spellbook_images, 0.7, 'Open Magic Spellbook Tab',
                             current_step_region=Common.Inventory_bar_region)
    MagicAlch.alch_items(itemCount, noted_bow_images)
