"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                    - RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - 117HD OFF and GPU ON
                    - Set Object Markers:
                      - Border width to 6
                      - Marker colors:
                        - FFD400FF for log storage (purple)
                        - FF00FFDD for all object (cyan)
                      - Highlight clickbox enabled with all others disabled
                      - Remember color per object
                    - GPU plugin draw distance set to 66
                    - Camera plugin Expand outer zoom limit: 200
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Lunar Isle Moonclan teleport middle bank stall
                    - Right Click compass and face south
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
                    - Zoom minimap all the way out
Menus:              - Inventory menu Open
                    - Set defensive attack mode and auto retaliate off (in case attacked by trolls)
                    - Set Spell filters to uncheck "show spells you lack the runes to cast"
equip items:        - Dust battlestaff
                    - Seal of passage necklace
                    - Full graceful set
items in inventory: - Giant/Large/Medium/small Rune essences pouches
                    - Cosmic and Law runes in rune pouch
items in bank:      - Rune essence
                    - Teleport home tablets
                    - Abyssal Book so dark mage repairs with NPC Contact spell (Can be anywhere in bank)
Setup:           - Open bank to tab with all items
                 - With bank window open, swap the left click for each rune pouch to Fill option
                 - Shift click NPC contact spell and set left click to Dark Mage via Runelite menu entry swapper plugin
                       - Note: May have to contact dark mage once before this is available
                 - Make sure inventory menu is not open
                 - Change banked player house tablet left click to withdraw 1 using runelite menu swapper plugin
                 - Change banked lobster left click to withdraw 1 using runelite menu swapper plugin
                 - Disable Regeneration Meter runelite plugin so it doesn't get in the way of checking HP
                 - Mark following inventory items using Inventory Tags runelite plugin:
                    - Small pouch: Yellow
                    - Medium pouch: Red
                    - Large pouch: Teal
                    - Giant pouch: Magenta
                    - Rune pouch: Blue (0043FF)
                - Disable Rune Pouch plugin so runes in pouch are not shown
Objects to mark: - Enable Highlight hull and Highlight clickbox
                 - Marker color to default magenta (FFD400FF)
                 - Border width: 6
                 - Middle bank teller
                 - Astral altar
                 - Revitalisation pool or above in Player house for stamina recovery
"""
from time import sleep

import pyautogui

import Banking
import Common as Common
import Display

# Constants
runes_crafted_per_run = 100

bank1_images = ['Images/Runecrafting/Astral/BankBooth1.png']
bank2_images = ['Images/Runecrafting/Astral/BankBooth2.png']
tiara_bank_tab_images = ['Images/Runecrafting/Astral/TiaraBankTab.png']
rune_essence_images = ['Images/Runecrafting/Astral/RuneEssence.png']
giant_rune_pouch_images = ['Images/Runecrafting/Astral/RunePouchGiant.png']
large_rune_pouch_images = ['Images/Runecrafting/Astral/RunePouchLarge.png']
med_rune_pouch_images = ['Images/Runecrafting/Astral/RunePouchMedium.png']
small_rune_pouch_images = ['Images/Runecrafting/Astral/RunePouchSmall.png']
rune_pouch_images = ['Images/Runecrafting/Astral/RunePouch.png']
stamina_potion_bank = ['Images/Astral/StaminaPotion.png']
stamina_potion_images = ['Images/Runecrafting/Astral/StaminaPotion.png',
                         'Images/Runecrafting/Astral/StaminaPotion2.png',
                         'Images/Runecrafting/Astral/StaminaPotion4.png']

altar1_images = ['Images/Runecrafting/Astral/Altar1.png']
altar2_images = ['Images/Runecrafting/Astral/Altar2.png']
inventory_tab_images = ['Images/Runecrafting/Astral/InventoryTab.png']
lunar_spellbook_images = ['Images/Runecrafting/Astral/LunarSpellbook.png']
astral_rune_images = ['Images/Runecrafting/Astral/AstralRune.png']
teleport_images = ['Images/Runecrafting/Astral/Teleport.png']

npc_contact_images = ['Images/Runecrafting/Astral/NpcContact.png']
dark_mage_images = ['Images/Runecrafting/Astral/DarkMage.png']
continue_images = ['Images/Runecrafting/Astral/Continue.png']
fix_pouches_images = ['Images/Runecrafting/Astral/Repair.png']

low_health_images = ['Images/Runecrafting/Astral/LowHealth.png']
lobster_images = ['Images/Runecrafting/Astral/Lobster.png']
home_teleport_images = ['Images/Runecrafting/Astral/HomeTeleport.png']
pool_images = ['Images/Runecrafting/Astral/Pool.png']

astral_altar = [1064, 331]


def open_bank1():
    Common.watch_click_image(bank1_images, 0.7, 'Click bank booth and look for bank options', False,
                             1, 10, current_step_region=Common.Main_game_screen_region,
                             next_step_image_paths=Banking.bank_withdraw_note_images, next_step_confidence=0.4,
                             next_step_region=Common.Bank_bottom_options_region)


def click_inventory_tab():
    Common.watch_click_image(inventory_tab_images, 0.7, 'Switch back to inventory tab', False,
                             2, 10, None, Common.Inventory_bar_region)


def go_to_bank_from_teleport():
    Common.watch_click_image(bank2_images, 0.7, 'Click bank booth 2 while looking for bank booth 1',
                             False, 7, 10, current_step_region=Common.Main_game_screen_region,
                             next_step_image_paths=bank1_images,
                             next_step_region=Common.Main_game_screen_region,
                             next_step_confidence=0.7)
    open_bank1()


def cast_lunar_teleport():
    Common.watch_click_image(lunar_spellbook_images, 0.7, 'Open spellbook while looking for teleport',
                             False, 2, 10, teleport_images,
                             Common.Inventory_bar_region, Common.Inventory_region)

    Common.watch_click_image(teleport_images, 0.7, 'Click teleport', False, 5,
                             10, None, Common.Inventory_region)


def pouch_astral_runes():
    Common.watch_click_image(astral_rune_images, 0.7, 'Click astrals in inventory',
                             False, 1, 10, None, Common.Inventory_region)

    Common.watch_click_image(rune_pouch_images, 0.7, 'Click rune pouch in inventory',
                             False, 1, 10, None, Common.Inventory_region)


def heal_hp():
    is_hp_low = Common.is_image_on_screen(low_health_images, 0.8, 0, 'Check if health is low',
                                          Common.Minimap_vitals_region)
    # If HP is low grab lobster and heal
    if is_hp_low:
        Common.watch_click_image(lobster_images, 0.7, 'Click bank lobster', False,
                                 1, 10, None, Common.Bank_region)
        Banking.close_bank()
        Common.watch_click_image(lobster_images, 0.7, 'Click lobster to heal', False,
                                 2, 10, None, Common.Inventory_region)

        open_bank1()


def check_repair_pouches(iteration):
    # Repair pouches every 9 runs before pouch degrades and changes colors
    # Do (pouch uses before breaks - 2) to fix it before it degrades so visual change doesn't mess up script
    # Note: Pouches repaired at second dark mage dialog:
    # "Fine. A simple transfiguration spell should resolve things"
    if iteration % 9 == 0:
        Common.watch_click_image(npc_contact_images, 0.7, 'Click on NPC Contact spell', False,
                                 6, 10, None, Common.Inventory_region)

        pyautogui.press('space')
        print('press space to continue conversation 1')
        sleep(2)

        pyautogui.press('1')
        print('press 1 to select fix pouches options')
        sleep(2)

        pyautogui.press('space')
        print('press space to continue conversation 2')
        sleep(2)

        pyautogui.press('space')
        print('press space to continue conversation 3')
        sleep(2)


def craft_astrals():
    try:
        heal_hp()

        # Get how many from user
        item_count_string = input("How many astrals do you want to craft? ")

        # Calculate how many loops needed
        item_count = int(item_count_string)
        loops_till_done = round(item_count / runes_crafted_per_run)

        open_bank1()

        Common.watch_click_image(tiara_bank_tab_images, 0.7, 'Click tiara bank tab', False,
                                 1, 10, None, Common.Top_half_game_screen_region)

        for x in range(loops_till_done):
            start_time = Display.start_timer()

            Common.watch_click_image(rune_essence_images, 0.7, 'Withdraw rune essence 1', False,
                                     0, 10, None,
                                     Common.Bank_region)
            sleep(1.5)

            Common.watch_click_image(small_rune_pouch_images, 0.7, 'Fill small rune pouch', False,
                                     0, 10, None,
                                     Common.Inventory_region)
            sleep(1.5)
            Common.watch_click_image(med_rune_pouch_images, 0.7, 'Fill medium rune pouch', False,
                                     0, 10, None,
                                     Common.Inventory_region)
            sleep(1.5)
            Common.watch_click_image(large_rune_pouch_images, 0.7, 'Fill large rune pouch', False,
                                     0, 10, None,
                                     Common.Inventory_region)
            sleep(1.5)

            Common.watch_click_image(rune_essence_images, 0.7, 'Withdraw rune essence 2', False,
                                     0, 10, None,
                                     Common.Bank_region)
            sleep(1.5)

            Common.watch_click_image(giant_rune_pouch_images, 0.7, 'Fill giant rune pouch', False,
                                     0, 10, None,
                                     Common.Inventory_region)
            sleep(1.5)

            Common.watch_click_image(rune_essence_images, 0.7, 'Withdraw rune essence 3', False,
                                     1, 10, None,
                                     Common.Bank_region)

            Banking.close_bank()

            Common.move_mouse_and_left_click(astral_altar[0], astral_altar[1], 0, 'Move to Astral altar')
            sleep(27)

            Common.watch_click_image(altar1_images, 0.7, 'Click astral altar1', False,
                                     5, 10, None,
                                     Common.Main_game_screen_region)

            # Empty pouches
            pyautogui.keyDown('shift')
            Common.watch_click_image(small_rune_pouch_images, 0.7, 'Empty small rune pouch', False,
                                     0, 10, None,
                                     Common.Inventory_region)
            sleep(1.5)

            Common.watch_click_image(med_rune_pouch_images, 0.7, 'Empty medium rune pouch', False,
                                     0, 10, None,
                                     current_step_region=Common.Inventory_region)
            sleep(1.5)

            Common.watch_click_image(large_rune_pouch_images, 0.7, 'Empty large rune pouch', False,
                                     0, 10, None,
                                     current_step_region=Common.Inventory_region)
            sleep(1.5)

            Common.watch_click_image(altar2_images, 0.6, 'Click astral altar2', False,
                                     0, 10, None,
                                     Common.Main_game_screen_region)
            sleep(1.5)

            Common.watch_click_image(giant_rune_pouch_images, 0.7, 'Empty giant rune pouch', False,
                                     0, 10, None,
                                     current_step_region=Common.Inventory_region)
            sleep(1.5)

            pyautogui.keyUp('shift')

            Common.watch_click_image(altar2_images, 0.6, 'Click altar 2 to craft more runes', False,
                                     3, 10, None, Common.Main_game_screen_region)

            cast_lunar_teleport()
            check_repair_pouches(x)
            click_inventory_tab()
            pouch_astral_runes()
            go_to_bank_from_teleport()

            # Display timer here so it's not inflated by stamina restore run and low hp check and heal
            Display.stop_timer(start_time, loops_till_done)

            heal_hp()

            # Teleport to house and restore stamina every couple of runs
            if x % 6 == 0:
                Common.watch_click_image(home_teleport_images, 0.7, 'Withdraw home teleport tablet', False,
                                         1, 10, None,
                                         Common.Bank_region)

                Banking.close_bank()

                Common.watch_click_image(home_teleport_images, 0.7, 'Use home teleport tablet', False,
                                         7, 10, None,
                                         Common.Inventory_region)

                # Use stamina pool
                Common.watch_click_image(pool_images, 0.7, 'Use pool to restore stamina', False,
                                         7, 10, None,
                                         Common.Main_game_screen_region)
                cast_lunar_teleport()
                click_inventory_tab()
                go_to_bank_from_teleport()

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    craft_astrals()
    print('Done crafting astral runes!')
