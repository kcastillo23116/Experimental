"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn off entity hider in runelite
                    - 117HD OFF and GPU ON
                    - Set Object Markers:
                      - Border width to 6
                      - Marker colors:
                        - FFD400FF for log storage (purple)
                        - FF00FFDD for all object (cyan)
                      - Highlight clickbox enabled with all others disabled
                      - Remember color per object
                    - GPU plugin draw distance set to 66
                    - Camera plugin: disabled
                    - Runelite Mouse tooltips and Item stats plugins off so hovering over items doesn't mess things up
                    - Turn on XP Globe plugin to see how much xp getting per hour
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Nightmare zone custom hard rumble. Southern spawn position
                    - Right Click compass and face north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
                    - Zoom minimap all the way out
Menus:              - Inventory menu Open
                    - Set  auto retaliate on and select attack mode for skill to train
equip items:        - Best gear from this page:
                        - https://oldschool.runescape.wiki/w/Nightmare_Zone/Strategies#Melee_(Prayer)
items in inventory: - 23 Prayer potions
                    - 5 Overload Potions
items in bank:      - Prayer potions
                    - Overload Potions (In nightmare zone barrel)
Setup:           - Nightmare zone hard rumble with recommend enemies and gear from this page:
                    - https://oldschool.runescape.wiki/w/Nightmare_Zone/Strategies#Melee_(Prayer)
                 - Mark following inventory items using Inventory Tags runelite plugin:
                    - Prayer Potions 1-4: Blue
                    - Overload Potions 1-4: Red
                - Drop a million gold or more in nightmare zone coffer
                - Disable overload potion notification in runelite nightmare zone plugin
Objects to mark: - Enable Highlight hull and Highlight clickbox
                 - Marker color to default magenta (FFD400FF)
                 - Border width: 6
                 - N/A
"""
import timeit
import Common as Common
import Display

# Constants
# Use numbers from this calculator to determine how many seconds prayer pot lasts.
# Be sure to include prayer bonus stat from gear
# https://oldschool.runescape.wiki/w/Calculator:Prayer/Prayer_drain
prayer_potion_dose_duration_seconds = 81
overload_potion_dose_duration_seconds = 300  # Lasts 5 minutes

prayer_potion_images = ['Images/Combat/PrayerPotion3.png', 'Images/Combat/PrayerPotion2.png',
                        'Images/Combat/PrayerPotion1.png']
overload_potion_images = ['Images/Combat/OverloadPotion3.png', 'Images/Combat/OverloadPotion2.png',
                          'Images/Combat/OverloadPotion1.png']

quick_prayer_icon = [3338, 292]


def nightmare_combat_training():
    try:
        # Get how many from user
        item_count_string = input("How many prayer pots do you have? ")

        # Calculate how long all prayer pots will last
        item_count = int(item_count_string)

        # Number of four dose prayer potions Multiplied by seconds of prayer per dose then
        # Multiplied four since each potion has four doses
        total_prayer_potion_seconds = round(item_count * prayer_potion_dose_duration_seconds * 4)

        # Display countdown timer
        Display.start_timer_thread_total_time(total_prayer_potion_seconds)

        start = timeit.default_timer()

        Common.watch_click_image(overload_potion_images, 0.7, 'Click first overload potion',
                                 sleep_time_after_click=0,
                                 current_step_region=Common.Inventory_region)
        overload_potion_start_time = timeit.default_timer()

        while True:
            Common.watch_click_image(prayer_potion_images, 0.7, 'Click prayer potion',
                                     sleep_time_after_click=prayer_potion_dose_duration_seconds,
                                     current_step_region=Common.Inventory_region)

            # Calculate elapsed seconds using start time
            elapsed_seconds = timeit.default_timer() - start

            # Drink overload potion if dose has run out
            elapsed_seconds_since_overload_potion = timeit.default_timer() - overload_potion_start_time
            if elapsed_seconds_since_overload_potion >= overload_potion_dose_duration_seconds:
                Common.watch_click_image(overload_potion_images, 0.7, 'Click overload potion after 5 minutes',
                                         sleep_time_after_click=0,
                                         current_step_region=Common.Inventory_region)

            # If time elapsed is greater than total prayer pots break out of loop and stop script
            if elapsed_seconds > total_prayer_potion_seconds:
                print('Out of prayer pots!')
                break

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    nightmare_combat_training()
    print('Done training combat!')
