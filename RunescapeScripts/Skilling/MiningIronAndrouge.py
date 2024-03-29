"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - Turn off ground items in runelite plugins
                    - 117HD OFF and GPU ON
                    - Set Object Markers:
                      - Border width: 6
                      - Marker colors: FFD400FF
                      - Marker Outline and Fill to same color above
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

import Common as Common
import Display

# region IMAGES
iron_rocks_images1 = ['Images/Mining/IronAndrouge.png']
iron_rocks_images2 = ['Images/Mining/IronAndrouge2.png']
iron_rocks_images3 = ['Images/Mining/IronAndrouge3.png']
iron_rocks_mined_images1 = ['Images/Mining/IronAndrougeMined.png']
iron_rocks_mined_images2 = ['Images/Mining/IronAndrougeMined2.png']
iron_rocks_mined_images3 = ['Images/Mining/IronAndrougeMined3.png']

items_to_drop_images = ['Images/Mining/IronOre.png', 'Images/Mining/UncutEmerald.png',
                        'Images/Mining/UncutSapphire.png', 'Images/Mining/UncutDiamond.png']
# endregion IMAGES


# Get how many from user
itemCountString = input("How many ores do you want to mine? ")

itemCount = int(itemCountString)

try:
    count = 0

    while True:
        print('Loop:', count, '/', itemCountString)

        start_time = Display.start_timer()

        Common.watch_click_image(iron_rocks_images1, 0.7, 'Click left iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images1,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        Common.watch_click_image(iron_rocks_images2, 0.7, 'Click Right iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images2,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        Common.watch_click_image(iron_rocks_images3, 0.7, 'Click Bottom iron rocks while looking for iron in inventory',
                                 False, 0, 10, iron_rocks_mined_images3,
                                 Common.Bottom_half_game_screen_region, Common.Bottom_half_game_screen_region)

        # When getting to around 15 items start dropping them till inventory is empty
        if count % 15 == 0:
            pyautogui.keyDown('shift')
            while not (Common.is_image_on_screen(Common.empty_inventory_images, 0.7, 0,
                                                 'Looking for empty inventory', Common.Inventory_region)):
                Common.watch_click_image(items_to_drop_images, 0.7,
                                         'Shift Click drop iron and gems in inventory',
                                         False, 0, 10, None,
                                         Common.Inventory_region)
            pyautogui.keyUp('shift')

        if count == itemCountString:
            break

        count += 3

        iterations_till_done = itemCount / 3
        Display.stop_timer(start_time, iterations_till_done)

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
