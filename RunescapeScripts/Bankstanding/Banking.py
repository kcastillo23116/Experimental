"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players and NPCs
                    - 117HD OFF and GPU ON
                    - Turn off runelite Mouse Tooltips plugin
                    - Turn on Menu Entry Swapper runelite plugin, shift right click alch item and select
                      "swap left click Use"
Monitors:           4k or 3K display
bank settings:      - N/A
location:           - Right bankers at Grand Exchange
items in bank:      - None
Setup:              - Zoom all the way in and click the compass to center North
Objects to mark:    - Both Bankers on right side at grand exchange

"""

import Common as Common

# Constants
defaultTimeBeforeClick = 1

# Images
banker_images = ['Images/Banker1.png', 'Images/Banker2.png',
                 'Images/Banker3.png', 'Images/Banker4.png',
                 'Images/Banker5.png', 'Images/Banker6.png',
                 'Images/Banker7.png', 'Images/Banker8.png',
                 'Images/Banker9.png']
bank_option_images = ['Images/BankOption.png']
bank_withdraw_note_images = ['Images/Banking/WithdrawNote.png', 'Images/Banking/WithdrawNoteSelected.png']


def open_grand_exchange_bank():
    '''
    Opens bank at Grand exchange
    '''
    try:
        Common.watch_click_image(banker_images, 0.2, 'Right click banker and look for context menu options',
                                 True, next_step_image_paths=bank_option_images)
        Common.watch_click_image(bank_option_images, 0.7,
                                 'Click Open bank and look for withdraw as note to make sure bank window is open',
                                 next_step_image_paths=bank_withdraw_note_images, next_step_confidence=0.4,
                                 next_step_region=Common.Bank_bottom_options_region)

        # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')
