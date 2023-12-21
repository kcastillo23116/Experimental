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
items in inventory: - None
items in bank:      - Sharks in feather tab
Setup:              - Mark just the knight you're pickpocketing with cyan fill and outline so he's easy to spot on the map
                      between different worlds
                    - Get south-eastern most knight into northeastern building so it stays at bottom of room.
                      Can do by getting in front of door and right click walking over the knight till it swaps places
                      with you and is in doorway then use dragon spear special twice to push into room then close the door
                        - Helpful video: https://www.youtube.com/watch?v=EyCx8I6qUSc
                        - Roof Removal runelite plugin helps make this easier
                    - Lead other NPCs out of room
                    - Setup runelite menu entry swapper to left-click pickpocket
                    - Enable runelite pickpocket guardian plugin to make sure don't die
                    - Get pickpocket helper runelite plugin and turn on hide others so other NPCs and players are
                      hidden while showing knight
                    - Can also turn on despawn timer to see how often knight needs to move before despawning
Objects to mark:    - South Eastern most Knight of Ardougnge: Fill and Highlight color: cyan: FF00FFFF highlight hull and outline
"""
import timeit
from time import sleep
import Common as Common
import Display
import Banking

# Click bottom left corner of stall so don't run to other spot when clicking empty stall on accident
food_images = ['Images/Thieving/Pickpocketing/SharkBank.png', 'Images/Thieving/Pickpocketing/SharkInventory.png']
max_coin_purse_images = ['Images/Thieving/Pickpocketing/MaxCoinPurse.png']
open_door_option_images = ['Images/Thieving/Pickpocketing/OpenDoorOption.png']
bank_booth_images = ['Images/Thieving/Pickpocketing/BankBooth.png']
feather_tab_images = ['Images/Fletching/FeatherTab.png']
knight_blob_images = ['Images/Thieving/Pickpocketing/KnightBlob1.png', 'Images/Thieving/Pickpocketing/KnightBlob2.png',
                      'Images/Thieving/Pickpocketing/Window.png']


def pickpocket_knight():
    try:
        # Get how many from user
        item_count_string = input("How many items do you want to steal? ")
        item_count = int(item_count_string)

        # Adjust number of attempts for success rate. Use this calculator to determine:
        # https://oldschool.runescape.wiki/w/User:MxFox/Sandbox/Calculator:Thieving/Pickpocket_rates
        pickpocket_attempts_needed = round(item_count * 1.6)

        display_countdown(pickpocket_attempts_needed)

        for x in range(pickpocket_attempts_needed):
            Common.move_mouse_and_click_in_region(2700, 850, 150, 100, 0, False,
                                                  'Steal from knight')

            # Wait four seconds after first pickpocket attempt in case of fail and stun don't want next steps to get
            # locked up because character is stunned
            if x == 0:
                sleep(4)

            # Use sleep here to get decimal seconds for more precision
            sleep(0.75)

            # Check if maxed out on coin purses
            if x % 2 == 0:
                Common.watch_click_image(max_coin_purse_images, 0.9, 'Get gold from coin purses',
                                         False, 1, 10,
                                         current_step_region=Common.Inventory_region)

            # If no more food in inventory go to bank to get more and go back to room with knight
            if not Common.is_image_on_screen(food_images, 0.6, 0,
                                             'Check if food in inventory', Common.Inventory_region):
                door_opened = False

                open_door_attempts = 0
                # Keep right-clicking door till open option is visible
                while not Common.is_image_on_screen(open_door_option_images, 0.95, 0,
                                                    'Check if open door option is available'):
                    Common.move_mouse_and_click_in_region(1684, 1357, 614, 434, 0,
                                                          True, 'Right click door to check if it is open and get out')
                    open_door_attempts += 1

                door_opened = Common.watch_click_image(open_door_option_images, 0.95, 'Click open door option',
                                                       False, 2, 10,
                                                       current_step_region=Common.All_game_screen_region)

                # Use minimap coordinates to bank from door if we opened the door otherwise use coordinates from knight
                if door_opened:
                    # Go to bank to get more food using coordinates from door
                    Common.move_mouse_and_left_click(3736, 327, 1, 'Go to bank on minimap from door')
                else:
                    # Go to bank to get more food using coordinates from knight
                    Common.move_mouse_and_left_click(3730, 334, 1, 'Go to bank on minimap from knight')

                sleep(20)
                Common.move_mouse_and_click_in_region(1557, 303, 691, 793, 0, False,
                                                      'Click bank booth')
                sleep(1)
                Common.watch_click_image(feather_tab_images, 0.7,
                                         'Click on white feather tab and look for food in bank window',
                                         False, 1, 10, food_images,
                                         current_step_region=Common.Top_half_game_screen_region,
                                         next_step_region=Common.Bank_region, next_step_confidence=0.6)
                Common.watch_click_image(food_images, 0.7, 'Withdraw food and make sure it is in inventory',
                                         False, 1, 10,
                                         current_step_region=Common.Bank_region,
                                         next_step_image_paths=food_images, next_step_confidence=0.6,
                                         next_step_region=Common.Inventory_region)

                # Go back to knight on mini map
                Common.move_mouse_and_left_click(3415, 187, 0,
                                                 'Go back to knight building door on minimap')
                sleep(20)
                Common.move_mouse_and_click_in_region(1642, 483, 617, 357, True,
                                                      'Right click door to check if it is open to get in')
                # Open door if it's not open
                if Common.is_image_on_screen(open_door_option_images, 0.7, 0,
                                             'Check if open door option is available'):
                    Common.watch_click_image(open_door_option_images, 0.95,
                                             'Click open door option and look for knight blob or window on screen',
                                             False, 1, 10,
                                             current_step_region=Common.All_game_screen_region,
                                             next_step_image_paths=knight_blob_images, next_step_confidence=0.6,
                                             next_step_region=Common.All_game_screen_region)

                Common.move_mouse_and_left_click(2585, 60, 0,
                                                 'Click in window to pickpocket knight and go inside')

            # Check if HP is low every specified number of pickpocket attempts
            if x % 3 == 0:
                # if hp is low heal
                if Common.is_hp_low():
                    Common.watch_click_image(food_images, 0.7, 'Eat food to heal',
                                             False, 1, 10,
                                             current_step_region=Common.Inventory_region)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


def display_countdown(pickpocket_attempts_needed):
    # Runtime constants
    pick_pocket_attempt_seconds = 2
    bank_roundtrip_seconds = 45
    food_healing = 20  # healing per shark

    # Figure out how many fails needed before bank trip based on healing and damage taken per failed attempt
    food_total_healing = food_healing * 26  # have 26 inventory slots for food
    fails_before_bank_trip = food_total_healing / 3  # take three damage per failed attempt

    # Calculate total runtime in seconds
    total_bank_trips = pickpocket_attempts_needed / fails_before_bank_trip
    total_bank_runtime = total_bank_trips * bank_roundtrip_seconds
    total_runtime_seconds = (pickpocket_attempts_needed * pick_pocket_attempt_seconds) + total_bank_runtime

    Display.start_timer_thread_total_time(total_runtime_seconds)


if __name__ == '__main__':
    pickpocket_knight()
    print("Stealing done!")
