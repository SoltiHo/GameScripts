moveCount = 0
SUMMON_NUM = 5

import Utilities
reload(Utilities)

def Battle():
    wait(1)
    MenuRegion = Region(1146,979,112,99)
    if MenuRegion.exists("1476748187876.png"):
        print "not in battle..."
        return
    # In Battle
    print "Fight!!"
    # Cure() now working
    global moveCount
    moveCount = 0
    AutoRegion = Region(679,1014,129,57)
    while not AutoRegion.exists("1476748460074.png"):
        print "waiting auto"
        wait(1)
    click(Location(783, 518))
    click(Location(908, 462))
    #click(Location(822, 409))
    #click(Location(959, 445))
    
    # summon if available    
    Utilities.summonIfAvailable(SUMMON_NUM)

    # Cure if needed
    Utilities.doMiddleCureIfNeeded()

    # start Battle
    click(AutoRegion)
    # Battle Ends
    ResultRegion = Region(837,299,235,73)
    while not ResultRegion.exists("1479949016541.png"):
        print "waiting for battle to end"
        wait(1)
    print "Battle Ended"
    while not MenuRegion.exists("1476748187876.png"):
        click(Location(778, 455))
        wait(1)
    return



def MoveAround():
    global moveCount
    moveCount = moveCount + 1
    MoveRegion = Region(859,451,231,183)
    print "moving around..", moveCount
    dragDrop(MoveRegion, MoveRegion.offset(100,0))
    dragDrop(MoveRegion, MoveRegion.offset(-100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(0,100))
    #dragDrop(MoveRegion, MoveRegion.offset(0,-100))
    Battle()

while True:
    MoveAround()
    print "one round finished"
    if moveCount > 1000:
        break
    wait(1)
print "end"

