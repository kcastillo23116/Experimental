"""
How to start:
client:             RuneLite with resizeable modern layout in runescape settings
                    and RuneLite Stretched mode enabled with Resizable scaling set to 75%
                    Runelite sidebar OPENED
Monitors:           4k middle monitor with all three on
bank settings:      Withdraw As: Item
                    Quantity: All
location:           Blast furnace bank chest directly in front of bank chest
                    click compass, so it's at default north and zoom out all the way and hold up arrow key to move
                    camera up
Menus:              None
equip items:        None
items in inventory: None
items in bank:  Coal (bank: row 1, column 1)
                Iron ore (bank: row 1, column 2)
                Stamina Potions (4 charges) (bank: row 1, column 3)
"""

from Skilling import Common as Common
import datetime

# Get how many from user
itemCountString = input("How many ores do you have? ")

# Calculate how many loops needed
itemCount = int(itemCountString)
# multiply by two since have to load both coal and iron
loopsTillDone = round(itemCount / 27) * 2

Common.move_mouse_and_left_click(1729, 1106, 2, "Bank Chest")
# Common.move_mouse_and_left_click(1230, 283, 2, "Get Stamina potion")

for x in range(loopsTillDone):
    print("Loop: ", x, "/", loopsTillDone)
    runtime = ((loopsTillDone - x) * 30)
    dtg = str(datetime.timedelta(seconds=runtime))
    print("Approx time till done: ", dtg)

    # Load ores
    Common.move_mouse_and_left_click(975, 292, 2, "Coal")
    Common.move_mouse_and_left_click(2016, 84, 2, "Close bank")
    Common.move_mouse_and_left_click(1445, 583, 1, "Coal Conveyer")
    Common.move_mouse_and_left_click(2155, 1819, 8, "Bank chest")
    Common.move_mouse_and_left_click(1096, 283, 8, "Iron Ore")
    Common.move_mouse_and_left_click(2042, 105, 2, "Close bank")

    # Fill up water bucket on way to dropping off iron ore
    Common.move_mouse_and_left_click(3101, 1349, 1, "Click bucket of water")
    Common.move_mouse_and_left_click(1340, 1089, 1, "Click water well")

    # Load iron ore
    Common.move_mouse_and_left_click(1707, 552, 4, "Iron ore Conveyer")
    # Common.move_mouse_and_left_click(746, 1951, 3, "Confirm in case of level")

    # Cool down get and deposit bars
    Common.move_mouse_and_left_click(3101, 1349, 7, "Click bucket of water")
    Common.move_mouse_and_left_click(1592, 1312, 2, "Use water on Bar dispenser")
    Common.move_mouse_and_left_click(1720, 1103, 4, "Click Bar dispenser")
    Common.move_mouse_and_left_click(685, 1818, 2, "Get bars")
    Common.move_mouse_and_left_click(2308, 1592, 2, "Bank chest")
    Common.move_mouse_and_left_click(3323, 1349, 7, "Deposit bars")

    # Drink stamina potion every second run since it should be almost out by then
    if x % 2 == 0:
        Common.move_mouse_and_left_click(2016, 84, 2, "Close bank")
        Common.move_mouse_and_left_click(2988, 1355, 2, "Drink stamina potion")
        Common.move_mouse_and_left_click(1729, 1106, 2, "Bank Chest")

