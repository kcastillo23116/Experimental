"""
How to start:
client:             - RuneLite with resizeable modern layout in runescape settings
                      and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    - Runelite sidebar CLOSED
                    - Turn on object markers plugin and Shift+Right click bank to mark it
                    - Turn off menu opacity in runecape options: Interfaces > resizable > Transparent side panel
                    - Turn on entity hider in runelite to hide other players
                    - 117HD off and enable GPU so it runs smoother
                    - Turnoff screenshot notifications on runelite (plugins > Screenshots) (Level up notifications get in way)
                    - run ::toggleroofs in runescape chat to turn off roofs
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           - Grand exchange, in front of the left teller box
                    - click compass, so it's at default north and zoom in, hold up arrow to get camera all the way up
                      and zoom all the way out
                    - Mark bench on NE corner of grand exchange
Menus:              Inventory menu open
equip items:        None
items in inventory: Tinderbox, four other items to block out second inventory row
items in bank: Oak Logs
"""

from Skilling import Common as Common

# 23 items since tinderbox hover blocks last four logs
inventoryItemCount = 23

# Get how many from user
itemCountString = input("How many items do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
loopsTillDone = round(itemCount / inventoryItemCount )

try:
    # Open bank to start
    grandexchange_bank_images = ['Images/GrandexchangeBankLeft2.png',
                                 'Images/GrandexchangeBank.png',
                                 'Images/GrandexchangeBank.png']
    bank_close_images = ['Images/BankClose.png', 'Images/BankClose2.png']
    wood_images = ['Images/WillowLogs.png', 'Images/WillowLogs.png']
    bank_pillar_images = ['Images/GrandexchangePillar2.png',
                          'Images/GrandexchangePillar.png']
    firemaking_starting_point_images = ['Images/GrandexchangeFiremakingBench.png',
                                        'Images/GrandexchangeFiremakingTree4.png',
                                        'Images/GrandexchangeFiremakingTree3.png',
                                        'Images/GrandexchangeFiremakingTree2.png',
                                        'Images/GrandexchangeFiremakingTree.png',
                                        'Images/GrandexchangeFiremakingTreeStump.png']

    Common.click_image(grandexchange_bank_images, 0.7, 1, 'Click bank booth')

    for x in range(loopsTillDone):
        Common.print_runtime(loopsTillDone, 65, x)

        Common.click_image(['Images/Wood2.png'], 0.7, 3, 'Get wood')
        Common.click_image(bank_close_images, 0.9, 1, 'Close bank')
        Common.click_image(['Images/GrandexchangeVoteMapIcon.png'], 0.9, 1, 'Move to vote icon')
        Common.click_image(firemaking_starting_point_images, 0.9, 6, 'Move to starting point')

        # Burn all logs in inventory
        for x in range(inventoryItemCount ):
            Common.click_image(['Images/Tinderbox.png'], 0.7, 4, 'Click tinderbox')
            Common.click_image(wood_images, 0.7, 1, 'Click inventory wood')

        Common.click_image(['Images/GrandexchangeVoteMapIcon.png'], 0.9, 3, 'Move to vote icon')
        Common.click_image(bank_pillar_images, 0.9, 6, 'Move to bank using pillars')
        Common.click_image(grandexchange_bank_images, 0.7, 5, 'Click bank booth')

# Image not found error, stop loop and print message
except ValueError as error:
    print(error, 'Stopping process')

