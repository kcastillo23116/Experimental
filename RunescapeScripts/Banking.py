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
                    - Set runelite menu entry swapper for bank teller to left click to Bank
Objects to mark:    - Both Bankers on right side at grand exchange
                        - With: NPC Indicator settings:
                            - Highlight Hull
                            - Highlight tile
                            - Highlight outline
                            - Highlight and Fill color: Cyan (FF00FFFF)
                            - Border width 2
"""

import Common as Common

# Constants
defaultTimeBeforeClick = 1

# Images
banker_images = ['Images/Banker1.png']
bank_option_images = ['Images/BankOption.png']
bank_withdraw_note_images = ['Images/Banking/WithdrawNote.png', 'Images/Banking/WithdrawNoteSelected.png']
deposit_inventory_images = ['Images/Banking/DepositInventory.png']
empty_inventory_images = ['Images/General/EmptyInventory.png']
bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']


def open_grand_exchange_bank():
    '''
    Opens bank at Grand exchange
    '''
    try:
        Common.watch_click_image(banker_images, 0.4, 'Click banker and look for context menu options',
                                 False, next_step_image_paths=bank_withdraw_note_images, next_step_confidence=0.4,
                                 next_step_region=Common.Bank_bottom_options_region)

    # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')


def close_bank():
    Common.watch_click_image(bank_close_images, 0.9, 'Close bank', sleep_time_after_click=1)


def deposit_inventory():
    Common.watch_click_image(deposit_inventory_images, 0.7,
                             'Deposit inventory and make sure inventory is empty before next step',
                             current_step_region=Common.Bank_bottom_options_region,
                             next_step_image_paths=empty_inventory_images,
                             next_step_region=Common.Bottom_half_game_screen_region)


def change_to_withdraw_x():
    Common.watch_click_image(['Images/Banking/WithdrawX.png'], 0.7, 'Change Withdraw Quantity to X',
                             False, 1, 10, None,
                             Common.Bank_bottom_options_region)

