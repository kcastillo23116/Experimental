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
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: Default quantity set to Withdraw 14 as Item
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              Inventory menu open
equip items:        None
items in inventory: None
items in bank:  Bow String and unstrung bow: top row
"""
import timeit

import Common as Common
import Banking as Banking
import Display

defaultTimeBeforeClick = 1

# Images
withdraw_x_images = ['Images/Banking/WithdrawX.png', 'Images/Banking/WithdrawXSelected.png']
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
bow_string_images = ['Images/Fletching/Bowstring.png']
unstrung_bow_images = ['Images/Fletching/UnstrungBow.png']
string_bow_images = ['Images/Fletching/StringBow.png']
bow_images = ['Images/Fletching/Bow.png']


# Optional get_timing parameter can be used to do one run to get time per iteration to set up countdown timer with
# different scripts running one after another
def string_bows(item_count, get_timing=False, display_timer=False):
    try:
        loops_till_done = round(item_count / 14)

        for x in range(loops_till_done):
            Common.print_runtime(loops_till_done, 24, x)

            start = timeit.default_timer()

            Common.watch_click_image(bow_string_images, 0.7, 'Get bow strings',
                                     current_step_region=Common.Bank_region)
            Common.watch_click_image(unstrung_bow_images, 0.7,
                                     'Get unstrung bows and make sure they are in inventory',
                                     current_step_region=Common.Bank_region,
                                     next_step_image_paths=unstrung_bow_images,
                                     next_step_region=Common.Inventory_region)
            Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)
            Common.watch_click_image(bow_string_images, 0.7, 'Click inventory bowstring',
                                     current_step_region=Common.Inventory_region)
            Common.watch_click_image(unstrung_bow_images, 0.7, 'Click inventory unstrung bow', sleep_time_after_click=1,
                                     current_step_region=Common.Inventory_region)
            Common.watch_click_image(string_bow_images, 0.7, 'Click string bow', sleep_time_after_click=18,
                                     current_step_region=Common.Chatbox_region)
            Banking.open_grand_exchange_bank()
            Common.watch_click_image(bow_images, 0.7, 'Deposit longbows',
                                     current_step_region=Common.Inventory_region)

            # Get stop time now to calculate how much time to make a single iteration
            stop = timeit.default_timer()
            seconds_per_iteration = round(stop - start)

            # If we just want timing for displaying countdown timer return after first iteration here
            if get_timing:
                return seconds_per_iteration

            if display_timer:
                # Subtract iteration already ran
                Display.start_timer_thread(loops_till_done - 1, seconds_per_iteration)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


# Only run code below if running this script
if __name__ == '__main__':
    # Get how many from user
    itemCountString = input("How many items do you have? ")
    itemCount = int(itemCountString)

    Banking.open_grand_exchange_bank()

    # Sleep a second longer to give bank more time to come up so we can click the X quantity option
    Common.sleep_with_countdown(1)

    # Change withdraw quantity to X
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

    string_bows(itemCount, False, True)
