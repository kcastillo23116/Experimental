"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on Interfaces > Disable level-up interface in runescape options so levels don't cancel
                      actions and mess up scripts
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
items in bank:      - In tab with White Feather icon:
                        - Knife
                        - Logs
                    - In Tab with Gold Coin Stack icon:
                        - Nature runes
                        - Strung bows
Setup:              - Zoom all the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common
import Display
import FletchBow as FletchBow
import StringBow as StringBow
import MagicAlch as MagicAlch
from Bankstanding import Banking

knife_images = ['Images/Knife.png']
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
gold_tab_images = ['Images/Banking/GoldTab.png']
deposit_inventory_images = ['Images/Banking/DepositInventory.png']
withdraw_all_images = ['Images/Banking/WithdrawAll.png', 'Images/Banking/WithdrawAllSelected.png']
withdraw_note_images = ['Images/Banking/WithdrawNote.png', 'Images/Banking/WithdrawNoteSelected.png']
bank_bow_images = ['Images/Fletching/BankBow.png']  # Need separate image for bank bow since it's cutoff by numbers
feather_tab_images = ['Images/Fletching/FeatherTab.png']
nature_rune_images = ['Images/Runes/NatureRune.png', 'Images/Runes/NatureRune2.png']
noted_bow_images = ['Images/Magic/NotedBows.png']
spellbook_images = ['Images/Magic/SpellbookTab.png']
inventory_icon_images = ['Images/General/InventoryIcon.png']
empty_inventory_images = ['Images/General/EmptyInventory.png']


def fletch_string_alch(item_count, get_timing=False):
    Banking.open_grand_exchange_bank()

    Common.watch_click_image(feather_tab_images, 0.7,
                             'Click on white feather tab for fletching items and look for knife in bank window',
                             False, 1, 10, knife_images,
                             Common.Top_half_game_screen_region)

    Common.watch_click_image(knife_images, 0.7, 'Withdraw knife and make sure it is in inventory',
                             False, 1, 10,
                             current_step_region=Common.Bank_region,
                             next_step_image_paths=knife_images, next_step_region=Common.Inventory_region)

    seconds_per_fletch_iteration = FletchBow.fletch_bows(item_count, get_timing)

    Common.watch_click_image(knife_images, 0.7, 'Deposit knife',
                             False, 1, 10, None,
                             Common.Inventory_region)
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

    seconds_per_string_bow_iteration = StringBow.string_bows(item_count, get_timing)

    # Setup for alching items
    Common.watch_click_image(withdraw_all_images, 0.7, 'Change Withdraw Quantity to All',
                             current_step_region=Common.Bank_bottom_options_region)
    Common.watch_click_image(withdraw_note_images, 0.7, 'Change Withdraw Type to Note',
                             current_step_region=Common.Bank_bottom_options_region)
    Common.watch_click_image(gold_tab_images, 0.7, 'Switch to Gold Tab',
                             current_step_region=Common.Top_half_game_screen_region)
    Common.watch_click_image(nature_rune_images, 0.6, 'Withdraw Nature Runes, make sure they are in inventory',
                             current_step_region=Common.Bank_region, sleep_time_after_click=1,
                             next_step_image_paths=nature_rune_images, next_step_region=Common.Inventory_region,
                             next_step_confidence=0.6)
    Common.watch_click_image(bank_bow_images, 0.7,
                             'Withdraw strung bows and make sure they are in inventory as noted bows',
                             current_step_region=Common.Bank_region,
                             next_step_image_paths=noted_bow_images, next_step_region=Common.Inventory_region)
    Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)
    Common.watch_click_image(spellbook_images, 0.7, 'Open Magic Spellbook Tab',
                             current_step_region=Common.Inventory_bar_region)
    seconds_per_alch_item_iteration = MagicAlch.alch_items(item_count, noted_bow_images, get_timing)

    if get_timing:
        # Reset for actual runs
        Banking.open_grand_exchange_bank()
        Common.watch_click_image(deposit_inventory_images, 0.7,
                                 'Deposit inventory and make sure inventory is empty before next step',
                                 current_step_region=Common.Bank_bottom_options_region,
                                 next_step_image_paths=empty_inventory_images,
                                 next_step_region=Common.Bottom_half_game_screen_region)
        Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)
        Common.watch_click_image(inventory_icon_images, 0.7, 'Switch to inventory menu', sleep_time_after_click=1,
                                 current_step_region=Common.Inventory_bar_region)

        # Calculate how many loops needed
        fletch_bow_iterations = round(item_count / 27)
        string_bow_iterations = round(item_count / 14)
        alch_item_iterations = item_count

        # Calculate time to process specified item count in seconds. Subtract one for the get timing iteration
        seconds_to_fletch_all = (fletch_bow_iterations - 1) * seconds_per_fletch_iteration
        seconds_to_string_all = (string_bow_iterations - 1) * seconds_per_string_bow_iteration
        seconds_to_alch_all = (alch_item_iterations - 1) * seconds_per_alch_item_iteration

        total_runtime = seconds_to_fletch_all + seconds_to_string_all + seconds_to_alch_all

        return total_runtime


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many items from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    # Run through steps once to get total runtime and display timer
    total_runtime_seconds = fletch_string_alch(itemCount, True)
    Display.start_timer_thread_total_time(total_runtime_seconds)

    fletch_string_alch(itemCount)
