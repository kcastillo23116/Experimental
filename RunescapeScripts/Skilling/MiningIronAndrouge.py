"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
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
                    - Collapse chat window
Monitors:           4k or 3K display
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Iron mines just east of Ardouge
                    - Hold up arrow to get camera all the way up
                    - Zoom all the way in and zoom about 9-11 ticks out till chatbox does not overlap with
                      bottom iron rock
Menus:              Inventory menu open
equip items:        - Best pickaxe available
items in inventory: - N/A
items in bank:      - N/A
Setup:              - N/A
Objects to mark: - Three iron rocks in a triangle at bottom left of mine

"""
import pyautogui

import RunescapeScripts.Common as Common

# region IMAGES
iron_rocks_images1 = ['Images/Mining/IronAndrouge.png']
iron_rocks_images2 = ['Images/Mining/IronAndrouge2.png']
iron_rocks_images3 = ['Images/Mining/IronAndrouge3.png']
iron_rocks_mined_images1 = ['Images/Mining/IronAndrougeMined.png']
iron_rocks_mined_images2 = ['Images/Mining/IronAndrougeMined2.png']
iron_rocks_mined_images3 = ['Images/Mining/IronAndrougeMined3.png']

iron_ore_images = ['Images/Mining/IronOre.png']
drop_images = ['Images/Drop.png']
# endregion IMAGES


# Get how many from user
itemCountString = input("How many ores do you want to mine? ")

itemCount = int(itemCountString)

try:
    count = 0

    while True:
        print('Loop:', count, '/', itemCountString)

        Common.watch_click_image(iron_rocks_images1, 0.7, 'Click left iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images1,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        Common.watch_click_image(iron_rocks_images2, 0.7, 'Click Right iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images2,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        Common.watch_click_image(iron_rocks_images3, 0.7, 'Click Bottom iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images3,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        # Drop 15 ores
        if count % 15 == 0:
            pyautogui.keyDown('shift')
            while Common.is_image_on_screen(iron_ore_images, 0.4, 0, 'Looking for iron or in inventory',
                                            Common.Inventory_region):
                Common.watch_click_image(iron_ore_images, 0.4, 'Shift Click drop iron in inventory', False, 0, 10, None,
                                         Common.Inventory_region)
            pyautogui.keyUp('shift')

        if count == itemCountString:
            break

        count += 3

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
