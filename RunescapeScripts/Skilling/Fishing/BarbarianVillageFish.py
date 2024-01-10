"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on Interfaces > Disable level-up interface in runescape options so levels don't cancel
                      actions and mess up scripts
                    - Turn on entity hider in runelite to hide other players and random events but don't hide NPCs.
                      Fishing spots are treated as NPCs
                    - 117HD OFF and GPU ON
                    - Turn off runelite Mouse Tooltips plugin
                    - Enable runelite fishing plugin so it shows fishing status at top left
Monitors:           4k display
bank settings:      - N/A
location:           - Barbarian Village fishing spots
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - Fishing rod
                    - Feathers
items in bank:      - N/A
Setup:              - Zoom all the way out and right-click the compass to look West and hold up arrow to move camera
                      all the way up
                    - Inventory tab open an visible
Objects to mark:    - Fishing spots with fill and default cyan
"""
from time import sleep

import Common as Common
import Display

fishing_spot_images = ['Images/Fishing/FishingSpot1.png', 'Images/Fishing/FishingSpot2.png']
not_fishing_status_images = ['Images/Fishing/NotFishingStatus.png']
trout_images = ['Images/Fishing/Trout.png']


def catch_fish():

    # Get how many from user
    item_count_string = input("How many fish do you want to catch? ")
    item_count = int(item_count_string)

    # start_time = Display.start_timer()

    # Click fishing spot to start and get runelite fishing plugin status message to show
    Common.watch_click_image(fishing_spot_images, 0.7,
                             'Click fishing spot',
                             False, 10, 10, current_step_region=Common.Main_game_screen_region)

    while True:
        if Common.is_image_on_screen(not_fishing_status_images, 0.7, 0, 'Check if not fishing',
                                     Common.Status_message_top_left):
            Common.watch_click_image(fishing_spot_images, 0.7,
                                     'Click fishing spot',
                                     False, 10, 10, current_step_region=Common.Main_game_screen_region)

            # Drop trout in inventory
            Common.drop_inventory_items(trout_images)

            # TODO: Sort out timer display loops till done
            # Display.stop_timer(start_time, loops_till_done)



# Only run code below if running this script
if __name__ == '__main__':
    catch_fish()
    print("Fishing done!")
