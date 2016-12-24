# To run this script, AUTO LB can be ON.
TARGET_LB_TYPE = 1  # 1 is attack, 2 is others\
TARGET_LB_SELECT_TEAM = True
BATTLE_COUNT_MAX = 14


import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import java.awt.Color as Color
from sikuli import *
import Utilities
reload(Utilities)

myRobot = JRobot()
def selectTransferUnit1():
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    myRobot.mouseMove(788, 940)
    myRobot.delay(300)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit2():
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    myRobot.mouseMove(759, 837)
    myRobot.delay(300)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit3():
    Utilities.scrollMenuDown_fast()
    myRobot.delay(400)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(400)
    myRobot.mouseMove(780, 922)
    myRobot.delay(300)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectTransferUnit4():
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(300)
    myRobot.mouseMove(780, 940)
    myRobot.delay(300)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)
    
def doOffensiveLB(toSelectTargetLB):
    if toSelectTargetLB:
        Utilities.openMagicMenu(5)
        myRobot.delay(500)
        if Utilities.isLBAvailable_BS(True):
            print "doOffensiveLB() : return true"
            myRobot.delay(1000)
            return True
        else:
            print "offensive LB isn't available"
            return False
    else:
        print "targetLB is already selected"
        return True

def doDefensiveLB(toSelectTargetLB):
    if toSelectTargetLB:
        wait(1)
        Utilities.openMagicMenu(5)
        wait(1)
        if Utilities.isLBAvailable_BS(True):
            myRobot.delay(1000)
            click(Location(1068, 830)) # select team
            myRobot.delay(1000)
            Utilities.defense(1)
            myRobot.delay(500)
            Utilities.defense(2)
            myRobot.delay(500)
            Utilities.defense(3)
            myRobot.delay(500)
            Utilities.defense(4)
            myRobot.delay(500)
            Utilities.defense(6)
            myRobot.delay(500)
            return True
        else:
            print "defensive LB isn't available"
            return False
    else:
        print "targetLB is already selected"
        Utilities.defense(1)
        myRobot.delay(500)
        Utilities.defense(2)
        myRobot.delay(500)
        Utilities.defense(3)
        myRobot.delay(500)
        Utilities.defense(4)
        myRobot.delay(500)
        Utilities.defense(6)
        myRobot.delay(500)
        return True

# toSummonUnitNum, after selecting LB, which unit to summon. 0 means no summon
def doLBaccordingToType(toSelectTargetLB, toSummonUnitNum):
    LB_EXECUTED = False
    #Utilities.log('LbCheck.csv', 'check', '1,')
    if TARGET_LB_TYPE != 1:
        LB_EXECUTED = doDefensiveLB(toSelectTargetLB)
    else:
        LB_EXECUTED = doOffensiveLB(toSelectTargetLB)
    #wait(1)
    print "LB_EXECUTED = ", LB_EXECUTED
    print "toSummonUnitNum = ", toSummonUnitNum
    if toSummonUnitNum != 0:
        Utilities.summonIfAvailable(toSummonUnitNum)
    myRobot.mouseMove(890, 366)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(752, 485)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    Utilities.manuallyKickOff()
    return LB_EXECUTED

LastTransferredUnitIdx = 3
def setRoundCommads(allowSummon):
    global LastTransferredUnitIdx
    #wait(0.5)
    targetLBavailable = False
    targetLBUsed = 0
    if Utilities.lookHavingLB(5):
        Utilities.openMagicMenu(5)
        wait(1)
        if Utilities.isLBAvailable_BS(True):
            myRobot.delay(1000)
            if TARGET_LB_TYPE != 1:
                click(Location(1068, 830)) # select team
                myRobot.delay(1000)
            targetLBavailable = True
        else:
            Utilities.closeMagicMenu()
        wait(1)
    summonNum = 1 if allowSummon else 0
    if targetLBavailable:
        if not doLBaccordingToType(False, summonNum):
            print "Error, LB should be ready but not"
            exit(1)
        targetLBUsed += 1
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
                myRobot.delay(500)
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

                    myRobot.delay(1000)
                    click(Location(1044, 835))                    
                    myRobot.delay(1000)
                    click(Utilities.UNIT_CENTER_LOCATIONS[ToCheckUnitIdx])
                    myRobot.delay(1000)
                    LastTransferredUnitIdx = ToCheckUnitIdx
                    break
                Utilities.closeMagicMenu()
            ToCheckUnitIdx = (ToCheckUnitIdx + 1) % 4
            checkCount = checkCount + 1
        #wait(1)

        if allowSummon and LastTransferredUnitIdx == 1:
            summonNum = 2
        if checkCount < 4:
            # transferred
            if not doLBaccordingToType(True, summonNum):
                print "Error, LB should be ready but not"
                exit(1)
            targetLBUsed += 1
        else:
            # no one can transfer
            # just do normal kickoff
            if allowSummon:
                Utilities.summonIfAvailable(1)
            print "ready to kickoff"
            myRobot.mouseMove(890, 366)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            myRobot.mouseMove(752, 485)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            Utilities.manuallyKickOff()
    return targetLBUsed

def doBattle(allowSummon):
    ResultRColor =  Color(0xBF,0xD1,0xDC) #java.awt.Color[r=191,g=209,b=220]
    #click(Location(883, 428))
    wait(1)
    totalTargetLBused = 0
    while True:
        wait(1)
        if myRobot.getPixelColor(868, 340) == ResultRColor:
            print "battle ends"
            click(Location(868, 340))
            break;

        totalTargetLBused += (setRoundCommads(allowSummon))
        wait(1)
        while Utilities.isAttacking_BS() and myRobot.getPixelColor(868, 340) != ResultRColor:
            print "round in progress"
            #click(Location(712, 745))
            wait(1)
        print "checking if battle ends..."
        if myRobot.getPixelColor(868, 340) == ResultRColor:
            print "battle ends"
            click(Location(868, 340))
            break;
    return totalTargetLBused


def doTrainLB(battle_max_count, direction):
    start = time.time()
    battleCount = 0
    numLBUsed = 0
    while True:
        Utilities.moveAround(direction)
        #wait(1)
        if Utilities.isInBattle():
            battleCount = battleCount + 1
            print "battle ", battleCount, " starts"
            numLBUsed += (doBattle(False))
            print "battle ", battleCount, " ends"
            if battleCount == battle_max_count:
                break
            wait(1)
    TimeSpent = time.time() - start
    return [TimeSpent, numLBUsed]

if __name__ == "__main__":
    #doBattle(True)
    #selectTransferUnit4()
    #doOffensiveLB(True)
    #wait(5)
    doTrainLB(BATTLE_COUNT_MAX, 'LeftRight')
