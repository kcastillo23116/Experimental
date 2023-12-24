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
location:           - House teleport spot using tablet
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - Noted planks
                    - Steel nails
                    - Gold coins
                    - Hammer
                    - Saw
                    - Three more items to fill in leftover inventory slots so there aren't unused planks
                        - So we can tell when planks successfully converted from notes
items in bank:      - N/A
Setup:              - Right click compass and click Look South
                    - Zoom out all the way
                    - Entity hider to hide players
                    - Use runelite menu entry swapper plugin to reassign portal left click to build mode
                    - Use Runelite Random Event Hider plugin and hide all player and other's random event NPCs
                    - Make sure bookshelf is removed before starting
Objects to mark:    - Portal in
                    - Portal out
                    - Phials NPC
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

# Constants
seconds_to_build = 6

# region IMAGES
bookshelf_images = ['Images/Construction/BookShelf1.png', 'Images/Construction/BookShelf2.png']
build_option_images = ['Images/Construction/BuildOption.png', 'Images/Construction/RemoveOption.png']
portal_out_images = ['Images/Construction/PortalOut.png']
noted_planks_images = ['Images/Construction/NotedPlank.png']
plank_images = ['Images/Construction/Plank.png']
phials_images = ['Images/Construction/Phials.png']
portal_in_images = ['Images/Construction/PortalIn.png']
exchange_all_images = ['Images/Construction/ExchangeAll.png']
# endregion IMAGES


def build_bookshelves():
    try:
        # Get how many from user
        builds_needed_string = input("How many  do you want to build? ")

        # Divide by four since we get four bookshelves built per inventory of planks
        build_count = int(builds_needed_string)
        iterations_needed = round(build_count/5)

        start_time = Display.start_timer()
        for x in range(iterations_needed):
            Common.watch_click_image(portal_out_images, 0.6,
                                     'Looking for portal out and clicking it',
                                     False, 5, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     current_step_grayscale=False, double_click=False)

            # Keep trying to click on Phail till we see the Exchange all option
            while True:
                Common.watch_click_image(noted_planks_images, 0.6,
                                         'Looking noted planks in inventory and clicking them',
                                         False, 1, 10,
                                         current_step_region=Common.Inventory_region,
                                         current_step_grayscale=False, double_click=False)

                Common.watch_click_image(phials_images, 0.6,
                                         'Looking for phials and clicking him',
                                         False, 6, 10,
                                         current_step_region=Common.Main_game_screen_region,
                                         current_step_grayscale=False, double_click=False)

                # If exchange all option is visible good to stop looking for Phail and move on
                if Common.is_image_on_screen(exchange_all_images, 0.6, 0,
                                             'Checking for Exchange All option in chatbox', Common.Chatbox_region):
                    break

            # Press three to get un-noted planks from Phials
            pyautogui.keyDown('3')
            pyautogui.keyUp('3')
            sleep(1)

            Common.watch_click_image(portal_in_images, 0.6,
                                     'Looking for portal and click it to go back in',
                                     False, 6, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     current_step_grayscale=False, double_click=False)

            Common.move_mouse_and_right_click(2125, 1298, 0,
                                              'Right clicking bookshelf space from portal')

            Common.watch_click_image(build_option_images, 0.9,
                                     'Clicking the build option',
                                     False, 3, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     current_step_grayscale=False, double_click=False)

            # Press one to build the bookcase
            pyautogui.keyDown('1')
            pyautogui.keyUp('1')
            sleep(seconds_to_build)

            # Build 4 more bookcases before needing to resupply planks
            for y in range(5):
                Common.move_mouse_and_right_click(1973, 1055, 0,
                                                  'Right clicking built bookshelf from inside house')

                Common.watch_click_image(build_option_images, 0.9,
                                         'Clicking the build option',
                                         False, 1, 10,
                                         current_step_region=Common.Main_game_screen_region,
                                         current_step_grayscale=False, double_click=False)

                # Press one to build the bookcase
                pyautogui.keyDown('1')
                pyautogui.keyUp('1')
                sleep(seconds_to_build)

                Common.move_mouse_and_right_click(1972, 1061, 0,
                                                  'Right clicking bookshelf space from inside house')

                Common.watch_click_image(build_option_images, 0.9,
                                         'Clicking the remove option',
                                         False, 1, 10,
                                         current_step_region=Common.Main_game_screen_region,
                                         current_step_grayscale=False, double_click=False)

                # Press one to remove the bookcase
                pyautogui.keyDown('1')
                pyautogui.keyUp('1')
                sleep(3)

            Display.stop_timer(start_time, iterations_needed)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    build_bookshelves()
