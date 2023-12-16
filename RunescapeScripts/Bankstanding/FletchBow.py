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
                    Quantity: All
location:           Grand exchange, directly in front of the right bottom bank teller box
                    click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
Menus:              Inventory menu open
equip items:        None
items in inventory: Knife at row 1 col 1
items in bank:  Logs(bank: row 1, column 2)
"""
import timeit

import Common as Common
import Banking as Banking
import Display

defaultTimeBeforeClick = 1

# Images
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
wood_images = ['Images/Wood.png', 'Images/Wood2.png']
banker_images = ['Images/Banker1.png', 'Images/Banker2.png',
                 'Images/Banker3.png', 'Images/Banker4.png',
                 'Images/Banker5.png', 'Images/Banker6.png',
                 'Images/Banker7.png', 'Images/Banker8.png']


# Optional get_timing parameter can be used to do one run to get time per iteration to set up countdown timer with
# different scripts running one after another
def fletch_bows(item_count, get_timing=False, display_timer=False):
    """
    Fletch loop
    """
    try:
        # Calculate how many loops needed
        loops_till_done = round(item_count / 28)

        for x in range(loops_till_done):
            Common.print_runtime(loops_till_done, 55, x)

            start = timeit.default_timer()

            Common.watch_click_image(['Images/Wood2.png'], 0.7, 'Get wood')
            Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)
            Common.watch_click_image(['Images/Knife.png'], 0.5, 'Click knife')
            Common.watch_click_image(wood_images, 0.7, 'Click inventory wood', sleep_time_after_click=1)
            Common.watch_click_image(['Images/LongBow.png', 'Images/LongBow.png'], 0.7,
                                     'Click longbow craft menu option', current_step_region=Common.Chatbox_region,
                                     sleep_time_after_click=49)
            Banking.open_grand_exchange_bank()
            Common.watch_click_image(['Images/LongBowInventory.png'], 0.7, 'Deposit longbows')

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
    fletch_bows(itemCount, False, True)
