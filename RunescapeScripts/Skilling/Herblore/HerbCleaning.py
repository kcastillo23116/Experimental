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
bank settings:      - Withdraw as: Item, Quantity: All
location:           - Right bankers at Grand Exchange
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - None
items in bank:      - In currently white feather tab:
                        - Grimy herbs
Setup:              - Zoom all the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common
import Display
import Banking

grimy_herb_bank_images = ['Images/Herblore/GrimyHerbBank.png']
grimy_herb_images = ['Images/Herblore/GrimyHerb.png']
clean_herb_images = ['Images/Herblore/CleanHerb.png']
feather_tab_images = ['Images/Fletching/FeatherTab.png']


def clean_herbs(item_count):
    # Calculate how many loops needed
    loops_till_done = round(item_count / 28)

    for x in range(loops_till_done):
        start_time = Display.start_timer()

        Common.watch_click_image(grimy_herb_bank_images, 0.6, 'Withdraw grimy herbs and make sure it is in inventory',
                                 False, 1, 10, current_step_region=Common.Bank_region,
                                 next_step_image_paths=grimy_herb_images, next_step_region=Common.Inventory_region,
                                 next_step_confidence=0.4)

        Banking.close_bank()

        Common.click_whole_inv_items(0.5)

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
                             'Click on white feather tab for fletching items and look for grimy herbs in bank window',
                             False, 1, 10, grimy_herb_bank_images,
                             Common.Top_half_game_screen_region)

    clean_herbs(itemCount)

    print("Herb cleaning done!")
