import java.awt.Robot as JRobot
import java.awt.Color as Color
import Utilities
reload(Utilities)
myRobot = JRobot()

selectFollower = True
start_phase = 1 # 0: beginning, 1: phase 1, 2: phase 2
STEP_WAIT = 400
buyStrength = True

num_LB_used = [0, 0, 0, 0, 0]
num_summon = 0
num_round = 0
alwaysSteal = True
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
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_1')
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
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_2')
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
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_3')
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
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_4')
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
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_5')
    else:
        Utilities.closeMagicMenu()
    myRobot.delay(500)

def reviveAndCure():
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

def doSteal():
    if not Utilities.lookHavingLB(5):
        Utilities.openMagicMenu(5)
        myRobot.delay(500)
        Utilities.fastClick(745, 819)
    myRobot.delay(500)

def followerAttackOnly():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[5])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(500)
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[5])
    mouseDown(Button.LEFT)
    mouseMove(0, -100)
    mouseUp(Button.LEFT)

def setCommand():
    global num_LB_used
    global num_summon
    global num_round
    global alwaysSteal
    do_cure_unit = 0
    do_revive_unit = 0
    num_round = num_round + 1
    #reviveAndCure()
    # after revive and cure, check LB
    if Utilities.lookHavingLB(1) and do_cure_unit != 1 and do_revive_unit != 1:
        num_LB_used[0] += 1
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_1')
    if Utilities.lookHavingLB(2) and do_cure_unit != 2 and do_revive_unit != 2:
        num_LB_used[1] += 1
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_2')
    if Utilities.lookHavingLB(3) and do_cure_unit != 3 and do_revive_unit != 3:
        num_LB_used[2] += 1
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_3')
    if Utilities.lookHavingLB(4) and do_cure_unit != 4 and do_revive_unit != 4:
        num_LB_used[3] += 1
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_4')
    if Utilities.lookHavingLB(5) and do_cure_unit != 5 and do_revive_unit != 5:
        num_LB_used[4] += 1
        Utilities.log('FireTempleLog.txt', 'LB_log', 'LB_5')
    myRobot.delay(1000)
    # summon if no LB and if available
    #if do_cure_unit != 2 and do_revive_unit != 2 and (not Utilities.lookHavingLB(2)):
    #    if Utilities.summonIfAvailable(2): # earth
    #        num_summon += 1
    #        Utilities.log('FireTempleLog.txt', 'LB_log', 'Summon')
    #    else:
    #        Utilities.log('FireTempleLog.txt', 'LB_log', 'check but no Summon')
    #    myRobot.delay(1000)

    #if alwaysSteal or num_round == 1:
    #    doSteal()
    #myRobot.delay(1000)
    #if Utilities.lookAbleToSummon():
    #    Utilities.summonIfAvailable(2)
    followerAttackOnly()
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
    Utilities.log('FireTempleLog.txt', 'LB_log', 'Boss Battle')
    myRobot.delay(1500)
    while not Utilities.isWaitingForCommand():
        myRobot.delay(500)
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
    global num_round
    num_round = 0
    Utilities.log('FireTempleLog.txt', 'LB_log', 'do Battle')
    myRobot.delay(1500)
    while not Utilities.isWaitingForCommand():
        myRobot.delay(500)
    Utilities.fastClick(794, 541)
    myRobot.delay(300)
    Utilities.fastClick(888, 541)
    myRobot.delay(300)
    Utilities.fastClick(794, 386)
    myRobot.delay(300)
    #Utilities.fastClick(888, 386)
    #myRobot.delay(300)

    ResultRColor =  Color(245,247,249) # (865,339)
    totalTargetLBused = 0
    Utilities.waitForColorAndDo(865, 339, ResultRColor,
            func_while_wait=setBattleCommand)
    myRobot.delay(1000)

def walkUp(count, isBoundary=False, detectBattle=True):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveUpAndCheckBattle(doBattle, isBoundary=isBoundary, detectBattle=detectBattle)
        myRobot.delay(STEP_WAIT)
        count -= 1
    return battle_count

def walkDown(count, isBoundary=False, detectBattle=True):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveDownAndCheckBattle(doBattle, isBoundary=isBoundary, detectBattle=detectBattle)
        myRobot.delay(STEP_WAIT)
        count -= 1
    return battle_count

def walkRight(count, isBoundary=False, detectBattle=True):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveRightAndCheckBattle(doBattle, isBoundary=isBoundary, detectBattle=detectBattle)
        myRobot.delay(STEP_WAIT)
        count -= 1
    return battle_count

def walkLeft(count, isBoundary=False, detectBattle=True):
    battle_count = 0
    while count > 0:
        battle_count += Utilities.MoveLeftAndCheckBattle(doBattle, isBoundary=isBoundary, detectBattle=detectBattle)
        myRobot.delay(STEP_WAIT)
        count -= 1
    return battle_count

def walkThroughPhaseOne():
    Utilities.log('FireTempleLog.txt', 'LB_log', 'phase 1')
    MAX_BATTLE_COUNT = 14
    num_battle = 0

    num_battle += walkLeft(1, isBoundary=True)
    # now, complete the rest battles
    doRemainingBattles(MAX_BATTLE_COUNT - num_battle)
    # ref point
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(0, -200)
    myRobot.delay(2000)
    mouseUp(Button.LEFT)
    myRobot.delay(500)
    
    num_battle += walkRight(1)
    num_battle += walkUp(3)
    # num_battle += walkUp(15, isBoundary=True)

    # go get 1st mine
    num_battle += walkLeft(4)
    num_battle += walkDown(2) # 1st mine
    num_battle += walkUp(2)
    
    # go get 2nd mine
    num_battle += walkRight(16)
    num_battle += walkRight(3, isBoundary=True)
    num_battle += walkRight(1, isBoundary=True, detectBattle=False)  # switch page
    myRobot.delay(2000)
    
    # now at page 2
    num_battle += walkRight(5, isBoundary=True)
    #myRobot.delay(500)
    num_battle += walkUp(6)
    num_battle += walkRight(11)
    num_battle += walkDown(8)
    num_battle += walkLeft(3)
    num_battle += walkDown(7)
    
    num_battle += walkLeft(1) # almost bottom
    num_battle += walkDown(5, isBoundary=True)
    num_battle += walkRight(7, isBoundary=True) # right turn to hidden path
    num_battle += walkDown(4, isBoundary=True)
    num_battle += walkRight(1, isBoundary=True) # 2nd mine
    num_battle += walkLeft(1, isBoundary=True)

    # now leave page2
    num_battle += walkUp(4, isBoundary=True)
    num_battle += walkLeft(7, isBoundary=True)
    num_battle += walkUp(5, isBoundary=True)
    num_battle += walkRight(1) # almost bottom

    num_battle += walkUp(7)
    num_battle += walkRight(3)
    num_battle += walkUp(8)
    num_battle += walkLeft(11)
    num_battle += walkDown(6)
    
    num_battle += walkLeft(5, isBoundary=True)
    num_battle += walkLeft(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000) # now back to page 1

    num_battle += walkLeft(4, isBoundary=True)  # switch page
    num_battle += walkLeft(11)
    # go up to page 3
    num_battle += walkUp(5)
    num_battle += walkUp(1, detectBattle=False)
    myRobot.delay(2000) 
    
    # now at page 3
    num_battle += walkUp(3, isBoundary=True)
    num_battle += walkLeft(1, isBoundary=True)
    
    # now go to zone 2
    num_battle += walkUp(5, isBoundary=True)
    num_battle += walkLeft(10)
    
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
    Utilities.log('FireTempleLog.txt', 'LB_log', 'Phase 2')
    MAX_BATTLE_COUNT = 15
    num_battle = 0
    # complete the remaining battle here
    doRemainingBattles(MAX_BATTLE_COUNT - num_battle)
    # ref point
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(0, 200)
    myRobot.delay(2000)
    mouseUp(Button.LEFT)
    myRobot.delay(500)

    #num_battle += walkDown(10, isBoundary=True)
    num_battle += walkLeft(4, isBoundary=True)
    num_battle += walkLeft(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)
    # now at page 4
    num_battle += walkLeft(8, isBoundary=True)
    num_battle += walkLeft(9)
    num_battle += walkDown(4)
    num_battle += walkDown(5, isBoundary=True)
    num_battle += walkDown(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)
    
    # now at page 5
    num_battle += walkDown(12, isBoundary=True)
    num_battle += walkRight(10)
    num_battle += walkUp(11, isBoundary=True)
    num_battle += walkUp(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # back to page 4 small island for mine 3
    num_battle += walkUp(3, isBoundary=True) # 3rd mine
    num_battle += walkDown(3, isBoundary=True)
    num_battle += walkDown(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now back to page 5, reverse it
    num_battle += walkDown(11, isBoundary=True)
    num_battle += walkLeft(10)
    num_battle += walkUp(12, isBoundary=True)
    num_battle += walkUp(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now back to page 4, reverse it
    num_battle += walkUp(5, isBoundary=True)
    num_battle += walkUp(3)
    num_battle += walkRight(9)
    num_battle += walkRight(8, isBoundary=True)
    num_battle += walkRight(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now back to page 3
    num_battle += walkRight(4, isBoundary=True)
    num_battle += walkUp(10, isBoundary=True)
    num_battle += walkRight(22)
    num_battle += walkDown(4)
    num_battle += walkDown(7, isBoundary=True)
    num_battle += walkRight(4, isBoundary=True)
    num_battle += walkRight(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now at page 6
    num_battle += walkRight(8, isBoundary=True)
    num_battle += walkUp(1)
    num_battle += walkRight(12)
    num_battle += walkUp(8, isBoundary=True)
    num_battle += walkLeft(9, isBoundary=True)
    num_battle += walkUp(1, isBoundary=True)
    num_battle += walkLeft(4, isBoundary=True)
    num_battle += walkDown(2, isBoundary=True)  # 4th mine
    # now reverse, go back
    num_battle += walkUp(2, isBoundary=True)
    num_battle += walkRight(4, isBoundary=True)
    num_battle += walkDown(1, isBoundary=True)
    num_battle += walkRight(9, isBoundary=True)
    num_battle += walkDown(8, isBoundary=True)



    # go to reference position
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(-200, 0)
    myRobot.delay(2000)
    mouseUp(Button.LEFT)
  
    num_battle += walkDown(1)
    num_battle += walkLeft(7, isBoundary=True)
    num_battle += walkLeft(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now back to page 3
    num_battle += walkLeft(4, isBoundary=True)
    num_battle += walkUp(11, isBoundary=True)
    num_battle += walkLeft(11)
    num_battle += walkUp(10, isBoundary=True)
    num_battle += walkUp(1, isBoundary=True, detectBattle=False)
    myRobot.delay(2000)

    # now at page 7
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
    Utilities.fastClick(1125, 289)
    myRobot.delay(2000)
    global alwaysSteal
    alwaysSteal = False
    doBattle()
    alwaysSteal = True
    myRobot.delay(2000)

    # exit
    Utilities.fastClick(1021, 422)
    myRobot.delay(1500)
    Utilities.fastClick(1141, 414)
    myRobot.delay(1500)

    Utilities.handleMissionEnd()
    myRobot.delay(1500)

def enterMission():
    FireMissionColor = Color(18, 69, 39) # (738, 384)
    Utilities.waitForColorAndDo(738, 384, FireMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 83, 196) # (954, 923)
    if buyStrength:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
                func_while_wait=Utilities.buyStrength)
    else:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)
         

    # select follower
    followerColor = Color(145,60,32) # (1015,223)    
    if selectFollower:
        Utilities.waitForColorAndDo(1015, 223, followerColor, 
                func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
    else:
        def waitAndSelectNoFollower():
            myRobot.delay(500)
            func_after_wait=Utilities.selectStranger()
        #followerColor = Color(22, 41, 54) # (916, 248)
        Utilities.waitForColorAndDo(1096, 223, followerColor, 
            func_after_wait=waitAndSelectNoFollower)

    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

def process():
    global num_LB_used
    global num_summon
    global start_phase
    while True:
        start = time.time()
        Utilities.log('FireTempleLog.txt', 'LB_log', 'start time = ' + str(start), toDelete=True)
        num_LB_used = [0, 0, 0, 0, 0]
        num_summon = 0

        if start_phase <= 0:
            enterMission()
            myRobot.delay(3000)
        if start_phase <= 1:
            walkThroughPhaseOne()
            myRobot.delay(2000)
        if start_phase <= 2:
            walkThroughPhaseTwo()
            myRobot.delay(2000)
        total_time = time.time() - start
        Utilities.log('FireTempleReport.csv', 'LB', str(total_time) + ',' + str(num_LB_used[0]) +
                    ',' + str(num_LB_used[1]) + ',' + str(num_LB_used[2]) + ',' + str(num_LB_used[3]) +
                    ',' + str(num_LB_used[4]) + ',' + str(num_summon))
        start_phase = 0

if __name__ == "__main__":
    #doRemainingBattles(15, 'LeftRight')
    #walkThroughPhaseTwo()
    doRemainingBattles(50) #, direction='LeftRight')
    process()
    #enterMission()
    #setCommand()
    #doBattle()
