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
                    - Turn off "Highlight Marks of Grace" in runelite Agility plugin
                    - Turn off Ground Items Runelite plugin
                    - Turn on runlite Agility plugin
Monitors:           - 4k or 3K display
bank settings:      - N/A
location:           - Al-Kharid end of agility course just south of silk stall
                    - Click compass, so it's at default north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
Menus:              - Inventory open
equip items:        - Lightest gear
items in inventory: - Stamina potions
items in bank:      - N/A
Setup:              - Right click compass and click North
                    - Set entity hider to hide player and NPCs
                    - Make sure low detail runelite plugin is turned off so roof is visible
                    - Disable Highlight Marks of Grace in Agility runelite plugin
Objects to mark:    - Sign on third rooftop: default magenta and border width 2

"""

import Common as Common
import Display

# Constants
runtime = 60

# region IMAGES
map_tree_images = ['Images/Agility/MapTrees.png']
map_agility_images = ['Images/Agility/AgilityIcon.png']
wall_images = ['Images/Agility/Wall.png']
tightrope_images = ['Images/Agility/Tightrope.png']
cable_images = ['Images/Agility/Cable.png']
tightrope_images2 = ['Images/Agility/Tightrope2.png']
sign_images = ['Images/Agility/Sign.png']
tree_images = ['Images/Agility/Tree.png']
beams_images = ['Images/Agility/Beams.png']
tightrope_images3 = ['Images/Agility/Tightrope3.png']
mark_of_grace_images = ['Images/Agility/MarkOfGrace.png']
gap_images = ['Images/Agility/Gap.png']
# endregion IMAGES


# Get how many from user
laps_needed_string = input("How many laps do you want? ")

laps_needed = int(laps_needed_string)

try:
    count = 0

    start_time = Display.start_timer()

    while True:
        Common.print_runtime(laps_needed, runtime, count)

        Common.watch_click_image(map_tree_images, 0.5, 'Click Map Trees',
                                 False, 6, 10, map_agility_images,
                                 Common.Minimap_region, Common.Minimap_region, 0.7)

        Common.watch_click_image(map_agility_images, 0.7, 'Click Map Agility Icon',
                                 False, 7, 10, wall_images,
                                 Common.Minimap_region, Common.Main_game_screen_region, 0.5)

        Common.watch_click_image(wall_images, 0.5, 'Click wall',
                                 False, 4, 10, tightrope_images,
                                 Common.Main_game_screen_region, Common.Bottom_half_game_screen_region, 0.5)

        Common.watch_click_image(tightrope_images, 0.5, 'Click tightrope 1', False, 10, 10,
                                 cable_images, Common.Bottom_half_game_screen_region,
                                 Common.Bottom_half_game_screen_region, 0.5)

        Common.watch_click_image(cable_images, 0.5, 'Click Cable till we see the sign',
                                 False, 7, 10,
                                 current_step_region=Common.Bottom_half_game_screen_region,
                                 next_step_image_paths=sign_images, next_step_confidence=0.7,
                                 next_step_region=Common.Main_game_screen_region)

        Common.watch_click_image(sign_images, 0.5, 'Click Sign till we see Tightrope 2',
                                 False, 4, 10,
                                 current_step_region=Common.Main_game_screen_region,
                                 next_step_image_paths=tightrope_images2, next_step_confidence=0.7,
                                 next_step_region=Common.Main_game_screen_region)

        Common.watch_click_image(tightrope_images2, 0.7, 'Click Tightrope 2',
                                 False, 14, 10, tree_images,
                                 Common.Main_game_screen_region, Common.Top_half_game_screen_region, 0.5)

        Common.watch_click_image(tree_images, 0.5, 'Click Tree',
                                 False, 6, 10, beams_images,
                                 Common.Top_half_game_screen_region, Common.Top_half_game_screen_region, 0.5)

        Common.watch_click_image(beams_images, 0.7, 'Click roof top beams',
                                 False, 4, 10, tightrope_images3,
                                 Common.Top_half_game_screen_region, Common.Top_half_game_screen_region, 0.5)

        Common.watch_click_image(tightrope_images3, 0.5, 'Click Tightrope 3',
                                 False, 13, 10, gap_images,
                                 Common.Top_half_game_screen_region, Common.Top_half_game_screen_region, 0.5)

        if Common.is_image_on_screen(mark_of_grace_images, 0.5, 0, 'Is there a mark of grace?',
                                     Common.Top_half_game_screen_region):
            Common.watch_click_image(mark_of_grace_images, 0.5, 'Click mark of grace',
                                     False, 3, 10, None,
                                     Common.Top_half_game_screen_region)

        Common.watch_click_image(gap_images, 0.5, 'Click gap',
                                 False, 4, 10, map_tree_images,
                                 Common.Top_half_game_screen_region, Common.Minimap_region, 0.5)

        if count >= laps_needed:
            break

        count += 1

        Display.stop_timer(start_time, laps_needed)


# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
