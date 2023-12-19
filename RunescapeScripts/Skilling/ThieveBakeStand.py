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
Objects to mark:    - None
"""
from random import randrange
from time import sleep

import pyautogui

import Common as Common
import Display

# Click bottom left corner of stall so don't run to other spot when clicking empty stall on accident
bakeStandImages = ['Images/Thieving/BakerStall.png']
bakeStandEmptyImages = ['Images/Thieving/BakerStallEmpty.png']
dropItemImages = ['Images/Thieving/Cake.png', 'Images/Thieving/Bread.png', 'Images/Thieving/ChocolateCake.png']


def steal_bake_stall():
    try:
        # Get how many from user
        item_count_string = input("How many items do you want to steal? ")

        # Calculate how many iterations needed
        item_count = int(item_count_string)
        iterations_till_done = item_count/28

        # Start at 1 so don't go into drop inventory function after first steal
        stolen_item_count = 1

        start_time = Display.start_timer()

        for x in range(item_count):
            x = randrange(1175, 1450)
            y = randrange(1035, 1355)

            Common.move_mouse_and_left_click(x, y, 0,
                                             'Steal from bake stand')

            # Use sleep here to get decimal seconds for more precision
            sleep(2.8)

            # Drop all items every 28 steals
            if stolen_item_count % 28 == 0:
                Common.drop_inventory(0.3)

                # display timer after first inventory drop to get a full iteration and more accurate timing
                Display.stop_timer(start_time, iterations_till_done)

            stolen_item_count += 1

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    steal_bake_stall()
    print("Stealing done!")
