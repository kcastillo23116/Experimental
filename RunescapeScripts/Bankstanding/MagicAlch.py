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
Objects to mark:        - N/A

"""

import Common as Common

# Constants
runtime = 1

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


def alch_items(item_count, alch_item_images):
    try:
        count = 0

        while True:
            Common.print_runtime(item_count, runtime, count)

            Common.watch_click_image(alch_spell_images, 0.7, 'Click alch spell',
                                     False, 1, 10, None,
                                     Common.Inventory_region)

            Common.watch_click_image(alch_item_images, 0.7, 'Click item to alch',
                                     False, 2, 10, None,
                                     Common.Inventory_region)

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
    alch_items(itemCount, alchItemImages)
