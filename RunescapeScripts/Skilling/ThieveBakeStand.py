"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - Turn off ground items in runelite plugins
                    - 117HD OFF and GPU ON
                    - Set Object Markers
                    - Turn off runelite Mouse Tooltips plugin
                    - Collapse chat window
Monitors:           4k or 3K display
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - East Ardougne Bakers stall right on top of the baker NPC
                    - Hold up arrow to get camera all the way up
                    - Zoom in all the way
Menus:              Inventory menu open
equip items:        - None
items in inventory: - N/A
items in bank:      - N/A
Setup:              - N/A
Objects to mark: - Bakers stall default yellow
"""
from time import sleep

import Common as Common
import Display

bakeStandImages = ['Images/Thieving/BakerStall.png']
dropItemImages = ['Images/Thieving/Cake.png', 'Images/Thieving/Bread.png', 'Images/Thieving/ChocolateCake.png']


def steal_bake_stall():
    try:
        # Get how many from user
        item_count_string = input("How many items do you want to steal? ")

        # Calculate how many loops needed
        item_count = int(item_count_string)
        iterations_till_done = round(item_count / 28)

        # Start at 1 so don't go into drop inventory function after first steal
        stolen_item_count = 1

        for x in range(iterations_till_done):
            start_time = Display.start_timer()

            Common.watch_click_image(bakeStandImages, 0.7,
                                     'Steal from bake stand',
                                     False, 0, 10, None,
                                     Common.All_game_screen_region)
            sleep(1.25)

            # Drop items every 20 steals
            if stolen_item_count % 20 == 0:
                Common.drop_inventory_items(dropItemImages)

                # display timer after first inventory drop to get a full iteration and more accurate timing
                Display.stop_timer(start_time, iterations_till_done)

            stolen_item_count += 1

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    steal_bake_stall()
    print("Stealing done!")
