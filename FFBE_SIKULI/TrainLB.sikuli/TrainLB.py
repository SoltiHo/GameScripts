# To run this script, AUTO LB can be ON.
TARGET_LB_TYPE = 1  # 1 is attack, 2 is others\
BATTLE_COUNT_MAX = 14

numLBUsed = 0

import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import java.awt.Color as Color
from sikuli import *
import Utilities
reload(Utilities)

myRobot = JRobot()
def selectTransferUnit1():
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    Utilities.scrollMenuDown()
    myRobot.delay(200)    
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    myRobot.mouseMove(721, 804)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit2():
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    myRobot.mouseMove(730, 892)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit3():
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    myRobot.mouseMove(1041, 842)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit4():
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    Utilities.scrollMenuDown()
    myRobot.delay(200)
    myRobot.mouseMove(1034, 889)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)
    
def doOffensiveLB(toSelectTargetLB):
    if toSelectTargetLB:
        Utilities.openMagicMenu(5)
        myRobot.delay(500)
        if Utilities.isLBAvailable_BS(True):
            print "doOffensiveLB() : return true"
            return True
        else:
            print "offensive LB isn't available"
            return True
    else:
        print "targetLB is already selected"
        return True

def doDefensiveLB(toSelectTargetLB):
    openMagicMenu(5)
    wait(1)
    if Utilities.isLBAvailable_BS(True):
        Utilities.defense(1)
        Utilities.defense(2)
        Utilities.defense(3)
        Utilities.defense(4)
        return True
    else:
        print "defensive LB isn't available"
        return False

def doLBaccordingToType(toSelectTargetLB):
    LB_EXECUTED = False
    if TARGET_LB_TYPE != 1:
        LB_EXECUTED = doDefensiveLB(toSelectTargetLB)
    else:
        LB_EXECUTED = doOffensiveLB(toSelectTargetLB)
    wait(1)
    print "LB_EXECUTED = ", LB_EXECUTED
    global numLBUsed
    if LB_EXECUTED:
        numLBUsed = numLBUsed + 1
    Utilities.manuallyKickOff()
    return LB_EXECUTED

LastTransferredUnitIdx = 3
def setRoundCommads():
    global LastTransferredUnitIdx
    #wait(0.5)
    targetLBavailable = False
    if Utilities.lookHavingLB(5):
        Utilities.openMagicMenu(5)
        wait(1)
        if Utilities.isLBAvailable_BS(True):
            targetLBavailable = True
        else:
            Utilities.closeMagicMenu()
        wait(1)
    if targetLBavailable:
        if not doLBaccordingToType(False):
            print "Error, LB should be ready but not"
            exit(1)
    else:
        print "Check teammates' LB..."
        # Target LB is not available, see if anyone can transfer
        
        #wait(1)       
        checkCount = 0
        ToCheckUnitIdx = (LastTransferredUnitIdx + 1) % 4    
        while checkCount < 4:
            print "checking unit idx ", ToCheckUnitIdx
            if Utilities.lookHavingLB(ToCheckUnitIdx + 1):
                Utilities.openMagicMenu(ToCheckUnitIdx + 1)
                print "Checking unit num ", ToCheckUnitIdx + 1
                #wait(0.5)
                if Utilities.isLBAvailable_BS(False):
                    print "unit ", ToCheckUnitIdx + 1, " has LB available"
                    myRobot.delay(500)
                    # LB available, find transfer magic
                    if ToCheckUnitIdx + 1 == 1:
                        selectTransferUnit1()
                    elif ToCheckUnitIdx + 1 == 2:
                        selectTransferUnit2()
                    elif ToCheckUnitIdx + 1 == 3:
                        selectTransferUnit3()
                    else:
                        selectTransferUnit4()

                    myRobot.delay(500)
                    click(Location(1044, 835))
                    myRobot.delay(500)
                    click(Utilities.UNIT_CENTER_LOCATIONS[ToCheckUnitIdx])
                    myRobot.delay(500)
                    LastTransferredUnitIdx = ToCheckUnitIdx
                    break
                Utilities.closeMagicMenu()
            ToCheckUnitIdx = (ToCheckUnitIdx + 1) % 4
            checkCount = checkCount + 1
        #wait(1)

        if checkCount < 4:
            # transferred
            if not doLBaccordingToType(True):
                print "Error, LB should be ready but not"
                exit(1)
        else:
            # no one can transfer
            # just do normal kickoff
            print "ready to kickoff"
            Utilities.manuallyKickOff()

def doBattle():
    ResultRColor =  Color(0xBF,0xD1,0xDC) #java.awt.Color[r=191,g=209,b=220]
    #click(Location(883, 428))
    wait(1)
    click(Location(890, 366))
    click(Location(752, 485))
    while True:
        wait(1)
        if myRobot.getPixelColor(868, 340) == ResultRColor:
            print "battle ends"
            click(Location(868, 340))
            break;

        setRoundCommads()
        wait(1)
        while Utilities.isAttacking_BS() and myRobot.getPixelColor(868, 340) != ResultRColor:
            print "round in progress"
            wait(1)
        print "checking if battle ends..."
        if myRobot.getPixelColor(868, 340) == ResultRColor:
            print "battle ends"
            click(Location(868, 340))
            break;

def doTrainLB():
    start = time.time()
    battleCount = 0
    global numLBUsed
    while True:
        Utilities.moveAround()
        #wait(1)
        if Utilities.isInBattle():
            battleCount = battleCount + 1
            print "battle ", battleCount, " starts"
            doBattle()
            print "battle ", battleCount, " ends"
            if battleCount == BATTLE_COUNT_MAX:
                break
        wait(1)
    print "finished, took ", time.time() - start, " seconds to complete ", battleCount, " battles"
    print "during which ", numLBUsed, " LB was used"    

if __name__ == "__main__":
    doTrainLB()
