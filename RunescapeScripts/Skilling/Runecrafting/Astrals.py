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
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Lunar Isle Moonclan teleport spot
                    - Click compass, so it's at default north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
Menus:              - Inventory menu open
                    - Set defensive attack mode and auto retaliate off (in case attacked by trolls)
                    - Set Spell filters to uncheck "show spells you lack the runes to cast"
                    - Shift click NPC contact spell and set to Dark Mage via Runelite menu entry swapper plugin
                       - Note: May have to contact dark mage once before this is available
equip items:        - Dust battlestaff
                    - Seal of passage necklace
                    - lightest weight gear
items in inventory: - Law runes
                    - Cosmic runes
                    - Large Rune essence pouch
                    - Medium Rune essence pouch
items in bank:      - Rune essence
                    - Stamina potions (4)
                    - Abyssal Book
Setup:           - Open bank to tab with all items
Objects to mark: - Middle bank teller
                 - Astral altar

"""
import pyautogui

import RunescapeScripts.Common as Common
import keyboard

# Constants
runtime = 60
runes_crafted_per_run = 48

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / runes_crafted_per_run)

try:
    # region BANK IMAGES
    bank_icon_images = ['Images/Runecrafting/BankIcon.png',
                        'Images/Runecrafting/BankIcon2.png']
    bank_images1 = ['Images/Runecrafting/bank.png']
    bank_images2 = ['Images/Runecrafting/bank2.png']
    rune_essence_images = ['Images/Runecrafting/RuneEssence.png']
    bank_close_images = ['Images/BankClose.png',
                         'Images/BankClose2.png']
    giant_rune_pouch_images = ['Images/Runecrafting/GiantRunePouch.png']
    large_rune_pouch_images = ['Images/Runecrafting/LargeRunePouch.png']
    med_rune_pouch_images = ['Images/Runecrafting/MediumRunePouch.png']
    stamina_potion_bank = ['Images/StaminaPotion.png']
    stamina_potion_images = ['Images/Runecrafting/StaminaPotion.png',
                             'Images/Runecrafting/StaminaPotion2.png',
                             'Images/Runecrafting/StaminaPotion4.png']
    withdraw_one_images = ['Images/Withdraw1Option.png']
    vial_images = ['Images/Vial.png']
    # endregion BANK IMAGES

    # region MOVEMENT IMAGES
    map_images1 = ['Images/Runecrafting/map1.png']
    map_images2 = ['Images/Runecrafting/map2.png']
    map_images3 = ['Images/Runecrafting/map3.png']
    map_images4 = ['Images/Runecrafting/map4.png']
    map_images5 = ['Images/Runecrafting/map5.png']
    pillar_images = ['Images/Runecrafting/Pillar.png']
    altar_images = ['Images/Runecrafting/Altar.png']
    altar_images2 = ['Images/Runecrafting/Altar2.png']
    lunar_spellbook_images = ['Images/Runecrafting/LunarSpellbook.png']
    astral_rune_images = ['Images/Runecrafting/AstralRune.png']
    teleport_images = ['Images/Runecrafting/Teleport.png']
    inventory_images = ['Images/Runecrafting/Inventory.png']

    npc_contact_images = ['Images/Runecrafting/NpcContact.png']
    dark_mage_images = ['Images/Runecrafting/DarkMage.png']
    continue_images = ['Images/Runecrafting/Continue.png']
    fix_pouches_images = ['Images/Runecrafting/Repair.png']

    low_health_images = ['Images/Runecrafting/LowHealth.png']
    lobster_images = ['Images/Runecrafting/Lobster.png']
    # endregion MOVEMENT IMAGES

    def click_bank():
        try:
            Common.watch_click_image(bank_images1, 0.4, 'Click bank 1', False, 6, 10,
                                     None, Common.Top_half_game_screen_region)
            # If bank is not opened try clicking bank teller from second spot
            if Common.is_image_on_screen(bank_close_images) is False:
                Common.watch_click_image(bank_images2, 0.4, 'Click bank while looking for close button', False, 2, 10,
                                         bank_close_images, Common.Top_half_game_screen_region)
        except ValueError as val_error:
            raise val_error

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, runtime, x)

        # region BANK STUFF
        click_bank()

        # Deposit astrals after first run since won't have any at start of first run
        if x != 0:
            Common.watch_click_image(astral_rune_images, 0.7, 'Click astrals to deposit', False, 0,
                                     10, None, Common.Inventory_region)

        # If HP is low grab two lobsters and heal
        if Common.is_image_on_screen(low_health_images, 0.6, 0, 'Check if health is low', Common.Minimap_vitals_region):
            Common.watch_click_image(lobster_images, 0.7, 'Right click lobster', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(lobster_images, 0.7, 'Right click lobster', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(bank_close_images, 0.9, 'Close bank')
            Common.watch_click_image(lobster_images, 0.7, 'Click lobster to eat', False, 2, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(lobster_images, 0.7, 'Click lobster to eat', False, 2, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(bank_images2, 0.5, 'Click bank while looking for close button', False, 2, 10,
                                     bank_close_images, Common.Top_half_game_screen_region)

        # Get new stamina potion every 4 runs
        if x % 4 == 0:
            # Only deposit vial after first run since won't be present till after first run
            if x != 0:
                Common.watch_click_image(vial_images, 0.7, 'Deposit vial', False, 0, 10, None,
                                         Common.Inventory_region)
            Common.watch_click_image(stamina_potion_bank, 0.7, 'Get Stamina potion', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)

        # Get rune essence and fill pouches
        Common.watch_click_image(rune_essence_images, 0.7, 'Get rune essence', False, 0, 10, None,
                                 Common.Bank_region)

        Common.watch_click_image(bank_close_images, 0.9, 'Close bank', False, 1)

        Common.watch_click_image(giant_rune_pouch_images, 0.7, 'Fill giant rune pouch', False, 1, 10, None,
                                 Common.Inventory_region)
        Common.watch_click_image(large_rune_pouch_images, 0.7, 'Fill large rune pouch', False, 1, 10, None,
                                 Common.Inventory_region)

        Common.watch_click_image(bank_images2, 0.7, 'Click bank', False, 0, 10, bank_close_images,
                                 Common.Top_half_game_screen_region)
        Common.watch_click_image(rune_essence_images, 0.7, 'Get more rune essence', False, 0, 10, None,
                                 Common.Bank_region)
        Common.watch_click_image(bank_close_images, 0.9, 'Close bank', False, 1)

        Common.watch_click_image(med_rune_pouch_images, 0.7, 'Fill medium rune pouch', False, 1, 10, None,
                                 Common.Inventory_region)

        Common.watch_click_image(bank_images2, 0.7, 'Click bank', False, 0, 10, bank_close_images,
                                 Common.Top_half_game_screen_region)
        Common.watch_click_image(rune_essence_images, 0.7, 'Get more rune essence', False, 0, 10, None,
                                 Common.Bank_region)

        # endregion BANK STUFF

        # region MOVEMENT
        Common.watch_click_image(map_images1, 0.7, 'Move to map1 while looking for map2', False, 4,
                                 10, map_images2, Common.Minimap_region, Common.Minimap_region)
        Common.watch_click_image(map_images2, 0.7, 'Move to map2 while looking for map3', False, 6,
                                 10, map_images3, Common.Minimap_region, Common.Minimap_region)
        Common.watch_click_image(map_images3, 0.7, 'Move to map3 while looking for map4', False, 6,
                                 10, map_images4, Common.Minimap_region, Common.Minimap_region, 0.7)
        Common.watch_click_image(map_images4, 0.7, 'Move to map4 while looking for map5', False, 5,
                                 10, map_images5, Common.Minimap_region, Common.Minimap_region, 0.5)
        Common.watch_click_image(map_images5, 0.5, 'Move to map5 while looking for pillar', False, 7,
                                 10, pillar_images, Common.Minimap_region, Common.Top_half_game_screen_region, 0.5)

        Common.watch_click_image(pillar_images, 0.5, 'Click pillar while  looking for altar', False, 5,
                                 10, altar_images, Common.Top_half_game_screen_region,
                                 Common.Center_game_screen_region, 0.5)
        Common.watch_click_image(altar_images2, 0.5, 'Click altar while looking for astrals in inv', False, 2,
                                 10, astral_rune_images, Common.Center_game_screen_region,
                                 Common.Inventory_region, 0.5)

        # Empty pouches
        pyautogui.keyDown('shift')
        Common.watch_click_image(giant_rune_pouch_images, 0.7, 'Empty giant rune pouch', False, 0, 10, None,
                                 Common.Inventory_region)
        Common.watch_click_image(large_rune_pouch_images, 0.7, 'Empty large rune pouch', False, 0, 10, None,
                                 Common.Inventory_region)
        pyautogui.keyUp('shift')

        Common.watch_click_image(altar_images2, 0.7, 'Click altar 2 to craft more runes', False, 2,
                                 10, None, Common.Center_game_screen_region)

        pyautogui.keyDown('shift')

        Common.watch_click_image(med_rune_pouch_images, 0.7, 'Empty medium rune pouch', False, 0, 10, None,
                                 Common.Inventory_region)
        pyautogui.keyUp('shift')

        Common.watch_click_image(altar_images2, 0.7, 'Click altar 2 to craft more runes again', False, 2,
                                 10, None, Common.Center_game_screen_region)

        Common.watch_click_image(lunar_spellbook_images, 0.7, 'Open spellbook while looking for teleport', False, 0,
                                 10, teleport_images, Common.Inventory_bar_region, Common.Inventory_region)
        Common.watch_click_image(teleport_images, 0.7, 'Click teleport', False, 4,
                                 10, None, Common.Inventory_region)

        # Repair pouches every 11 runs before pouch degrades and changes colors
        # Do (pouch uses before breaks - 2) to fix it before it degrades so visual change doesn't mess up script
        # Note: Pouches repaired at second dark mage dialog:
        # "Fine. A simple transfiguration spell should resolve things"
        if x % 9 == 0:
            Common.watch_click_image(npc_contact_images, 0.7, 'Click on NPC Contact spell', False, 6,
                                     10, None, Common.Inventory_region)
            Common.watch_click_image(continue_images, 0.7, 'Click continue conversation', False, 1,
                                     10, None, Common.Chatbox_region)
            Common.watch_click_image(fix_pouches_images, 0.7, 'Click fix pouches', False, 2,
                                     10, None, Common.Chatbox_region)
            Common.watch_click_image(continue_images, 0.7, 'Click continue conversation', False, 2,
                                     10, None, Common.Chatbox_region)
            Common.watch_click_image(continue_images, 0.7, 'Click continue conversation', False, 2,
                                     10, None, Common.Chatbox_region)

        Common.watch_click_image(inventory_images, 0.7, 'Switch back to inventory tab', False, 0,
                                 10, None, Common.Inventory_bar_region)

        # Drink stamina potion every run
        # if x % 2 == 0:
        Common.watch_click_image(stamina_potion_images, 0.8, 'Drink Stamina potion', False, 0, 10, None,
                                 Common.Inventory_region)

        # region MOVEMENT

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
