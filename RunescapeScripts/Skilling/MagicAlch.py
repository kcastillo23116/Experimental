"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - 117HD OFF and GPU ON
                    - Set Object Markers:
                      - Border width: 6
                      - Marker colors: FFD400FF
                      - Highlight clickbox enabled with all others disabled
                      - Remember color per object
                    - Turn off runelite Mouse Tooltips plugin
                    - Turn on Menu Entry Swapper runelite plugin, shift right click alch item and select
                      "swap left click Use"
Monitors:           4k or 3K display
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - N/A
Menus:              - Spell menu open
                    - Set Spell filters to uncheck "show spells you lack the runes to cast"
equip items:        - Fire staff
items in inventory: - Nature runes
                    - Rune arrows
items in bank:      - N/A
Setup:              - N/A
Objects to mark:        - N/A

"""

import RunescapeScripts.Common as Common

# Constants
runtime = 1

# region IMAGES
alch_spell_images = ['Images/Magic/Alch.png']
arrow_images = ['Images/Magic/Arrows.png']
# endregion IMAGES


# Get how many from user
itemCountString = input("How many items do you have? ")

itemCount = int(itemCountString)

try:
    count = 0

    while True:
        Common.print_runtime(itemCount, runtime, count)

        Common.watch_click_image(alch_spell_images, 0.7, 'Click alch spell',
                                 False, 1, 10, None,
                                 Common.Inventory_region)

        Common.watch_click_image(arrow_images, 0.7, 'Click arrows',
                                 False, 1, 10, None,
                                 Common.Inventory_region)

        if count == itemCountString:
            break

        count += 1

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
