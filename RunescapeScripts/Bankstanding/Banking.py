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
                 'Images/Banker7.png', 'Images/Banker8.png']


def open_grand_exchange_bank():
    '''
    Opens bank at Grand exchange
    '''
    try:
        Common.click_image(banker_images, 0.3, defaultTimeBeforeClick, 'Right click banker', True)
        Common.click_image(['Images/BankOption.png'], 0.7, defaultTimeBeforeClick, 'Click Open bank')

        # Image not found error, stop loop and print message
    except ValueError as error:
        print(error, 'Stopping process')
