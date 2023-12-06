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
Monitors:           4k or 3K display
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Edgeville top left bank teller
                    - Click compass, so it's at default north
                    - Zoom out, hold up arrow to get camera all the way up
                    - Zoom all the way out
Menus:              Inventory menu open
equip items:        - lightest weight gear
items in inventory: - Bracelet mould
items in bank:      - Gold bars
                    - Stamina potions
Setup:           - N/A
Objects to mark: - Edgeville left top bank teller
                 - Edgeville furnace

"""

import Common as Common

# Constants
runtime_per_run = 90

# region BANK IMAGES
bank_icon_images = ['Images/BankIcon3.png',
                    'Images/BankIcon2.png',
                    'Images/BankIcon.png']
bank_images = ['Images/Crafting/Bank.png']
gold_bar_images = ['Images/Crafting/GoldBar.png']
gold_bar_images = ['Images/Crafting/GoldBar.png']
furnace_images = ['Images/Crafting/Furnace.png']
craft_bracelet_images = ['Images/Crafting/CraftGoldBracelet.png']
bank_furnace_images = ['Images/Crafting/BankFromFurnace.png']
gold_bracelet_images = ['Images/Crafting/GoldBracelet.png']

bank_close_images = ['Images/BankClose.png',
                     'Images/BankClose2.png']
withdraw_one_images = ['Images/Withdraw1Option.png']
withdraw_as_note_images = ['Images/WithdrawAsNote.png']
withdraw_as_item_images = ['Images/WithdrawAsItem.png']
# endregion BANK IMAGES

# region MOVEMENT IMAGES
stamina_potion_images = ['Images/StaminaPotion.png',
                         'Images/StaminaPotion2.png',
                         'Images/StaminaPotion4.png']
stamina_potion_bank = ['Images/StaminaPotion.png']
vial_images = ['Images/Vial.png',
               'Images/Vial.png']
# endregion MOVEMENT IMAGES

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / 27)

try:
    # Open bank from in front of teller
    Common.watch_click_image(bank_images, 0.7, 'Click bank teller', False, 0, 10, bank_close_images,
                             Common.Top_half_game_screen_region, Common.Top_half_game_screen_region)

    # Loop
    for x in range(loopsTillDone):
        print('Loop:', x, '/', loopsTillDone)
        Common.print_runtime(loopsTillDone, runtime_per_run, x)
        # If on 10th run
            # Right click stamina potion
            # Withdraw one
            # Close bank
            # Drink stamina potion
            # Open bank
        # Withdraw gold bars
        Common.watch_click_image(gold_bar_images, 0.7, 'Withdraw gold bars', False, 0, 10, None,
                                 Common.Bank_region)
        # Click furnace (sleep for like 4 seconds)
        Common.watch_click_image(furnace_images, 0.7, 'Click furnace', False, 5, 10, craft_bracelet_images,
                                 Common.Top_half_game_screen_region, Common.Bank_region)
        # Click bracelet craft option (sleep like 60 seconds)
        Common.watch_click_image(craft_bracelet_images, 0.7, 'Click gold bracelet craft', False, 50, 10, None,
                                 Common.Bank_region)
        # Click bank from furnace
        Common.watch_click_image(bank_furnace_images, 0.7, 'Click bank from furnace', False, 5, 10, bank_close_images,
                                 Common.Bottom_half_game_screen_region)
        # Deposit gold bracelets
        Common.watch_click_image(gold_bracelet_images, 0.7, 'Click gold bar in inventory', False, 0, 10, None,
                                 Common.Inventory_region)

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')
