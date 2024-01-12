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
Monitors:           - 4k or 3K display
bank settings:      - N/A
location:           - In front of oak larder
                        - Reference: Images\Construction\LarderLocationReference.png
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - Gold coins
                    - Hammer
                    - Saw
items in bank:      - Oak planks
Setup:              - Right click compass and click Look South
                    - Make sure runelite camera plugin is disabled
                    - Zoom out all the way
                    - Entity hider to hide players
                    - Use bell to withdraw 24 oak planks from butler so bell is set up with option
                    - Make sure larder is removed before starting
                    - Make sure larder is in southern build spot rotated so it's at bottom right and bell pull is next
                      door at top left
                        - Reference: Images\Construction\LarderLocationReference.png
Objects to mark:    - Rope Bell pull
                    - TAG ALL Demon butler so it doesn't get untagged when coming back and forth
                    - Empty Larder space
                    - Object Marker plugin settings:
                        - Note: To get object marker to fill have to set stuff below and THEN toggle the markers
                        - Highlight hull
                        - Highlight clickbox
                        - Border width 2
                        - Default magenta (FFD400FF) and max opacity
                    - NPC Indicators plugin settings:
                        - Highlight hull
                        - highlight outline
                        - Default Cyan color (FF00FFFF)
"""

from time import sleep
import pyautogui
import Common as Common
import Display

# Constants to update depending on what's being built
build_key = '2'
seconds_to_build = 3
planks_per_build = 8
open_inventory_slots = 24

# region IMAGES
bell_images = ['Images/Construction/OakLarderWithButler/Bell.png']
build_option_images = ['Images/Construction/BuildOption.png', 'Images/Construction/RemoveOption.png']
butler_pay_images = ['Images/Construction/OakLarderWithButler/ButlerPay.png']
# endregion IMAGES

larder_coords1 = [2332, 1439]
larder_coords2 = [1983, 1072]


def build_larders_with_butler():
    try:
        # Get how many from user
        total_planks_string = input("How many planks do you have? ")

        # Calculate number of iterations needed to use all user specified materials
        total_planks = int(total_planks_string)
        builds_per_inventory = round(open_inventory_slots/planks_per_build)
        iterations_needed = round((total_planks/planks_per_build) / builds_per_inventory)

        start_time = Display.start_timer()
        for x in range(iterations_needed):
            Common.watch_click_image(bell_images, 0.6,
                                     'Clicking bell',
                                     False, 5, 10,
                                     current_step_region=Common.Main_game_screen_region)

            pyautogui.press('1')
            print('Press 1 to get planks from butler')
            sleep(0.5)

            Common.move_mouse_and_left_click(larder_coords1[0], larder_coords1[1], 0,
                                             'Moving to larder from bell and waiting for demon butler to get back')
            sleep(7.5)  # Demon butler takes 7 seconds to return

            butler_needs_pay = Common.is_image_on_screen(butler_pay_images, 0.8, 0,
                                                         'Check if butler needs pay', Common.Chatbox_region)
            if butler_needs_pay:
                pyautogui.press('space')
                sleep(0.5)
                pyautogui.press('1')
                sleep(0.5)
                pyautogui.press('space')
                sleep(0.5)

            # Build all larders before resupplying noted materials
            for y in range(builds_per_inventory):
                Common.move_mouse_and_right_click(larder_coords2[0], larder_coords2[1], 0,
                                                  'Right clicking larder 1')
                sleep(0.5)

                Common.watch_click_image(build_option_images, 0.9,
                                         'Clicking the build option',
                                         False, 1, 10,
                                         current_step_region=Common.Main_game_screen_region,
                                         current_step_grayscale=False, double_click=False)

                # Press one to build the larder
                pyautogui.press(build_key)
                sleep(seconds_to_build)

                Common.move_mouse_and_right_click(larder_coords2[0], larder_coords2[1], 0,
                                                  'Right clicking larder 2')
                sleep(0.5)

                Common.watch_click_image(build_option_images, 0.9,
                                         'Clicking the remove option',
                                         False, 1, 10,
                                         current_step_region=Common.Main_game_screen_region,
                                         current_step_grayscale=False, double_click=False)

                # Press one to remove the larder
                pyautogui.press('1')
                sleep(3)

            Display.stop_timer(start_time, iterations_needed)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    build_larders_with_butler()
