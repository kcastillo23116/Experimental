"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - 117HD OFF and GPU ON
                    - Turn off runelite Mouse Tooltips plugin
                    - Use Runelite Random Event Hider plugin and hide all player and other's random event NPCs
Monitors:           - 4k or 3K display
bank settings:      - N/A
location:           - Camelot teleport on a PVP world
Menus:              - Inventory open
equip items:        - Dust staff
                    - Boots of lightness
                    - NO Graceful set or other items that can be lost on PVP world
items in inventory: - Law runes
                    - Tinderbox
items in bank:      - Bones
                    - Marrentill herb
Setup:              - Right click compass and click Look North
                    - Make sure runelite camera plugin is disabled
                    - Zoom out all the way
                    - Entity hider to hide players
                    - Set spellbook filters to only show teleport spells. All other filters disabled
                    - Use runelite menu entry swapper plugin to swap left click for:
                        - Marrentill herb: Withdraw 2
                        - Bones: Use
Objects to mark:    - Camelot teleport Bank chest on a PVP world: Magenta (FFD400FF)
                    - Altar: Magenta (FFD400FF)
                    - Bottom Incense burner: Green (FF3AFF00)
                    - Top Incense burner: Blue (FF0043FF)
                    - Reference: Images\Prayer\MarkedObjectReference.png
                    - Object Marker plugin settings:
                        - Note: To get object marker to fill have to set stuff below and THEN toggle the markers
                        - Highlight clickbox
                        - Border width 2
                        - Default magenta (FFD400FF) and max opacity
"""

from time import sleep
import pyautogui

import Banking
import Common as Common
import Display

bones_per_run = 26

# region IMAGES
bank_images = ['Images/Prayer/Bank.png']
pizza_tab_images = ['Images/Prayer/PizzaTab.png']
herb_images = ['Images/Prayer/Herb.png']
bones_images = ['Images/Prayer/Bones.png']
spell_book_images = ['Images/Prayer/SpellBook.png']
house_teleport_images = ['Images/Prayer/HouseTeleport.png']
burner1_images = ['Images/Prayer/Burner1.png']
burner2_images = ['Images/Prayer/Burner2.png']
altar_images = ['Images/Prayer/Altar.png']
camelot_teleport_images = ['Images/Prayer/CamelotTeleport.png']
# endregion IMAGES


def offer_bones():
    try:
        # Get how many from user
        total_bones_string = input("How many bones do you have? ")

        # Calculate number of iterations needed
        total_bones = int(total_bones_string)
        iterations_needed = round(total_bones / bones_per_run)

        start_time = Display.start_timer()
        for x in range(iterations_needed):
            Common.watch_click_image(bank_images, 0.7,
                                     'Click bank while looking for bank options',
                                     False, 3, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     next_step_image_paths=Banking.bank_withdraw_note_images,
                                     next_step_region=Common.Bank_bottom_options_region,
                                     next_step_confidence=0.5)

            # Only change bank tabs on the first iteration since banks stays on tab
            if x == 0:
                Common.watch_click_image(pizza_tab_images, 0.7,
                                         'Click pizza bank tab while looking for bones',
                                         False, 2, 10,
                                         current_step_region=Common.Top_half_game_screen_region,
                                         next_step_image_paths=bones_images,
                                         next_step_region=Common.Bank_region,
                                         next_step_confidence=0.7)

            Common.watch_click_image(herb_images, 0.7,
                                     'Click herb while looking for herbs in inventory',
                                     False, 1, 10,
                                     current_step_region=Common.Bank_region,
                                     next_step_image_paths=herb_images,
                                     next_step_region=Common.Inventory_region,
                                     next_step_confidence=0.7)

            Common.watch_click_image(bones_images, 0.7,
                                     'Click bones while looking for bones in inventory',
                                     False, 1, 10,
                                     current_step_region=Common.Bank_region,
                                     next_step_image_paths=bones_images,
                                     next_step_region=Common.Inventory_region,
                                     next_step_confidence=0.7)

            Banking.close_bank()

            Common.watch_click_image(spell_book_images, 0.7,
                                     'Click spellbook tab while looking for house teleport spell',
                                     False, 1, 10,
                                     current_step_region=Common.Inventory_bar_region,
                                     next_step_image_paths=house_teleport_images,
                                     next_step_region=Common.Inventory_region,
                                     next_step_confidence=0.7)

            Common.watch_click_image(house_teleport_images, 0.9,
                                     'Click house teleport spell  while looking for burner1',
                                     False, 4, 10,
                                     current_step_region=Common.Inventory_region,
                                     next_step_image_paths=burner1_images,
                                     next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.7)

            Common.watch_click_image(burner1_images, 0.7,
                                     'Click burner1 while looking for burner2',
                                     False, 4, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     next_step_image_paths=burner2_images,
                                     next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.7)

            Common.watch_click_image(burner2_images, 0.7,
                                     'Click burner2 while looking for altar',
                                     False, 4, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     next_step_image_paths=altar_images,
                                     next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.7)

            Common.open_inventory(bones_images)

            Common.watch_click_image(bones_images, 0.7,
                                     'Click bones in inventory while looking for altar',
                                     False, 1, 10,
                                     current_step_region=Common.Inventory_region,
                                     next_step_image_paths=altar_images,
                                     next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.7)

            Common.watch_click_image(altar_images, 0.7,
                                     'Click altar  while looking for spellbook',
                                     False, 54, 10,
                                     current_step_region=Common.Main_game_screen_region,
                                     next_step_image_paths=spell_book_images,
                                     next_step_region=Common.Inventory_bar_region,
                                     next_step_confidence=0.7)

            Common.open_spellbook(camelot_teleport_images)

            Common.watch_click_image(camelot_teleport_images, 0.9,
                                     'Click camelot teleport  while looking for bank chest',
                                     False, 4, 10,
                                     current_step_region=Common.Inventory_region,
                                     next_step_image_paths=bank_images,
                                     next_step_region=Common.Main_game_screen_region,
                                     next_step_confidence=0.7)

            Display.stop_timer(start_time, iterations_needed)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


if __name__ == '__main__':
    offer_bones()
    print('Done offering bones!')
