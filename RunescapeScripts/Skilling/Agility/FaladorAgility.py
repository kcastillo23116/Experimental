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
location:           - At end of Falador agility course. Southwest of agility icon
                        - World location Runelite plugin: 3029, 3333, 0
                    - Click compass, so it's at default north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
                    - Zoom minimap out all the way
Menus:              - Inventory closed
equip items:        - Lightest gear
items in inventory: - Stamina potions
items in bank:      - N/A
Setup:              - Right click compass and click North
                    - Set entity hider to hide player and NPCs
                    - Make sure low detail runelite plugin is turned off so roof is visible
                    - Disable Highlight Marks of Grace in Agility runelite plugin
Objects to mark:    - N/A

"""

import Common as Common
import Display

# Constants to update
is_agility_at_least_level_66 = True  # Used to skip failed obstacle checks since can't fail if at least level 66 agility

# region IMAGES
start1_images = ['Images/Agility/Falador/Start1.png']
tightrope1_images = ['Images/Agility/Falador/Tightrope1.png']
handhold_images = ['Images/Agility/Falador/Handhold.png']
agility_icon = ['Images/Agility/Falador/AgilityIcon1.png', 'Images/Agility/Falador/AgilityIcon2.png',
                'Images/Agility/Falador/AgilityIcon3.png']
gap1_images = ['Images/Agility/Falador/Gap1_3.png', 'Images/Agility/Falador/Gap1_1.png',
               'Images/Agility/Falador/Gap1_2.png']
gap2_images = ['Images/Agility/Falador/Gap2_1.png', 'Images/Agility/Falador/Gap2_2.png',
               'Images/Agility/Falador/Gap2_3.png']
tightrope2_images = ['Images/Agility/Falador/Tightrope2.png']
tightrope3_images = ['Images/Agility/Falador/Tightrope3.png']
gap3_images = ['Images/Agility/Falador/Gap3.png']
ledge1_images = ['Images/Agility/Falador/Ledge1_1.png', 'Images/Agility/Falador/Ledge1_2.png']
ledge2_images = ['Images/Agility/Falador/Ledge2_1.png', 'Images/Agility/Falador/Ledge2_2.png']
ledge3_images = ['Images/Agility/Falador/Ledge3.png']
ledge4_images = ['Images/Agility/Falador/Ledge4.png']
ledge5_images = ['Images/Agility/Falador/Ledge5.png']
start2_images = ['Images/Agility/Falador/Start2.png']
mark_of_grace_images = ['Images/Agility/Falador/MarkOfGrace.png']
# endregion IMAGES


def falador_agility():
    # Get how many from user
    laps_needed_string = input("How many laps do you want? ")

    laps_needed = int(laps_needed_string)

    try:
        count = 0

        start_time = Display.start_timer()

        while True:
            failable_tightrope2()

            Common.watch_click_image(tightrope3_images, 0.6, 'Click Tightrope3 while looking for Gap3',
                                     False, 5, 10, gap3_images,
                                     Common.Center_game_screen_region, Common.Center_game_screen_region, 0.6)

            Common.watch_click_image(gap3_images, 0.6, 'Click Gap3 while looking for Ledge1',
                                     False, 4, 10, ledge1_images,
                                     Common.Center_game_screen_region, Common.Center_game_screen_region, 0.6)

            # Only look at the building between Gap3 and Ledge1 since there can be other marks nearby that mess
            # things up if they're clicked on
            ledge1_building_region = (1714, 1196, 530, 348)
            check_for_mark_of_grace(region=ledge1_building_region)

            Common.watch_click_image(ledge1_images, 0.6, 'Click Ledge1 while looking for Ledge2',
                                     False, 4, 10,
                                     current_step_region=Common.Center_game_screen_region,
                                     next_step_image_paths=ledge2_images,next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.5)

            check_for_mark_of_grace(region=Common.Center_game_screen_region)

            Common.watch_click_image(ledge2_images, 0.5, 'Click Ledge2 while looking for Ledge3',
                                     False, 3, 10, ledge3_images,
                                     Common.Main_game_screen_region, Common.Main_game_screen_region, 0.6)

            Common.watch_click_image(ledge3_images, 0.6, 'Click Ledge3 while looking for Ledge4',
                                     False, 3, 10, ledge4_images,
                                     Common.Main_game_screen_region, Common.Main_game_screen_region, 0.5)

            check_for_mark_of_grace(region=Common.Center_game_screen_region)

            Common.watch_click_image(ledge4_images, 0.5, 'Click Ledge4 while looking for Ledge5',
                                     False, 4, 10, ledge5_images,
                                     Common.Main_game_screen_region, Common.Main_game_screen_region, 0.6)

            Common.watch_click_image(ledge5_images, 0.6,
                                     'Click Ledge5 while looking for Start2',
                                     False, 4, 10, start2_images,
                                     Common.Main_game_screen_region, Common.Main_game_screen_region, 0.6)

            if count >= laps_needed:
                break

            count += 1

            Display.stop_timer(start_time, laps_needed)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Run steps till failable Handholds obstacle and restart steps if it fails
def failable_handhold():
    Common.watch_click_image(start2_images, 0.6,
                             'Start2 while looking for Tightrope1',
                             False, 6, 10, tightrope1_images,
                             Common.Main_game_screen_region, Common.Main_game_screen_region, 0.6)

    # Common.watch_click_image(start1_images, 0.6, 'Click Start1 while looking for Tightrope1',
    #                          False, 4, 10, tightrope1_images,
    #                          Common.Center_game_screen_region, Common.Center_game_screen_region, 0.6)

    Common.watch_click_image(tightrope1_images, 0.7, 'Click Tightrope1 while looking for Handholds',
                             False, 8, 10, handhold_images,
                             Common.Main_game_screen_region, Common.Main_game_screen_region, 0.6)

    check_for_mark_of_grace(region=Common.Center_game_screen_region)

    # If agility is at least level 66 we can just do a regular click and check for next step
    # Otherwise we check if the obstacle failed and reset from start, since this obstacle can fail before 66 agility
    if is_agility_at_least_level_66:
        Common.watch_click_image(handhold_images, 0.6, 'Click Handholds and look for Gap1',
                                 False, 9, 10, current_step_region=Common.Main_game_screen_region,
                                 next_step_image_paths=gap1_images, next_step_region=Common.Center_game_screen_region,
                                 next_step_confidence=0.55)
    else:
        Common.watch_click_image(handhold_images, 0.6, 'Click Handholds',
                                 False, 9, 10, current_step_region=Common.Main_game_screen_region)

        if not Common.is_image_on_screen(gap1_images, 0.55, 0,
                                         'Checking for Gap 1 in case it failed and we need to reset',
                                         Common.Center_game_screen_region):
            failable_handhold()


# Run steps till failable tightrope2 obstacle and restart steps if it fails
def failable_tightrope2():
    failable_handhold()

    check_for_mark_of_grace(region=Common.Center_game_screen_region)

    Common.watch_click_image(gap1_images, 0.55, 'Click Gap1 while looking for Gap2',
                             False, 4, 10, current_step_region=Common.Center_game_screen_region,
                             next_step_image_paths=gap2_images, next_step_region=Common.Main_game_screen_region,
                             next_step_confidence=0.55)

    Common.watch_click_image(gap2_images, 0.55, 'Click Gap2 while looking for Tightrope2',
                             False, 4, 10, tightrope2_images,
                             Common.Center_game_screen_region, Common.Center_game_screen_region, 0.6)

    # If agility is at least level 66 we can just do a regular click and check for next step
    # Otherwise we check if the obstacle failed and reset from start, since this obstacle can fail before 66 agility
    if is_agility_at_least_level_66:
        Common.watch_click_image(tightrope2_images, 0.6, 'Click Tightrope2 while looking for tightrope 3',
                                 False, 9, 10, current_step_region=Common.Center_game_screen_region,
                                 next_step_image_paths=tightrope3_images, next_step_region=Common.Center_game_screen_region,
                                 next_step_confidence=0.6)
    else:
        # Can fail this obstacle before 66 agility
        Common.watch_click_image(tightrope2_images, 0.6, 'Click Tightrope2',
                                 False, 9, 10, current_step_region=Common.Center_game_screen_region)

        if not Common.is_image_on_screen(tightrope3_images, 0.7, 0,
                                         'Checking for Tightrope3 in case it failed and we need to reset',
                                         Common.Main_game_screen_region):
            failable_tightrope2()


def check_for_mark_of_grace(region=Common.Main_game_screen_region):
    Common.watch_click_image(mark_of_grace_images, 0.6, 'Click mark of grace if it is available',
                             False, 3, 10, current_step_region=region)


if __name__ == '__main__':
    falador_agility()
    print('Laps Done!')
