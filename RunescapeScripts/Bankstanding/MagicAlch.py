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
bank settings:      - N/A
location:           - N/A
Menus:              - Spell menu open
                    - Set Spell filters to uncheck "show spells you lack the runes to cast"
equip items:        - Fire staff
items in inventory: - Nature runes
                    - Noted items to be alched
items in bank:      - None
Setup:              - None
Objects to mark:    - With: NPC Indicator settings:
                        - Highlight Hull
                        - Highlight tile
                        - Highlight outline
                        - Highlight and Fill color: Cyan (FF00FFFF)
                        - Border width 2

"""
import timeit
from threading import Thread

import Common as Common
import Display

# region IMAGES
alch_spell_images = ['Images/Magic/Alch.png']
# endregion IMAGES


def select_item_to_alch():
    arrow_images = ['Images/Magic/Arrows.png']
    noted_bow_images = ['Images/Magic/NotedBows.png']

    # Set images for item to be alched
    item_to_alch = input("Type number: 1.Arrows or 2.Bows? ")

    alch_item_images = ['None']
    if item_to_alch == 1:
        return arrow_images
    else:
        return noted_bow_images


# Optional get_timing parameter can be used to do one run to get time per iteration to set up countdown timer with
# different scripts running one after another
def alch_items(item_count, alch_item_images, get_timing=False, display_timer=False):
    try:
        count = 0

        timer_started = False
        while True:
            # Get start time now to calculate how much time to make a single iteration
            start = timeit.default_timer()

            Common.print_runtime(item_count, 3, count)

            Common.watch_click_image(alch_spell_images, 0.6, 'Click alch spell',
                                     False, 1, 10, alch_item_images,
                                     Common.Inventory_region, next_step_confidence=0.6)

            Common.watch_click_image(alch_item_images, 0.6, 'Click item to alch',
                                     False, 2, 10,
                                     alch_spell_images, Common.Inventory_region, next_step_confidence=0.6)

            # Get stop time now to calculate how much time to make a single iteration
            stop = timeit.default_timer()
            seconds_per_iteration = round(stop - start)

            # If we just want timing for displaying countdown timer return after first iteration here
            if get_timing:
                return seconds_per_iteration

            if display_timer:
                # Subtract iteration already ran
                Display.start_timer_thread(item_count - 1, seconds_per_iteration)

            if count >= item_count:
                break

            count += 1

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    # Get info from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    alchItemImages = select_item_to_alch()
    alch_items(itemCount, alchItemImages, False, True)

    print("Alching done!")
