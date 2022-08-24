"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players
                    - 117HD ON
                    - Set Object Markers:
                      - Border width to 12
                      - Marker color to: #FF00FFDD
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
items in bank:      - Rune essence
                    - Rings of dueling
                    - Binding necklaces
                    - Stamina potions
Setup:           - Fill up hot air balloon box with bunch of willow logs
                   Note: CAN STORE NOTED LOGS MAX 100 AT A TIME
Objects to mark: - Castle wars bank chest
                 - Castle wars air balloon basket
                 - Mysterious Ruin near varrock balloon
                 - Earth Run Altar

"""

import RunescapeScripts.Common as Common

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 26)

try:
    red_rug_images = ['Images/CastleWarsRedRug3.png',
                      'Images/CastleWarsRedRug2.png',
                      'Images/CastleWarsRedRug.png']
    bank_icon_images = ['Images/BankIcon.png',
                        'Images/BankIcon.png']
    bank_images = ['Images/CastleWarsChest5.png',
                   'Images/CastleWarsChest4.png',
                   'Images/CastleWarsChest3.png',
                   'Images/CastleWarsChest2.png',
                   'Images/CastleWarsChest.png']
    bank_close_images = ['Images/BankClose.png',
                         'Images/BankClose2.png']
    rune_essence_images = ['Images/RuneEssence.png',
                           'Images/RuneEssence.png']
    water_talisman_images = ['Images/WaterTalisman.png',
                             'Images/WaterTalisman.png']
    withdraw_one_images = ['Images/Withdraw1Option.png',
                           'Images/Withdraw1Option.png']
    bridge_images = ['Images/CastleWarsBridge3.png',
                     'Images/CastleWarsBridge2.png',
                     'Images/CastleWarsBridge.png']
    balloon_basket_images = ['Images/CastleWarsBalloonBasket2.png',
                             'Images/CastleWarsBalloonBasket.png']
    balloon_map_varrock_images = ['Images/BalloonMapVarrock.png',
                                  'Images/BalloonMapVarrock.png']
    ruin_images = ['Images/VarrockEarthMysteriousRuin.png',
                   'Images/VarrockEarthMysteriousRuin.png']
    rune_altar_images = ['Images/VarrockEarthRuneAltar.png',
                         'Images/VarrockEarthRuneAltar.png']
    water_rune = ['Images/WaterRune.png',
                  'Images/WaterRune.png']
    ring_of_dueling = ['Images/RingOfDueling.png',
                       'Images/RingOfDueling2.png']
    rub_option = ['Images/RubOption.png',
                  'Images/RubOption.png']
    castle_wars_teleport = ['Images/CastleWarsArenaTeleportOption.png',
                            'Images/CastleWarsArenaTeleportOption.png']
    mud_rune_images = ['Images/MudRune2.png',
                       'Images/MudRune.png']
    stamina_potion_images = ['Images/StaminaPotion.png',
                             'Images/StaminaPotion4.png']
    vial_images = ['Images/Vial.png',
                   'Images/Vial.png']
    necklace_of_binding_images = ['Images/NecklaceOfBinding2.png',
                                  'Images/NecklaceOfBinding.png']

    # Then open bank to start
    Common.click_image(bank_icon_images, 0.7, 2, 'Move to bank chest using map')
    Common.click_image(bank_images, 0.7, 5, 'Click bank chest')

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, 65, x)

        # Get stuff from chest
        Common.click_image(water_talisman_images, 0.7, 3, 'Right click water talisman', True)
        Common.click_image(withdraw_one_images, 0.9, 1, 'Withdraw one')

        # Get new ring of dueling at first run then every 8 runs
        if x % 8 == 0:
            Common.click_image(ring_of_dueling, 0.7, 1, 'Get new ring of dueling', True)
            Common.click_image(withdraw_one_images, 0.9, 1, 'Withdraw one')

        # Get new and equip binding necklace at first run then every 16 runs
        # Also get new stamina potion
        # Otherwise just get rune essence
        if x % 16 == 0:
            # Get new necklace of binding
            Common.click_image(necklace_of_binding_images, 0.9, 1, 'Get new necklace of binding', True)
            Common.click_image(withdraw_one_images, 0.9, 1, 'Withdraw one')

            # Deposit vial (Skip on first run since won't have one)
            if x != 0:
                Common.click_image(vial_images, 0.9, 1, 'Deposit vial')

            # Get stamina potion
            Common.click_image(stamina_potion_images, 0.7, 1, 'Get Stamina potion', True)
            Common.click_image(withdraw_one_images, 0.9, 1, 'Withdraw one')

            # Get rune essence last since it fills inventory
            Common.click_image(rune_essence_images, 0.7, 1, 'Get rune essence')

            # Close bank and put on binding necklace
            Common.click_image(bank_close_images, 0.9, 1, 'Close bank')
            Common.click_image(necklace_of_binding_images, 0.8, 1, 'Equip Binding Necklace')
        else:
            # Get rune essence last since it fills inventory
            Common.click_image(rune_essence_images, 0.7, 1, 'Get rune essence')
            Common.click_image(bank_close_images, 0.9, 1, 'Close bank')

        # Drink stamina potion at first run then every fourth run
        if x % 4 == 0:
            Common.click_image(stamina_potion_images, 0.7, 1, 'Drink Stamina potion')

        # Take Balloon to Varrock
        Common.click_image(bridge_images, 0.9, 1, 'Move to bridge using map')
        Common.click_image(balloon_basket_images, 0.7, 6, 'Click Balloon')
        Common.click_image(balloon_map_varrock_images, 0.9, 9, 'Click Varrock on Map')

        # Craft mud runes
        Common.click_image(ruin_images, 0.7, 7, 'Click Mysterious Ruin')
        Common.click_image(water_rune, 0.9, 5, 'Click Water Rune')
        Common.click_image(rune_altar_images, 0.9, 1, 'Click Rune Altar')

        # Teleport back to castle wars and open bank
        Common.click_image(ring_of_dueling, 0.9, 5, 'Right click ring of dueling', True)
        Common.click_image(rub_option, 0.9, 1, 'Rub ring')
        Common.click_image(castle_wars_teleport, 0.9, 1, 'Teleport to Castle Wars')

        # Bank mud runes
        Common.click_image(bank_icon_images, 0.7, 3, 'Move to bank chest using map')
        Common.click_image(bank_images, 0.7, 5, 'Click bank chest')
        Common.click_image(mud_rune_images, 0.7, 4, 'Deposit Mud Runes')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

