moveCount = 0

def Cure():
    UnitHP_01 = Region(771,769,26,13)
    UnitHP_02 = Region(775,874,23,12)
    UnitHP_03 = Region(774,978,22,10)
    UnitHP_04 = Region(1062,770,23,12)
    UnitHP_05 = Region(1058,875,25,14)
    EmptyBlood = "EmptyBlood.png"
    shouldCure = False
    if UnitHP_01.exists(EmptyBlood):
        print "User 1 need cure"
        shouldCure = True
    else:
        print "User 1 is okay"
    if UnitHP_02.exists(EmptyBlood):
        print "User 2 need cure"
        shouldCure = True
    else:
        print "User 2 is okay"    
    if UnitHP_03.exists(EmptyBlood):
        print "User 3 need cure"
        shouldCure = True
    else:
        print "User 3 is okay"    
    if UnitHP_04.exists(EmptyBlood):
        print "User 4 need cure"
        shouldCure = True
    else:
        print "User 4 is okay"    
    if UnitHP_05.exists(EmptyBlood):
        print "User 5 need cure"
        shouldCure = True
    else:
        print "User 5 is okay"
    if not shouldCure:
        return
    
    CureRegion = Region(679,687,138,98)    
    CureRegion.mouseMove(SummonRegion)
    CureRegion.mouseDown(Button.LEFT)
    CureRegion.mouseMove(SummonRegion.offset(150,0))
    CureRegion.mouseUp(Button.LEFT)

    MagicRegion = Region(678,683,561,302)
    MagicMiddleCure = "MagicMiddleCure.png"
    MagicRegion.mouseMove(Location(958, 786))
    moveDownCount = 0
    while True:
        moveDownCount = moveDownCount + 1
        MagicRegion.mouseDown(Button.LEFT)
        MagicRegion.mouseMove(0, -50)
        MagicRegion.mouseUp(Button.LEFT)
        if MagicRegion.exists(MagicMiddleCure):
            click(getLastMatch())
            wait(0.5)
            click(Location(805, 738))
            break
        if moveDownCount == 10:
            print "Failed to find middle cure magic"
            exit
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
    SummonRegion = Region(970,704,75,56)
    SummonRegion.mouseMove(SummonRegion)
    SummonRegion.mouseDown(Button.LEFT)
    SummonRegion.mouseMove(SummonRegion.offset(150,0))
    SummonRegion.mouseUp(Button.LEFT)
    wait(1)
    if SummonRegion.exists("1476749894805.png"):
        click(Location(1181, 1028)) # go back
    else:
        click(Location(1086, 734))
    wait(0.5)

    # start Battle
    click(AutoRegion)
    # Battle Ends
    ResultRegion = Region(860,349,194,52)
    while not ResultRegion.exists("1476748616317.png"):
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
    #dragDrop(MoveRegion, MoveRegion.offset(100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(-100,0))
    dragDrop(MoveRegion, MoveRegion.offset(0,100))
    dragDrop(MoveRegion, MoveRegion.offset(0,-100))
    Battle()

while True:
    MoveAround()
    print "one round finished"
    if moveCount > 1000:
        break
    wait(1)
print "end"

