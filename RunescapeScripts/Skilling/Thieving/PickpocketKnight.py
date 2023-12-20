"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn off entity hider in runelite to hide other players, NPCs and hide local player
                    - Turn off ground items in runelite plugins
                    - 117HD OFF and GPU ON
                    - Turn off runelite Mouse Tooltips plugin
                    - Turn off runelite Regeneration meter plugin
                    - Collapse chat window
Monitors:           - 4k or 3K display
bank settings:      - Withdraw As: Item
                    - Quantity: X and withdraw 26 to leave space for gold and coin pouches
location:           - East Ardougne North Eastern building
                    - Move camera so knight blob is visible directly through window and compass is pointing west:
                      refer to images here:
                        - "Images\Thieving\Pickpocketing\CameraPosition.png",
                    - Right click compass and select: Look East
                    - Zoom in all the way
                    - Hold down arrow key to tilt camera all the way down
                    - Zoom minimap all the way out
Menus:              - Inventory menu open
equip items:        - Regen bracelet to heal damage over time a bit faster
items in inventory: - Sharks to heal
items in bank:      - Sharks in feather tab
Setup:              - Mark just the knight you're pickpocketing with cyan fill and outline so he's easy to spot on the map
                      between different worlds
                    - Get south-eastern most knight into northeastern building so it stays at bottom of room.
                      Can do by getting in front of door and right click walking over the knight till it swaps places
                      with you and is in doorway then use dragon spear special twice to push into room then close the door
                        - Helpful video: https://www.youtube.com/watch?v=EyCx8I6qUSc
                        - Roof Removal runelite plugin helps make this easier
                    - Setup runelite menu entry swapper to left-click pickpocket
                    - Enable runelite pickpocket guardian plugin to make sure don't die
                    - Get pickpocket helper runelite plugin and turn on hide others so other NPCs and players are
                      hidden while showing knight
                    - Can also turn on despawn timer to see how often knight needs to move before despawning
Objects to mark:    - South Eastern most Knight of Ardougnge: Fill and Highlight color: cyan: FF00FFFF highlight hull and outline
"""
from time import sleep
import Common as Common
import Display
import Banking

# Click bottom left corner of stall so don't run to other spot when clicking empty stall on accident
food_images = ['Images/Thieving/Pickpocketing/Shark.png']
max_coin_purse_images = ['Images/Thieving/Pickpocketing/MaxCoinPurse.png']
open_door_option_images = ['Images/Thieving/Pickpocketing/OpenDoorOption.png']
bank_booth_images = ['Images/Thieving/Pickpocketing/BankBooth.png']
feather_tab_images = ['Images/Fletching/FeatherTab.png']


def pickpocket_knight():
    try:
        # Get how many from user
        item_count_string = input("How many items do you want to steal? ")
        item_count = int(item_count_string)

        start_time = Display.start_timer()

        for x in range(item_count):
            Common.move_mouse_and_click_in_region(2700, 850, 150, 100, 0, False,
                                                  'Steal from knight')

            # Use sleep here to get decimal seconds for more precision
            sleep(0.75)

            # Check if HP is low every specified number of pickpocket attempts
            if x % 3 == 0:
                # if hp is low heal
                if Common.is_hp_low():
                    Common.watch_click_image(food_images, 0.7, 'Eat food to heal',
                                             False, 1, 10,
                                             current_step_region=Common.Inventory_region)

            # Check if maxed out on coin purses
            if x % 2 == 0:
                Common.watch_click_image(max_coin_purse_images, 0.9, 'Get gold from coin purses',
                                         False, 1, 10,
                                         current_step_region=Common.Inventory_region)

            # If no more food in inventory go to bank to get more and go back to room with knight
            if not Common.is_image_on_screen(food_images, 0.7, 0,
                                             'Check if food in inventory', Common.Inventory_region):
                # Right click door and open it if it's not open
                Common.move_mouse_and_click_in_region(1684, 1357, 614, 434, 0,
                                                      True, 'Right click door to check if it is open and get out')
                if Common.is_image_on_screen(open_door_option_images, 0.7, 0,
                                             'Check if open door option is available'):
                    Common.watch_click_image(open_door_option_images, 0.95, 'Click open door option',
                                             False, 2, 10,
                                             current_step_region=Common.All_game_screen_region)

                # Go to bank to get more food
                Common.move_mouse_and_left_click(3733, 337, 1, 'Go to bank on minimap')
                sleep(19)
                Common.move_mouse_and_click_in_region(1557, 303, 691, 793, 0, False,
                                                      'Click bank booth')
                sleep(1)
                Common.watch_click_image(feather_tab_images, 0.7,
                                         'Click on white feather tab and look for food in bank window',
                                         False, 1, 10, food_images,
                                         current_step_region=Common.Top_half_game_screen_region,
                                         next_step_region=Common.Bank_region, next_step_confidence=0.6)
                Common.watch_click_image(food_images, 0.7, 'Withdraw food',
                                         False, 1, 10,
                                         current_step_region=Common.Bank_region)
                Banking.close_bank()

                # Go back to knight on mini map
                Common.move_mouse_and_left_click(3415, 184, 0, 'Go back to knight building door on minimap')
                sleep(19)
                Common.move_mouse_and_click_in_region(1642, 483, 617, 357, True,
                                                      'Right click door to check if it is open to get in')
                # Open door if it's not open
                if Common.is_image_on_screen(open_door_option_images, 0.7, 0,
                                             'Check if open door option is available'):
                    Common.watch_click_image(open_door_option_images, 0.95, 'Click open door option',
                                             False, 1, 10,
                                             current_step_region=Common.All_game_screen_region)

                    # Stop timer here since going back to knight after getting more food the last thing that happens
                    # Use current number of clicks to determine how many more iterations are needed
                    iterations_till_done = round(item_count * x)
                    Display.stop_timer(start_time, iterations_till_done)

                Common.move_mouse_and_click_in_region(2629, 90, 272, 171, 0,
                                                      False, 'Click in window to pickpocket knight and go inside')

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    pickpocket_knight()
    print("Stealing done!")
