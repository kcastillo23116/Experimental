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
Monitors:           4k display
bank settings:      - Withdraw as: Item
location:           - Right bankers at Grand Exchange
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - None
items in bank:      - In currently white feather tab:
                        - Unfinished potion
                        - Ingredient i.e. Limpwurt root
Setup:              - Zoom all the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common
import Display
from Bankstanding import Banking

feather_tab_images = ['Images/Fletching/FeatherTab.png']
unfinished_pot_bank_images = ['Images/Herblore/UnfinishedStrPotBank.png']
ingredient_bank_images = ['Images/Herblore/LimpwurtRootBank.png']
unfinished_pot_images = ['Images/Herblore/UnfinishedStrPotBank.png']
ingredient_images = ['Images/Herblore/LimpwurtRoot.png']
make_potion_images = ['Images/Herblore/MakeSuperStrengthPotion.png']


def make_potions(item_count):
    # Calculate how many loops needed
    loops_till_done = round(item_count / 28)

    for x in range(loops_till_done):
        start_time = Display.start_timer()

        Common.watch_click_image(unfinished_pot_bank_images, 0.6,
                                 'Withdraw 14 unfinished kwuarm potions and make sure they are in inventory',
                                 False, 1, 10, current_step_region=Common.Bank_region,
                                 next_step_image_paths=unfinished_pot_images, next_step_region=Common.Inventory_region,
                                 next_step_confidence=0.4)

        Common.watch_click_image(ingredient_bank_images, 0.6,
                                 'Withdraw 14 limpwurt roots  and make sure they are in inventory',
                                 False, 1, 10, current_step_region=Common.Bank_region,
                                 next_step_image_paths=ingredient_images, next_step_region=Common.Inventory_region,
                                 next_step_confidence=0.4)

        Banking.close_bank()

        Common.watch_click_image(unfinished_pot_images, 0.6,
                                 'Left click unfinished potion',
                                 False, 1, 10, current_step_region=Common.Inventory_region)

        Common.watch_click_image(ingredient_images, 0.6,
                                 'Left click ingredient',
                                 False, 1, 10, current_step_region=Common.Inventory_region)

        Common.watch_click_image(make_potion_images, 0.6,
                                 'Click make potion option in chat box and wait',
                                 False, 16, 10, current_step_region=Common.Chatbox_region)

        Banking.open_grand_exchange_bank()
        Banking.deposit_inventory()

        Display.stop_timer(start_time, loops_till_done)


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Banking.open_grand_exchange_bank()

    Common.watch_click_image(feather_tab_images, 0.7,
                             'Click on white feather tab for fletching items and look for unfinished pots in bank window',
                             False, 1, 10, unfinished_pot_bank_images,
                             Common.Top_half_game_screen_region)

    Banking.change_to_withdraw_x()

    make_potions(itemCount)

    print("Potion making done!")
