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
Monitors:           4k display
bank settings:      - Withdraw as: Item and All
location:           - Right banker at edgeville
Menus:              - Inventory open
equip items:        - Boots of lightness and naked everything else for lowest weight less stamina used
items in inventory: - None
items in bank:      - In gold coin tab:
                        - Cannon Ball Ammo Mold
                    - In white feather tab:
                        - Steel Bars
Setup:              - Zoom out the way in and click the compass to center North and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Top leftmost bank booth and furnace on right marked as default yellow
"""

import Common as Common
import Display
from Bankstanding.Banking import bank_withdraw_note_images

feather_tab_images = ['Images/Fletching/FeatherTab.png']
gold_tab_images = ['Images/Banking/GoldTab.png']
bank_booth_1_images = ['Images/Smithing/BankBooth1.png']
ammo_mold_images = ['Images/Smithing/AmmoMold.png']
steel_bar_bank_images = ['Images/Smithing/SteelBarBank.png']
furnace_images = ['Images/Smithing/Furnace.png']
make_cannon_ball_images = ['Images/Smithing/MakeCannonBalls.png']
bank_booth_2_images = ['Images/Smithing/BankBooth2.png']
cannon_ball_images = ['Images/Smithing/CannonBalls.png']


def make_cannonballs(item_count):
    # Calculate how many loops needed
    loops_till_done = round(item_count / 26)

    for x in range(loops_till_done):
        start_time = Display.start_timer()

        Common.watch_click_image(steel_bar_bank_images, 0.7,
                                 'Withdraw steel bars and make sure they are in inventory',
                                 False, 1, 10, current_step_region=Common.Bank_region,
                                 next_step_image_paths=steel_bar_bank_images, next_step_region=Common.Inventory_region,
                                 next_step_confidence=0.7)

        Common.watch_click_image(furnace_images, 0.7,
                                 'Click on furnace and look for make cannon ball option',
                                 False, 6, 10, current_step_region=Common.All_game_screen_region,
                                 next_step_image_paths=make_cannon_ball_images, next_step_region=Common.Chatbox_region,
                                 next_step_confidence=0.6)

        Common.watch_click_image(make_cannon_ball_images, 0.7,
                                 'Click on make cannon balls option and look for cannon balls in inventory',
                                 False, 160, 10, current_step_region=Common.Chatbox_region,
                                 next_step_image_paths=cannon_ball_images, next_step_region=Common.Inventory_region,
                                 next_step_confidence=0.5)

        Common.watch_click_image(bank_booth_2_images, 0.7,
                                 'Click on bank booth 2 and look for bank note option to make sure bank is open',
                                 False, 6, 10, current_step_region=Common.All_game_screen_region,
                                 next_step_image_paths=bank_withdraw_note_images, next_step_region=Common.Bank_bottom_options_region,
                                 next_step_confidence=0.6)

        Display.stop_timer(start_time, loops_till_done)


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Common.watch_click_image(bank_booth_1_images, 0.7,
                             'Click on bank booth 1 and look for note option at bottom to make sure bank is open',
                             False, 1, 10, current_step_region=Common.Center_game_screen_region,
                             next_step_image_paths=bank_withdraw_note_images, next_step_confidence=0.4,
                             next_step_region=Common.Bank_bottom_options_region)

    Common.watch_click_image(gold_tab_images, 0.7,
                             'Click on gold coin tab and look for ammo mold',
                             False, 1, 10, current_step_region=Common.Top_half_game_screen_region,
                             next_step_image_paths=ammo_mold_images, next_step_confidence=0.5, next_step_region=Common.Bank_region)

    Common.watch_click_image(ammo_mold_images, 0.7,
                             'Withdraw ammo mold and make sure it is in inventory',
                             False, 1, 10, current_step_region=Common.Bank_region,
                             next_step_image_paths=ammo_mold_images, next_step_confidence=0.4, next_step_region=Common.Inventory_region)

    Common.watch_click_image(feather_tab_images, 0.7,
                             'Click on white feather tab and look for steel bars',
                             False, 2, 10, current_step_region=Common.Top_half_game_screen_region,
                             next_step_image_paths=steel_bar_bank_images, next_step_confidence=0.7, next_step_region=Common.Bank_region)

    make_cannonballs(itemCount)

    print("Cannon Ball making done!")
