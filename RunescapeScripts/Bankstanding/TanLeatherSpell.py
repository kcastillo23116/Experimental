"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75% and performance mode enabled
                    - Runelite sidebar CLOSED
                    - NPC Indicators plugin: Highlight hull, highlight outline, highlight color: FF00FFFF, Border width: 2
                    - Turn on NPC Indicators plugin, Shift+Right click banker and click Tag All
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite
                    - 117HD OFF
Monitors:           - 4k middle monitor with all three on
bank settings:      - Withdraw As: Item
                    - Quantity: All
location:           - Grand exchange, directly in front of the right bottom bank teller box
                    - click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              - Spellbook not open
equip items:        - Fire staff
items in inventory: - Rune pouch with following runes:
                        - Nature
                        - Astral
items in bank:      - Blue Dragon Hide
                    - Red Dragon Hide
Objects to Mark:    - With: NPC Indicator settings:
                        - Highlight Hull
                        - Highlight tile
                        - Highlight outline
                        - Highlight and Fill color: Cyan (FF00FFFF)
                        - Border width 2
                    - Top Grand Exchange banker on Eastern side
Setup:              - Lunar spell book with only utility spells filter enabled
                    - Enable XP drops by clicking the XP button at top left of minimap so you can see that pies being
                      baked
"""
import timeit

import Common as Common
import Banking as Banking
import Display

defaultTimeBeforeClick = 1

# Images
lunar_spellbook_tab_images = ['Images/Cooking/LunarSpellbookTab.png']
dragon_hide_images = ['Images/BankStanding/TanLeather/BlackDragonHide.png',
                      'Images/BankStanding/TanLeather/BlueDragonHide.png',
                      'Images/BankStanding/TanLeather/RedDragonHide.png']
tan_leather_spell_images = ['Images/BankStanding/TanLeather/TanLeatherSpell.png']
dragon_leather_images = ['Images/BankStanding/TanLeather/BlackDragonLeather.png',
                         'Images/BankStanding/TanLeather/BlueDragonLeather.png',
                         'Images/BankStanding/TanLeather/RedDragonLeather.png']


def cast_tan_leather():
    try:
        # Get how many from user
        item_count_string = input("How many hides do do want to tan? ")
        item_count = int(item_count_string)

        # Calculate how many loops needed
        loops_till_done = round(item_count / 25)

        Common.watch_click_image(lunar_spellbook_tab_images, 0.7, 'Open lunar spellbook', sleep_time_after_click=1,
                                 current_step_region=Common.Inventory_bar_region)

        for x in range(loops_till_done):
            start = timeit.default_timer()

            Banking.open_grand_exchange_bank()

            Common.watch_click_image(dragon_hide_images, 0.7, 'Get dragon hides', sleep_time_after_click=1,
                                     current_step_region=Common.Bank_region)

            Banking.close_bank()

            # Cast tan leather five times to tan 25 hides
            for y in range(5):
                Common.watch_click_image(tan_leather_spell_images, 0.7, 'Cast tan leather ' + str(y),
                                         sleep_time_after_click=2, current_step_region=Common.Inventory_region)

            Banking.open_grand_exchange_bank()

            Common.watch_click_image(dragon_leather_images, 0.7, 'Deposit tanned leather', sleep_time_after_click=1,
                                     current_step_region=Common.Inventory_region)

            # Subtract iteration already ran and display countdown timer
            Display.stop_timer(start, loops_till_done - 1)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    cast_tan_leather()
    print('Done tanning leather!')
