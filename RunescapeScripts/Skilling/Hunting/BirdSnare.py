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
location:           - Piscatoris teleport south at flowers near fence
                        - Stand one tile left of the flowers by fence. Reference picture:
                          "Images\Hunting\StartingLocationReference.png"
Menus:              - Inventory open
equip items:        - N/A
items in inventory: - 8 Bird snares
items in bank:      - N/A
Setup:              - Right click compass and click Look North
                    - Zoom out a bit so all traps are visible in the middle of the screen when standing four tiles west
                      of flowers: "Images\Hunting\ZoomReference.png"
                    - Entity hider to hide player and other players/npc
                    - Disable runelite hunter plugin so timers don't block broken trap poles
                    - Use runelite hunter plugin to set zero opacity on Open trap and Transitioning trap
                    - Use runelite menu entry swapper plugin to reassign shift click to Walk Here for
                      successful and failed traps
                    - Use runelite ground item plugin to hide ground item names and text and put bird snares at top
                        - Add Bird snare to Highlighted Items section and check show highlighted items only and
                          de-prioritize menu hidden items and add Bones and Raw bird meat to Hidden Items section
                    - Use Runelite Random Event Hider plugin and hide all player and other's random event NPCs
Objects to mark:    - Failed bird snare traps with following settings:
                      Note: To get object marker to fill have to set stuff below and THEN toggle the markers
                      Note: Have to mark each successful and failed snare traps individually. So set them down till they fail and
                            mark each till all in inventory are marked then do same for success
                        - Highlight hull
                        - Highlight clickbox
                        - Border width 2
                        - Marker color and Fill colors:
                            - Success and fail: Defualt magenta (FFD400FF) and max opacity
"""

from time import sleep
import pyautogui
import Common as Common
import Display

# Constants
runtime = 1

# region IMAGES
bird_snare_inventory_images = ['Images/Hunting/BirdSnareInventory.png']
bird_snare_status_images = ['Images/Hunting/BirdSnareSuccess.png', 'Images/Hunting/BirdSnareFail.png',
                            'Images/Hunting/BirdSnareBreak.png', 'Images/Hunting/BirdSnareBreak2.png']
items_to_drop_images = ['Images/Hunting/Bones.png', 'Images/Hunting/BirdMeat.png']
walk_here_option_images = ['Images/General/WalkHereOption.png']
empty_inv_images = ['Images/Woodcutting/EmptyInvSlot.png']
# endregion IMAGES

# Straight line through middle of screen used to see line of traps when zoomed all the way in
# Encompasses two rows of tiles in the middle all the way across screen
middle_bar_region = (0, 556, 3773, 854)


def bird_snare():
    try:
        # Constants
        max_traps = 3

        # Get how many from user
        bird_count_string = input("How many birds do you want to catch? ")

        # Calculate attempts needed using 50% success rate
        bird_count = int(bird_count_string)
        attempts_needed = round(bird_count * 1.6)

        # Set up max number of traps to start
        for x in range(max_traps):
            Common.watch_click_image(bird_snare_inventory_images, 0.7,
                                     'Click inventory trap to set up first trap',
                                     False, 4, 10,
                                     current_step_region=Common.Inventory_region)

        start_time = Display.start_timer()

        for x in range(attempts_needed):
            # Hold down shift to walk on top of traps instead of dismantling them
            pyautogui.keyDown('shift')

            # Keep looking for successful or failed traps till one is clicked
            while True:
                is_clicked = Common.watch_click_image(bird_snare_status_images, 0.6,
                                                      'Looking for  successful trap then shift clicking to walk on top of it',
                                                      False, 0, 10,
                                                      current_step_region=middle_bar_region,
                                                      current_step_grayscale=False, double_click=True)

                # Break if trap was clicked so we can do next steps to pick it up and set new trap
                if is_clicked:
                    # Drop specified items while walking to other trap
                    Common.drop_inventory_items(items_to_drop_images, grayscale=True)
                    sleep(1.5)

                    # Sleep longer on first pass since won't have items to drop and buffer time to run to next trap
                    if x == 0:
                        sleep(2)
                    break

            pyautogui.keyUp('shift')

            # Left center of the screen since standing on top of trap at this point
            Common.move_mouse_and_left_click(1917, 1133, 0, 'Click trap to dismantle it')
            sleep(1.9)

            Common.watch_click_image(bird_snare_inventory_images, 0.7,
                                     'Click trap in inventory to set it up',
                                     False, 0, 10,
                                     current_step_region=Common.Inventory_region)
            sleep(2.5)

            Display.stop_timer(start_time, attempts_needed)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    bird_snare()
