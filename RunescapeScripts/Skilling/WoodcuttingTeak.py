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
Monitors:           4k or 3K display
bank settings:      N/A
location:           - Teak tree SW of castle wars (can see it on map)
Menus:              - Inventory open
equip items:        - Best woodcutting axe
items in inventory: - Empty
items in bank:      - N/A
Setup:              - N/A
Objects to mark:        - Teak tree SW of castle wars (can see it on map)

"""
import pyautogui

from Skilling import Common as Common

# Constants
runtime = 1

# region IMAGES
teak_tree_images = ['Images/Woodcutting/CastlwarsTeak.png']
teak_log_images = ['Images/Woodcutting/TeakLogs.png']
empty_inv_images = ['Images/Woodcutting/EmptyInvSlot.png']
# endregion IMAGES


# Get how many from user
itemCountString = input("How many logs do you want? ")

itemCount = int(itemCountString)

try:
    count = 0

    while True:
        Common.print_runtime(itemCount, runtime, count)

        Common.watch_click_image(teak_tree_images, 0.5, 'Click tree',
                                 False, 4, 10, None,
                                 Common.Top_half_game_screen_region)

        # Drop all logs once inventory is full
        if Common.is_image_on_screen(empty_inv_images, 0.7, 0, 'Are there any empty inventory slots?',
                                     Common.Inventory_region) is False:
            pyautogui.keyDown('shift')
            while Common.is_image_on_screen(teak_log_images, 0.4, 0, 'Are there teak logs in inventory?',
                                            Common.Inventory_region):

                Common.watch_click_image(teak_log_images, 0.4, 'Shift click drop log in inventory', False, 0, 10, None,
                                         Common.Inventory_region)
                count += 1
            pyautogui.keyUp('shift')

        if count >= itemCount:
            break


# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
