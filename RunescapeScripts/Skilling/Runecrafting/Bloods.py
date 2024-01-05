"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players, NPCs and player
                    - 117HD OFF and GPU ON
                    - Turn off XP globes runelite plugin
                    - Disable total XP bar by clicking the XP button at top left corner of Minimap
Monitors:           4k middle monitor with all three on
bank settings:      - N/A
location:           - Start at Dense essence rocks East of Arceuus library teleport
                    - Click compass, so it's at default north
                    - Hold up arrow to get camera all the way up
                    - Zoom all the way out
                    - Zoom minimap all the way out
Menus:              - Inventory menu open
equip items:        - Highest level pickaxe
                    - Full Graceful set
items in inventory: - Chisel
                    - Blood Essence
items in bank:      - N/A
Setup:           - Start at Dense essence rocks East of Arceuus library teleport
Objects to mark: - Marker Color and Fill Color default magenta (FFD400FF)
                    - Full opacity, highlight hull and clickbox
                 - Shortcut rocks
                 - Both Dense Runestone rocks
                 - Rockslide north of northern essence rock
                 - Rockslide east of northern essence rock
                 - Dark Altar
                 - Blood Altar
                 - Reference: "Images\Runecrafting\BloodRunes\MarkingReference.png"
                 - Inventory tag Runelite Plugin:
                    - Ouline and Fill enabled
                    - Fill Opacity: 50
                    - Dark essence marked with default magenta (D400FF)

"""

from time import sleep
import Common as Common
import Display

# Constants
runes_crafted_per_run = 196

runestone_images = ['Images/Runecrafting/BloodRunes/RuneStone3.png', 'Images/Runecrafting/BloodRunes/RuneStone4.png',
                    'Images/Runecrafting/BloodRunes/RuneStone1.png', 'Images/Runecrafting/BloodRunes/RuneStone2.png']
dense_essence_images = ['Images/Runecrafting/BloodRunes/DenseEssence.png']
rockslide1_images = ['Images/Runecrafting/BloodRunes/RockSlide1_1.png',
                     'Images/Runecrafting/BloodRunes/RockSlide1_2.png']
rockslide2_images = ['Images/Runecrafting/BloodRunes/RockSlide2.png']
rock_shortcut1_images = ['Images/Runecrafting/BloodRunes/RockShortcut1.png']
dark_altar_images = ['Images/Runecrafting/BloodRunes/DarkAltar.png']
chisel_images = ['Images/Runecrafting/BloodRunes/Chisel.png']
dark_essence_images = ['Images/Runecrafting/BloodRunes/DarkEssence.png']
max_fragments_images = ['Images/Runecrafting/BloodRunes/MaxFragments.png']
rock_shortcut2_images = ['Images/Runecrafting/BloodRunes/RockShortcut2.png']
blood_altar_images = ['Images/Runecrafting/BloodRunes/BloodAltar.png']
rock_shortcut3_images = ['Images/Runecrafting/BloodRunes/RockShortcut3_1.png',
                         'Images/Runecrafting/BloodRunes/RockShortcut3_2.png']

dark_altar_path_minimap = [3399, 226]
runestone_path_minimap = [3757, 295]
runestone_minimap = [3585, 359]
blood_altar_path_minimap = [3658, 423]
blood_altar_icon_minimap = [3487, 373]
rock_shortcut_3 = [2892, 110]
max_fragment_confirm = [779, 1944]


def prepare_dark_essence():
    # Keep mining essence till inventory is full
    while not Common.is_image_on_screen(dense_essence_images, 0.7, 0,
                                        'Check for dense essence in last inventory slot',
                                        Common.Inventory_last_slot_region):
        Common.watch_click_image(runestone_images, 0.7, 'Click a runestone to mine it',
                                 False, 15, 10, None,
                                 Common.All_game_screen_region)

    Common.watch_click_image(rockslide1_images, 0.7, 'Click rockslide and look for Rock Shortcut 1',
                             False, 11, 10,
                             current_step_region=Common.Main_game_screen_region,
                             next_step_image_paths=rock_shortcut1_images,
                             next_step_region=Common.Main_game_screen_region,
                             next_step_confidence=0.7)

    Common.watch_click_image(rock_shortcut1_images, 0.7, 'Click Rock Shortcut 1',
                             False, 5, 10,
                             current_step_region=Common.Main_game_screen_region)

    Common.move_mouse_and_left_click(dark_altar_path_minimap[0], dark_altar_path_minimap[1], 0,
                                     'Click minimap to walk toward dark altar')
    sleep(10)

    Common.watch_click_image(dark_altar_images, 0.7, 'Click Dark Altar till we see dark essence in inventory',
                             False, 9, 10,
                             current_step_region=Common.Main_game_screen_region,
                             next_step_image_paths=dark_essence_images, next_step_region=Common.Inventory_region,
                             next_step_confidence=0.8)


# Chisel all dark essence in inventory one by one so it's processed faster stop if no more essence in inventory
def chisel_dark_essence():

    while Common.is_image_on_screen(dark_essence_images, 0.7, 0,
                                    'Looking for dark essence in inventory to see if we need to keep chiseling it',
                                    Common.Inventory_region, False):
        Common.watch_click_image(chisel_images, 0.7, 'Click chisel in inventory',
                                 False, 1, 10,
                                 current_step_region=Common.Inventory_region)
        Common.watch_click_image(dark_essence_images, 0.7, 'Click dark essence in inventory',
                                 False, 1, 10,
                                 current_step_region=Common.Inventory_region)


def walk_back_to_runestones():
    Common.move_mouse_and_left_click(runestone_path_minimap[0], runestone_path_minimap[1], 0,
                                     'Click minimap to walk back to Rock Shortcut 2')
    sleep(1)

    chisel_dark_essence()

    # Keep looking for rock shortcut 2 so we don't go to next step before clicking it when our dark essence fragments
    # are maxed out earlier than expected
    Common.watch_click_image(rock_shortcut2_images, 0.7, 'Click Rock Shortcut 2 while looking for rockslide 2',
                             False, 3, 10,
                             current_step_region=Common.Main_game_screen_region,
                             next_step_image_paths=rockslide2_images, next_step_region=Common.Main_game_screen_region,
                             next_step_confidence=0.7)

    Common.move_mouse_and_left_click(runestone_minimap[0], runestone_minimap[1], 0,
                                     'Click minimap to walk to runestones')
    sleep(12)


def craft_blood_runes():
    # Get how many from user
    item_count_string = input("How many runes do you want to craft? ")

    # Calculate how many loops needed
    item_count = int(item_count_string)
    loops_till_done = round(item_count / runes_crafted_per_run)

    try:
        start_time = Display.start_timer()

        for x in range(loops_till_done):
            prepare_dark_essence()
            walk_back_to_runestones()
            prepare_dark_essence()

            Common.move_mouse_and_left_click(blood_altar_path_minimap[0], blood_altar_path_minimap[1], 0,
                                             'Click minimap to walk toward blood altar')
            sleep(52)

            Common.move_mouse_and_left_click(blood_altar_icon_minimap[0], blood_altar_icon_minimap[1], 0,
                                             'Click minimap to walk to blood altar')
            sleep(17)

            Common.watch_click_image(blood_altar_images, 0.7, 'Click Blood Altar',
                                     False, 2, 10,
                                     current_step_region=Common.Main_game_screen_region)

            chisel_dark_essence()

            Common.watch_click_image(blood_altar_images, 0.7, 'Click Blood Altar',
                                     False, 2, 10,
                                     current_step_region=Common.Main_game_screen_region)

            Common.watch_click_image(rock_shortcut3_images, 0.7,
                                     'Click Rock Shortcut 3 while looking for runestone mines',
                                     False, 19, 10,
                                     current_step_region=Common.All_game_screen_region,
                                     next_step_image_paths=runestone_images,
                                     next_step_region=Common.All_game_screen_region,
                                     next_step_confidence=0.7)

            Display.stop_timer(start_time, loops_till_done)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    craft_blood_runes()
