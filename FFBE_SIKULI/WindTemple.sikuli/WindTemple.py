import java.awt.Robot as JRobot
import java.awt.Color as Color
import Utilities
reload(Utilities)
myRobot = JRobot()

selectFollower = False
start_phase = 0  # 0: beginning, 1: phase 1, 2: phase 2

num_LB_used = [0, 0, 0, 0, 0]
num_summon = 0
def revive(unitNum):
    # must use thunder summon
    # open healer menu
    Utilities.openMagicMenu(5) # assume the healer is at 5
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.fastClick(721, 831) # revive magic
    myRobot.delay(500)
    Utilities.fastClick(
            Utilities.UNIT_CENTER_LOCATIONS[unitNum - 1].getX(),
            Utilities.UNIT_CENTER_LOCATIONS[unitNum - 1].getY())
    myRobot.delay(500)
    returnColor = Color(19,209,208) # 1175, 1005
    if myRobot.getPixelColor(1175,1005) == returnColor: # not dead
        Utilities.fastClick(1175, 1005)
        myRobot.delay(500)
        Utilities.fastClick(1175, 1005)
        myRobot.delay(500)
        return False
    myRobot.delay(500)
    return True
    
def needCure():
    if Utilities.isBloodLowerThanHalf(1):
        return True
    if Utilities.isBloodLowerThanHalf(2):
        return True
    if Utilities.isBloodLowerThanHalf(3):
        return True
    if Utilities.isBloodLowerThanHalf(4):
        return True
    if Utilities.isBloodLowerThanHalf(5):
        return True
    return False

def Cure1(): # fire monster
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    middleCureColor = Color(98,146,173)
    if myRobot.getPixelColor(732, 817) != middleCureColor:
        # out of MP
        print 'Unit 4 out of MP'
        myRobot.delay(500)
        Utilities.fastClick(1175, 1005)
        myRobot.delay(500)
        return False
    Utilities.fastClick(732, 817)
    myRobot.delay(500)
    Utilities.fastClick(777, 726)
    myRobot.delay(500)
    return True

def Cure2():
    return False

def Cure3():
    return False

def Cure4():
    Utilities.openMagicMenu(4)
    myRobot.delay(500)
    middleCureColor = Color(127,146,125)
    if myRobot.getPixelColor(1031, 822) != middleCureColor:
        # out of MP
        print 'Unit 4 out of MP'
        myRobot.delay(500)
        Utilities.fastClick(1175, 1005)
        myRobot.delay(500)
        return False
    Utilities.fastClick(1031, 822)
    myRobot.delay(500)
    Utilities.fastClick(1025, 718)
    myRobot.delay(500)
    return True

def Cure5():
    return False

def doLB1():
    global num_LB_used
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    if Utilities.isLBAvailable_BS(True):
        # follow action depending on LB type
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_1')
        num_LB_used[0] += 1
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def doLB2():
    global num_LB_used
    Utilities.openMagicMenu(2)
    myRobot.delay(500)
    if Utilities.isLBAvailable_BS(True):
        # follow action depending on LB type
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_2')
        num_LB_used[1] += 1
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def doLB3():
    global num_LB_used
    Utilities.openMagicMenu(3)
    myRobot.delay(500)
    if Utilities.isLBAvailable_BS(True):
        # follow action depending on LB type
        num_LB_used[2] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_3')
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def doLB4():
    global num_LB_used
    Utilities.openMagicMenu(4)
    myRobot.delay(500)
    if Utilities.isLBAvailable_BS(True):
        # follow action depending on LB type
        num_LB_used[3] += 1
        myRobot.delay(500)
        Utilities.fastClick(1062, 723)
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_4')
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def doLB5():
    global num_LB_used
    Utilities.openMagicMenu(5)
    myRobot.delay(500)
    if Utilities.isLBAvailable_BS(True):
        # follow action depending on LB type
        num_LB_used[4] += 1
        myRobot.delay(500)
        Utilities.fastClick(1061, 829)
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_5')
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def setCommand():
    global num_LB_used
    global num_summon

    do_revive_unit = 0
    if not Utilities.isUnitAliveFast(1):
        revive(1)
        do_revive_unit = 5
    elif not Utilities.isUnitAliveFast(2):
        revive(2) 
        do_revive_unit = 5
    elif not Utilities.isUnitAliveFast(3):
        revive(3)
        do_revive_unit = 5
    elif not Utilities.isUnitAliveFast(4):
        revive(4)
        do_revive_unit = 5
    elif not Utilities.isUnitAliveFast(5):
        print 'master healer dead... game over'
        exit -1
    do_cure_unit = 0
    if needCure():
        cured = Cure1()
        do_cure_unit = 1
        if not cured:
            cured = Cure2()
            do_cure_unit = 2
        if not cured:
            cured = Cure3()
            do_cure_unit = 3
        if not cured:
            cured = Cure4()
            do_cure_unit = 4
        if not cured:
            print 'Cannot Cure'
            exit -1
    # after revive and cure, check LB
    if Utilities.lookHavingLB(1) and do_cure_unit != 1 and do_revive_unit != 1:
        num_LB_used[0] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_1')
    if Utilities.lookHavingLB(2) and do_cure_unit != 2 and do_revive_unit != 2:
        num_LB_used[1] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_2')
    if Utilities.lookHavingLB(3) and do_cure_unit != 3 and do_revive_unit != 3:
        num_LB_used[2] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_3')
    if Utilities.lookHavingLB(4) and do_cure_unit != 4 and do_revive_unit != 4:
        num_LB_used[3] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_4')
    if Utilities.lookHavingLB(5) and do_cure_unit != 5 and do_revive_unit != 5:
        num_LB_used[4] += 1
        Utilities.log('WindTempleLog.txt', 'LB_log', 'LB_5')
    myRobot.delay(1000)
    # summon if no LB and if available
    if do_cure_unit != 2 and do_revive_unit != 2 and (not Utilities.lookHavingLB(2)):
        if Utilities.summonIfAvailable(2): # earth
            num_summon += 1
            Utilities.log('WindTempleLog.txt', 'LB_log', 'Summon')
        else:
            Utilities.log('WindTempleLog.txt', 'LB_log', 'check but no Summon')
        myRobot.delay(1000)
    
    #Utilities.manuallyKickOff()
    Utilities.fastClick(745, 1032)  # click AUTO
    myRobot.delay(500)
    Utilities.fastClick(745, 1032)  # click AUTO
    myRobot.delay(500)

def issueCommandIfWaitingForOne(commandFunc):
    if Utilities.isWaitingForCommand():
        commandFunc()

def setBossBattleCommand():
    issueCommandIfWaitingForOne(setBossCommand)

def doBossBattle():
    Utilities.log('WindTempleLog.txt', 'LB_log', 'Boss Battle')
    myRobot.delay(1500)
    
    ResultRColor =  Color(245,247,249) # (865,339)
    totalTargetLBused = 0
    Utilities.waitForColorAndDo(865, 339, ResultRColor,
            func_while_wait=setBossBattleCommand)
    myRobot.delay(1000)   

def setBossCommand():
    if Utilities.lookHavingLB(1):
        num_LB_used[0] += 1
        print 'unit 1 LB = ', num_LB_used[0]
    if Utilities.lookHavingLB(2):
        num_LB_used[1] += 1
        print 'unit 2 LB = ', num_LB_used[1]
    if Utilities.lookHavingLB(3):
        num_LB_used[2] += 1
        print 'unit 3 LB = ', num_LB_used[2]
    if Utilities.lookHavingLB(4):
        num_LB_used[3] += 1
        print 'unit 4 LB = ', num_LB_used[3]
    # revive the Boss
    Utilities.openMagicMenu(5) # assume the healer is at 5
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.fastClick(721, 831) # revive magic
    myRobot.delay(800)
    Utilities.fastClick(757,1034)
    myRobot.delay(800)
    Utilities.fastClick(799, 374)
    myRobot.delay(800)
    Utilities.fastClick(745, 1032)  # click AUTO
    myRobot.delay(500)
    
    ResultRColor =  Color(245,247,249) # (865,339)

def setBattleCommand():
    issueCommandIfWaitingForOne(setCommand)

def doBattle():
    Utilities.log('WindTempleLog.txt', 'LB_log', 'do Battle')
    myRobot.delay(1500)
    Utilities.fastClick(796, 471)
    Utilities.fastClick(695, 377)
    Utilities.fastClick(864, 421)
    
    ResultRColor =  Color(245,247,249) # (865,339)
    totalTargetLBused = 0
    Utilities.waitForColorAndDo(865, 339, ResultRColor,
            func_while_wait=setBattleCommand)
    myRobot.delay(1000)

def walkUp(count, isBoundary=False):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveUpAndCheckBattle(doBattle, isBoundary=isBoundary)
        myRobot.delay(300)
        count -= 1
    return battle_count

def walkDown(count, isBoundary=False):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveDownAndCheckBattle(doBattle, isBoundary=isBoundary)
        myRobot.delay(300)
        count -= 1
    return battle_count

def walkRight(count, isBoundary=False):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveRightAndCheckBattle(doBattle, isBoundary=isBoundary)
        myRobot.delay(300)
        count -= 1
    return battle_count

def walkLeft(count, isBoundary=False):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveLeftAndCheckBattle(doBattle, isBoundary=isBoundary)
        myRobot.delay(300)
        count -= 1
    return battle_count

def walkThroughPhaseOne():
    Utilities.log('WindTempleLog.txt', 'LB_log', 'phase 1')
    MAX_BATTLE_COUNT = 14
    num_battle = 0
    
    num_battle += walkRight(13)
    num_battle += walkLeft(13)
    num_battle += walkUp(7)
    num_battle += walkRight(1)
    num_battle += walkUp(3)
    num_battle += walkRight(1)
    num_battle += walkUp(2)
    num_battle += walkLeft(2)
    num_battle += walkUp(5)  # entering page 2
    myRobot.delay(2000)
    
    # --- page 2 ---
    num_battle += walkUp(2)
    num_battle += walkLeft(7)
    num_battle += walkUp(4)
    num_battle += walkLeft(3)
    num_battle += walkDown(7)
    num_battle += walkRight(7) # 2nd mine
    num_battle += walkLeft(7)
    num_battle += walkUp(10)
    num_battle += walkLeft(4)
    num_battle += walkUp(7)
    num_battle += walkRight(7)
    num_battle += walkDown(4)
    num_battle += walkRight(6)  # Leaving Zone 1, do the remaining battles
    doRemainingBattles(MAX_BATTLE_COUNT - num_battle)

    # go to reference position
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(0, -270)
    myRobot.delay(2000)
    mouseUp(Button.LEFT)
    walkRight(1)
    walkUp(2)
    walkUp(5, isBoundary=True) # entering page 3, Zone 2
    myRobot.delay(2000)
    
def doRemainingBattles(numBattle, direction='UpDown'):
    while numBattle > 0:
        while True:
            Utilities.moveAround(direction)
            if Utilities.isInBattle():                
                doBattle()
                break
        numBattle -= 1
        print 'remaining battle count: ', numBattle

def walkThroughPhaseTwo():
    Utilities.log('WindTempleLog.txt', 'LB_log', 'Phase 2')
    MAX_BATTLE_COUNT = 15
    num_battle = 0
    
    num_battle += walkRight(8)
    num_battle += walkUp(2)        
    num_battle += walkRight(6) # 3rd Mine
    num_battle += walkLeft(6)
    num_battle += walkDown(2)
    num_battle += walkLeft(8)
    num_battle += walkUp(23)
    num_battle += walkLeft(10)
    num_battle += walkUp(4, isBoundary=True)
    num_battle += walkRight(10, isBoundary=True)
    num_battle += walkUp(1, isBoundary=True)
    # do the remaining battle
    doRemainingBattles(MAX_BATTLE_COUNT - num_battle, 'LeftRight')
    # go to reference position
    myRobot.delay(1000)
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(-270, 0)
    myRobot.delay(1000)
    mouseUp(Button.LEFT)

    walkRight(4, isBoundary=True)
    walkUp(3, isBoundary=True)  # entering page 4
    myRobot.delay(2000)

    # go meet Boss and catch 5th mine on the way
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(0, -270)
    myRobot.delay(4000)
    mouseUp(Button.LEFT)

    # "Yes" to Boss
    Utilities.fastClick(1125, 289)
    myRobot.delay(1500)
    # confirm
    Utilities.fastClick(1125, 289)
    myRobot.delay(2000)
    doBossBattle()
    myRobot.delay(1000)

    # exit
    Utilities.fastClick(1021, 422)
    myRobot.delay(1500)
    Utilities.fastClick(1141, 414)
    myRobot.delay(1500)

    Utilities.handleMissionEnd()
    myRobot.delay(1500)

def enterMission():
    # select mission (779, 364)
    Utilities.selectMission(779, 364)
    # select follower
    print 'select follower = ', selectFollower
    Utilities.selectFollowerAndLaunch(selectFollower)
    myRobot.delay(2000)

def process():
    global num_LB_used
    global num_summon
    global start_phase
    while True:
        start = time.time()
        Utilities.log('WindTempleLog.txt', 'LB_log', 'start time = ' + str(start), toDelete=True)
        num_LB_used = [0, 0, 0, 0, 0]
        num_summon = 0

        if start_phase <= 0:
            enterMission()
            myRobot.delay(3000)
        if start_phase <= 1:
            walkThroughPhaseOne()
            myRobot.delay(1000)
        if start_phase <= 2:
            walkThroughPhaseTwo()
        total_time = time.time() - start
        Utilities.log('WindTempleReport.csv', 'LB', str(total_time) + ',' + str(num_LB_used[0]) +
                    ',' + str(num_LB_used[1]) + ',' + str(num_LB_used[2]) + ',' + str(num_LB_used[3]) +
                    ',' + str(num_LB_used[4]) + ',' + str(num_summon))
        start_phase = 0

if __name__ == "__main__":
    process()
    #setCommand()
    #Utilities.boundaryGoRight()
    #doBattle()
    #doRemainingBattles(15, 'LeftRight')
    #Utilities.fastClick(796, 471)