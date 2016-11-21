# To run this script, AUTO LB can be ON.
TARGET_LB_TYPE = 1  # 1 is attack, 2 is others\
BATTLE_COUNT_MAX = 14

import Utilities
reload(Utilities)

def doOffensiveLB():
    openMagicMenu(5)
    wait(2)
    if Utilities.isLBAvailable_BS(True):
        print "doOffensiveLB() : return true"
        return True
    else:
        print "offensive LB isn't available"
        return False

def doDefensiveLB():
    openMagicMenu(5)
    wait(2)
    if Utilities.isLBAvailable_BS(True):
        Utilities.defense(1)
        Utilities.defense(2)
        Utilities.defense(3)
        Utilities.defense(4)
        return True
    else:
        print "defensive LB isn't available"
        return False

def doLBaccordingToType():
    LB_EXECUTED = False
    if TARGET_LB_TYPE != 1:
        LB_EXECUTED = doDefensiveLB()
    else:
        LB_EXECUTED = doOffensiveLB()
    wait(0.5)
    print "LB_EXECUTED = ", LB_EXECUTED
    global numLBUsed
    if LB_EXECUTED:
        numLBUsed = numLBUsed + 1
    Utilities.manuallyKickOff()
    return LB_EXECUTED

LastTransferredUnitIdx = 3
def setRoundCommads():
    global LastTransferredUnitIdx
    Utilities.openMagicMenu(5)
    wait(0.5)
    if Utilities.isLBAvailable_BS(True):
        if not doLBaccordingToType():
            print "Error, LB should be ready but not"
            exit(1)
    else:
        print "Check teammates' LB..."
        # Target LB is not available, see if anyone can transfer
        Utilities.closeMagicMenu()
        wait(1)       
        checkCount = 0
        ToCheckUnitIdx = (LastTransferredUnitIdx + 1) % 4    
        while checkCount < 4:
            print "checking unit idx ", ToCheckUnitIdx
            if Utilities.lookHavingLB(ToCheckUnitIdx + 1):
                Utilities.openMagicMenu(ToCheckUnitIdx + 1)
                print "Checking unit num ", ToCheckUnitIdx + 1
                wait(0.5)
                if Utilities.isLBAvailable_BS(False):
                    print "unit ", ToCheckUnitIdx + 1, " has LB available"
                    # LB available, find transfer magic
                    magicTransfer = "magicTransfer.png"
                    result = Utilities.findTheMagic_BS(magicTransfer)
                    if result != None:
                        click(result)
                        wait(0.5)
                        click(Location(1044, 835))
                        wait(0.5)
                        click(Utilities.UNIT_CENTER_LOCATIONS[ToCheckUnitIdx])
                        wait(0.5)
                        LastTransferredUnitIdx = ToCheckUnitIdx
                        break
                Utilities.closeMagicMenu()
            ToCheckUnitIdx = (ToCheckUnitIdx + 1) % 4
            checkCount = checkCount + 1
        wait(1)

        if checkCount < 4:
            # transferred
            if not doLBaccordingToType():
                print "Error, LB should be ready but not"
                exit(1)
        else:
            # no one can transfer
            # just do normal kickoff
            print "ready to kickoff"
            Utilities.manuallyKickOff()

def doBattle():
    ResultRColore =  Color(0xBF,0xD1,0xDC) #java.awt.Color[r=191,g=209,b=220]
    #click(Location(883, 428))
    click(Location(890, 366))
    click(Location(752, 485))
    while True:
        setRoundCommads()
        wait(1)
        myRobot = JRobot()
        while Utilities.isAttacking_BS() and myRobot.getPixelColor(868, 340) != ResultRColore:
            print "round in progress"
            wait(1)
        if myRobot.getPixelColor(868, 340) == ResultRColore:
            print "battle ends"
            click(Location(868, 340))
            break;
battleCount = 0
numLBUsed = 0
start = time.time()
while True:
    Utilities.moveAround()
    wait(1)
    if Utilities.isInBattle():
        battleCount = battleCount + 1
        print "battle ", battleCount, " starts"
        doBattle()
        print "battle ", battleCount, " ends"
        if battleCount == BATTLE_COUNT_MAX:
            break
print "finished, took ", time.time() - start, " seconds to complete ", battleCount, " battles"
print "during which ", numLBUsed, " LB was used"