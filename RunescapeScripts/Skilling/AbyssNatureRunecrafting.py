"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
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
                    - Turn off binding necklace item charge notifications on Runelite
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Castle Wars ring of dueling teleport spot
                    - Click compass, so it's at default north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
Menus:              Inventory menu open
equip items:        - Steam battlestaff
                    - Earth tiara
                    - no necklace
                    - lightest weight gear
items in inventory: - Stack of water runes
                    - Large Rune essence pouch
                    - Medium Rune essence pouch
items in bank:      - Rune essence
                    - Rings of dueling
                    - Binding necklaces with 16 charges
                      (NOTE: if less than 16 charges on necklaces destory one to recharge all others to
                      full charges)
                    - Stamina potions
Setup:           - Set Withdraw-X to 100
                 - Fill up hot air balloon box with bunch of willow logs
                   Note: CAN STORE NOTED LOGS MAX 100 AT A TIME
Objects to mark: - Castle wars bank chest
                 - Castle wars air balloon basket
                 - Castle wars air balloon wood box
                 - Mysterious Ruin near varrock balloon
                 - Earth Run Altar

"""

import RunescapeScripts.Common as Common
import keyboard

# region BANK IMAGES
bank_icon_images = ['Images/BankIcon3.png',
                    'Images/BankIcon2.png',
                    'Images/BankIcon.png']
bank_images = ['Images/CastleWarsChest.png']
bank_close_images = ['Images/BankClose.png',
                     'Images/BankClose2.png']
rune_essence_images = ['Images/RuneEssence.png']
large_rune_pouch_images = ['Images/LargeRunePouch.png']
med_rune_pouch_images = ['Images/MediumRunePouch.png']
water_talisman_images = ['Images/WaterTalisman.png']
willow_log_images = ['Images/WillowLogs.png']
withdraw_one_images = ['Images/Withdraw1Option.png']
withdraw_one_hundred_images = ['Images/Withdraw100Option.png']
withdraw_as_note_images = ['Images/WithdrawAsNote.png']
withdraw_as_item_images = ['Images/WithdrawAsItem.png']
# endregion BANK IMAGES

# region MOVEMENT IMAGES
bridge_images = ['Images/CastleWarsBridge3.png',
                 'Images/CastleWarsBridge2.png',
                 'Images/CastleWarsBridge.png']
dirt_path_images = ['Images/CastleWarsDirtPath.png']
balloon_wood_storage_images = ['Images/CastleWarsBalloonWoodStorage.png']
balloon_store_logs_images = ['Images/StoreLogs.png']
balloon_store_logs_prompt_images = ['Images/BalloonDepositLogsPrompt.png']
balloon_basket_images = ['Images/CastleWarsBalloonBasket.png']
balloon_basket_wood_deposit_images = ['Images/CastleWarsBalloonBasketWoodDeposit.png']
balloon_map_varrock_images = ['Images/BalloonMapVarrock.png']
ruin_images = ['Images/VarrockEarthMysteriousRuin.png',
               'Images/VarrockEarthMysteriousRuin2.png']
rune_altar_images = ['Images/VarrockEarthRuneAltar.png']
water_rune = ['Images/WaterRune.png',
              'Images/WaterRune.png']
empty_pouch_images = ['Images/EmptyPouchOption.png']
ring_of_dueling_bank = ['Images/RingOfDueling2.png']
rub_option = ['Images/RubOption.png',
              'Images/RubOption.png']
castle_wars_teleport = ['Images/CastleWarsArenaTeleportOption.png',
                        'Images/CastleWarsArenaTeleportOption.png']
mud_rune_images = ['Images/MudRune3.png',
                   'Images/MudRune2.png',
                   'Images/MudRune.png']
ring_of_dueling = ['Images/RingOfDueling.png']
stamina_potion_images = ['Images/StaminaPotion.png',
                         'Images/StaminaPotion2.png',
                         'Images/StaminaPotion4.png']
stamina_potion_bank = ['Images/StaminaPotion.png']
vial_images = ['Images/Vial.png',
               'Images/Vial.png']
necklace_of_binding_bank = ['Images/NecklaceOfBinding3.png',
                            'Images/NecklaceOfBinding2.png']
necklace_of_binding_images = ['Images/NecklaceOfBinding3.png',
                              'Images/NecklaceOfBinding2.png',
                              'Images/NecklaceOfBinding.png']
all_chatbox_option = ['Images/AllChatBoxOption.png']

# endregion MOVEMENT IMAGES

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 24)

try:
    # Probably need more mining/agility/theiving for this script to have more options
    # on what obstacles can get through
    # Turn off auto retaliate
    # Entity Hider off
    # Pickaxe equipped and tinderbox in inventory

    # Click bank map icon
    # Click marked bank booth
    # If health is low
        # Right click lobster
        # Withdraw 5
    # If on first or 6th run
        # Right click glory amulet
        # Withdraw 1
    # If on first or 3rd run
        # Right click stamina potion
        # Withdraw 1
    # Get pure rune essence
    # Close bank
    # If health is low
        # eat the 5 lobsters
    # If on first or 6th run
        # Equip glory amulet
        # Open bank
        # Deposit empty glory amulet
    # fill large pouch
    # Fill medium pouch
    # Open bank
    # Get more pure rune essence
    # Run to marked cart
    # Click ditch marked spot
    # Click hill spot on map?
    # Click second hill spot on map
    # Right click marked mage of zamorak
    # Click teleport option
    # While don't see dark mage
        # Spam click burn boils
    # If 28th run go right click marked dark mage
        # Click repair
    # If don't see nature portal on screen
        # Click dark mage on map
    # Click marked nature rift portal
    # Left Click marked nature altar
    # Empty large pouch
    # Empty medium pouch
    # Left click nature altar
    # Go to equipment tab
    # Right click glory amulet
    # Click Edgeville option




    # Open bank to start
    Common.watch_click_image(bank_icon_images, 0.9, 'Move to bank chest using map', False, 1, 10, bank_images,
                             Common.Minimap_region, Common.Top_half_game_screen_region)
    Common.watch_click_image(bank_images, 0.7, 'Click bank chest', False, 0, 10, bank_close_images,
                             Common.Top_half_game_screen_region)

    for x in range(loopsTillDone):
        print('Loop:', x, '/', loopsTillDone)
        Common.print_runtime(loopsTillDone, 90, x)

        # region BANK STUFF

        # Get stuff from bank chest
        # Get new ring of dueling at first run then every 8 runs
        # Note: Get this first so right click menu isn't out of bounds when it's in the first column
        if x % 8 == 0:
            Common.watch_click_image(ring_of_dueling_bank, 0.7, 'Right click ring of dueling', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)

        Common.watch_click_image(water_talisman_images, 0.7, 'Right click water talisman', True, 0, 10, None,
                                 Common.Bank_region)
        Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                 Common.Bank_region)
        Common.watch_click_image(water_talisman_images, 0.7, 'Right click water talisman', True, 0, 10, None,
                                 Common.Bank_region)
        Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                 Common.Bank_region)

        # Get new stamina potion every 15 runs
        if x % 15 == 0:
            # Only deposit vial after first run since won't be present till after first run
            if x != 0:
                Common.watch_click_image(vial_images, 0.7, 'Deposit vial', False, 0, 10, None,
                                         Common.Inventory_region)
            Common.watch_click_image(stamina_potion_bank, 0.7, 'Get Stamina potion', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)

        # Get 100 willow logs every 100 runs
        if x % 100 == 0 and x != 0:
            Common.watch_click_image(withdraw_as_note_images, 0.7, 'Set to withdraw as note', False, 0, 10, None,
                                     Common.Bank_bottom_options_region)
            Common.watch_click_image(willow_log_images, 0.7, 'Right click willow logs', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_hundred_images, 0.9, 'Withdraw one hundred', False, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_as_item_images, 0.7, 'Set to withdraw as item', False, 0, 10, None,
                                     Common.Bank_bottom_options_region)

        # Get new and equip binding necklace at first run then every 16 runs
        # Otherwise just get rune essence
        if x % 16 == 0:
            # Get new necklace of binding
            Common.watch_click_image(necklace_of_binding_bank, 0.7, 'Get new necklace of binding', True, 0, 10, None,
                                     Common.Bank_region)
            Common.watch_click_image(withdraw_one_images, 0.9, 'Withdraw one', False, 0, 10, None,
                                     Common.Bank_region)

            # Get rune essence last since it fills inventory
            Common.watch_click_image(rune_essence_images, 0.7, 'Get rune essence', False, 0, 10, None,
                                     Common.Bank_region)

            # Close bank and put on binding necklace and fill rune pouch
            Common.watch_click_image(bank_close_images, 0.9, 'Close bank')

            # Equip necklace of binding
            Common.watch_click_image(necklace_of_binding_images, 0.6, 'Equip Binding Necklace', False, 0, 10, None,
                                     Common.Inventory_region)

            Common.watch_click_image(large_rune_pouch_images, 0.7, 'Fill rune pouch', False, 1, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(med_rune_pouch_images, 0.7, 'Fill medium rune pouch', False, 1, 10, None,
                                     Common.Inventory_region)

            Common.watch_click_image(bank_images, 0.7, 'Click bank chest', False, 0, 10, bank_close_images,
                                     Common.Top_half_game_screen_region)

            # Get rune essence last since it fills inventory
            Common.watch_click_image(rune_essence_images, 0.7, 'Get more rune essence', False, 0, 10, None,
                                     Common.Bank_region)
        else:
            # Get rune essence last since it fills inventory
            Common.watch_click_image(rune_essence_images, 0.7, 'Get rune essence', False, 0, 10, None,
                                     Common.Bank_region)

            Common.watch_click_image(bank_close_images, 0.9, 'Close bank')

            Common.watch_click_image(large_rune_pouch_images, 0.7, 'Fill large rune pouch', False, 0, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(med_rune_pouch_images, 0.7, 'Fill medium rune pouch', False, 0, 10, None,
                                     Common.Inventory_region)

            Common.watch_click_image(bank_images, 0.7, 'Click bank chest', False, 0, 10, bank_close_images,
                                     Common.Top_half_game_screen_region)

            # Get rune essence last since it fills inventory
            Common.watch_click_image(rune_essence_images, 0.7, 'Get more rune essence', False, 0, 10, None,
                                     Common.Bank_region)

            Common.watch_click_image(bank_close_images, 0.9, 'Close bank')

        # Drink stamina potion every third run
        if x % 3 == 0 and x != 0:
            Common.watch_click_image(stamina_potion_images, 0.7, 'Drink Stamina potion', False, 0, 10, None,
                                     Common.Inventory_region)
        # endregion BANK STUFF

        # region MOVEMENT

        # Move to bridge while looking for dirt path
        Common.watch_click_image(bridge_images, 0.8, 'Move to bridge while looking for dirt path', False, 1,
                                 20, dirt_path_images, Common.Minimap_region, Common.Minimap_region)

        # Click dirt path while looking for balloon
        Common.watch_click_image(dirt_path_images, 0.7, 'Click dirt path while looking for balloon', False, 6,
                                 10, balloon_basket_images, Common.Minimap_region, Common.Top_half_game_screen_region,
                                 0.3)

        # Restock willow logs after 100th run
        # Else carry on to balloon
        if x % 100 == 0 and x != 0:
            # Try to right-click wood deposit box while looking for deposit wood prompt
            count = 0
            while True:
                Common.watch_click_image(all_chatbox_option, 0.7,
                                         'Right Click all chatbox option to clear any bad option menus', True, 0,
                                         10, None, Common.Chatbox_options_region)
                Common.watch_click_image(balloon_wood_storage_images, 0.7,
                                         'Right click wood storage box while looking for store logs option', True, 1)
                Common.watch_click_image(balloon_store_logs_images, 0.9,
                                         'Click on store logs option while looking for store logs prompt', False, 5)
                count += 1

                # If next step is visible or on attempt 10 break out of loop
                if (Common.is_image_on_screen(balloon_store_logs_prompt_images, 0.7, 0,
                                              'Is deposit logs prompt up?', Common.Chatbox_region)):
                    break
                elif count == 10:
                    break

            Common.sleep_with_countdown(1)
            keyboard.write('100')
            keyboard.press('enter')

            Common.watch_click_image(balloon_basket_wood_deposit_images, 0.3,
                                     'Click balloon from wood deposit box while looking for varrock on map', False, 3,
                                     10, balloon_map_varrock_images, Common.Top_half_game_screen_region,
                                     Common.Top_half_game_screen_region)
        else:
            # Click balloon from dirt path while looking for varrock on map
            Common.watch_click_image(balloon_basket_images, 0.3,
                                     'Click balloon from dirt path while looking for varrock on map', False, 4,
                                     10, balloon_map_varrock_images, Common.Top_half_game_screen_region,
                                     Common.Top_half_game_screen_region)

        Common.watch_click_image(balloon_map_varrock_images, 0.8, 'Click Varrock Map', False, 2,
                                 10, None, Common.Top_half_game_screen_region)

        # Click mysterious ruin while looking for earth altar
        Common.watch_click_image(ruin_images, 0.5, ' Click mysterious ruin while looking for earth altar', False, 5,
                                 10, rune_altar_images, Common.Bottom_right_game_screen_region,
                                 Common.Top_half_game_screen_region, 0.5)

        # Craft mud runes and check if they're in inventory if they aren't try crafting them again up to ten times
        count = 0
        while True:
            Common.watch_click_image(water_rune, 0.8, 'Click Water Rune', False, 0, 10, None, Common.Inventory_region)
            Common.watch_click_image(rune_altar_images, 0.5, 'Click Rune Altar', False, 4)
            Common.watch_click_image(large_rune_pouch_images, 0.7, 'Right click large rune pouch', True, 0, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(empty_pouch_images, 0.8, 'Empty pouch', False, 1, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(med_rune_pouch_images, 0.7, 'Right click medium rune pouch', True, 0, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(empty_pouch_images, 0.8, 'Empty pouch', False, 1, 10, None,
                                     Common.Inventory_region)
            Common.watch_click_image(water_rune, 0.8, 'Click Water Rune 2', False, 1, 10, None, Common.Inventory_region)
            Common.watch_click_image(rune_altar_images, 0.5, 'Click Rune Altar 2', False, 2)

            # If mud runes in inventory break loop
            if Common.is_image_on_screen(mud_rune_images, 0.8, 0, 'Are mud runes in inventory?',
                                         Common.Inventory_region) is True and count < 10:
                break

            count += 1

        # Teleport back to castle wars and open bank
        Common.watch_click_image(ring_of_dueling, 0.8, 'Right click ring of dueling', True, 1, 10, None,
                                 Common.Inventory_region)
        Common.watch_click_image(rub_option, 0.8, 'Rub ring', False, 1, 10, None,
                                 Common.Inventory_region)
        Common.watch_click_image(castle_wars_teleport, 0.8, 'Teleport to Castle Wars', False, 1, 10, None,
                                 Common.Chatbox_region)

        # endregion MOVEMENT

        # region BANK DEPOSIT

        # Bank mud runes
        Common.watch_click_image(bank_icon_images, 0.9, 'Move to bank chest using map', False, 1, 10, bank_images,
                                 Common.Minimap_region, Common.Top_half_game_screen_region)
        Common.watch_click_image(bank_images, 0.7, 'Click bank chest', False, 0, 10, bank_close_images,
                                 Common.Top_half_game_screen_region)
        Common.watch_click_image(mud_rune_images, 0.8, 'Deposit Mud Runes', False, 0, 10, None,
                                 Common.Inventory_region)
        # endregion BANK DEPOSIT

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
