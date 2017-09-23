import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
import time
from sikuli import *
reload(Utilities)
myRobot = JRobot()

def enterStory(X, Y):
    menuColor = Color(213, 174, 163) # (1195, 224)
    if myRobot.getPixelColor(1195, 224) == menuColor:
        Utilities.fastClick(X, Y)

def skipStory(X, Y):
    skipColor = Color(126, 146, 191)  # (696, 76)
    Utilities.waitForColorAndDo(696, 76, skipColor, wait_time_period=1500,
            func_while_wait=enterStory, arg_while_wait=(X, Y))
    menuColor = Color(213, 174, 163) # (1195, 224)
    while myRobot.getPixelColor(1195, 224) != menuColor:
        if myRobot.getPixelColor(696, 76) == skipColor:
            Utilities.fastClick(696, 76)
        myRobot.delay(1000)

def waitForMenu():
    menuColor = Color(213, 174, 163) # (1195, 224)
    while myRobot.getPixelColor(1195, 224) != menuColor:
        Utilities.handleCommunicationError()
        print 'waiting for menu'
        myRobot.delay(1000)

def clickCombatAndBuyIfNeeded(X, Y):
    menuColor = Color(213, 174, 163) # (1195, 224)
    if myRobot.getPixelColor(1195, 224) == menuColor:
        Utilities.fastClick(X, Y)
    Utilities.buyStrength()


def enterACombat(X, Y):
    nextStepColor = Color(0, 44, 95) # (931, 923)
    Utilities.waitForColorAndDo(931, 923, nextStepColor, wait_time_period=1000,
            func_while_wait=clickCombatAndBuyIfNeeded, arg_while_wait=(X, Y))
    launchColor = Color(2, 36, 104)  # (930,947)
    Utilities.waitForColorAndDo(930, 947, launchColor)
    InBattleMenuColor = Color(0, 17, 51) # (1134, 1039)
    while myRobot.getPixelColor(1134, 1039) != InBattleMenuColor:
        Utilities.handleCommunicationError()
        myRobot.delay(2000)
    #Utilities.waitForColor(1134, 1039, InBattleMenuColor, wait_msg='waiting for in battle', wait_time_period=2000)

def clickAutoIfNeeded():
    AutoColor = Color(0, 38, 62) # (690, 1045)
    if myRobot.getPixelColor(690, 1045) == AutoColor:
        Utilities.fastClick(690, 1045)

def completeOneAutoCombat():
    ResultRColor = Color(192, 207, 222) # (868, 341)
    Utilities.waitForColorAndDo(868, 341, ResultRColor, wait_time_period=1000,
            func_while_wait=clickAutoIfNeeded, arg_while_wait=())
    waitForMenu()

def doSmallBoss():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    selectUnit3_RandomAttack()

    Utilities.fastClick(719, 1040) # Auto
    myRobot.delay(500)
    Utilities.fastClick(719, 1040) # Auto
    #waitForMenu()

def doBigBoss():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    selectUnit2_Sing()
    selectUnit3_RandomAttack()
    selectUnit4_Defense()
    selectUnit5_StatusBomb()
    
    # click on blue knight
    Utilities.fastClick(765, 506)
    myRobot.delay(2000)

    # first sing
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(2000)
    # then bomb
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(1000)

    # the rest 1st wave attack
    Utilities.fastClick(719, 1040) # Auto
    myRobot.delay(500)
    Utilities.fastClick(719, 1040) # Auto

    # waiting for start of 2nd wave
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    myRobot.delay(2000)

    # 2nd wave
    selectUnit3_RandomAttack()
    if Utilities.isUnitAlive(4):
        selectUnit4_Summon()
    Utilities.fastClick(719, 1040) # Auto
    myRobot.delay(500)
    Utilities.fastClick(719, 1040) # Auto
    

def completeBossCombat(totalNumBattles, bossBattleFunct=doSmallBoss, bossBattleFunctArgs=[]):
    for i in range(0, totalNumBattles - 1):
        doOneSimpleBattle()
    bossBattleFunct(*bossBattleFunctArgs)
    ResultRColor = Color(192, 207, 222) # (868, 341)
    Utilities.waitForColorAndDo(868, 341, ResultRColor, wait_time_period=1000,
            func_while_wait=clickAutoIfNeeded, arg_while_wait=())
    waitForMenu()

def doBattle(X, Y, fightFunct=completeOneAutoCombat, fightFunctArgs=[]):
    enterACombat(X, Y) 
    fightFunct(*fightFunctArgs)

def selectUnit2_Sing():
    Utilities.openMagicMenu(2)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(772, 944)
    myRobot.delay(1000)
    Utilities.fastClick(772, 944)
    myRobot.delay(1500)

def selectUnit3_RandomAttack():
    Utilities.openMagicMenu(3)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(1057, 838)
    myRobot.delay(1500)

def selectUnit4_Summon():
    Utilities.openMagicMenu(4)
    myRobot.delay(1000)
    Utilities.fastClick(1078, 717)
    myRobot.delay(1500)

def selectUnit4_Defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[3])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1500)

def selectUnit5_StatusBomb():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(1071, 931)
    myRobot.delay(1500)

def doOneSimpleBattle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    InBattleMenuColor = Color(0, 17, 51) # (1134, 1039)
    while myRobot.getPixelColor(1134, 1039) == InBattleMenuColor:
        clickAutoIfNeeded()
        myRobot.delay(300)



def doOneRound():
    waitForMenu()
    myRobot.delay(3000)
    
    doBattle(963, 790, fightFunct=completeBossCombat, fightFunctArgs=[3, doSmallBoss, []]) # combat 1
    myRobot.delay(3000)
    doBattle(965, 619, fightFunct=completeBossCombat, fightFunctArgs=[4, doSmallBoss, []]) # combat 2
    myRobot.delay(3000)
    doBattle(961, 618, fightFunct=completeBossCombat, fightFunctArgs=[4, doSmallBoss, []]) # combat 3
    myRobot.delay(3000)
    doBattle(957, 604, fightFunct=completeBossCombat, fightFunctArgs=[4, doSmallBoss, []]) # combat 4
    myRobot.delay(3000)
    doBattle(963, 604, fightFunct=completeBossCombat, fightFunctArgs=[5, doBigBoss, []]) # combat 5 final    
    myRobot.delay(3000)

    skipStory(959, 499)
    myRobot.delay(3000)

    frontPageColor = Color(193, 128, 128) # (1204, 223)
    Utilities.handleMissionEnd(1204, 223, frontPageColor)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 66, 15) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        Utilities.checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetColor = Color(238, 243, 245)  # (722,408)
    while myRobot.getPixelColor(722,408) != targetColor:
        Utilities.fastClick(1254, 408)
        myRobot.delay(2000)
        print("waiting for targetUnitColor")
    myRobot.delay(1000)

    # back to front page
    letterColor = Color(180,113,99) # (1150,175)
    while myRobot.getPixelColor(1150, 175) != letterColor:
        Utilities.fastClick(707, 1013)
        print("waiting for letter color, ", myRobot.getPixelColor(1150, 175))
        myRobot.delay(3000)
    myRobot.delay(1000)

def goToMissionMenu():
    rewardExchangeColor = Color(110, 84, 63) # (1212, 89)
    while myRobot.getPixelColor(1212, 89) != rewardExchangeColor:
        Utilities.fastClick(822, 514)
        myRobot.delay(3000)
    
    mission = "mission.png"
    missionRegion = Region(725,169,284,903)
    missionRegion.click(mission)
    frontPageColor = Color(228, 160, 160) # (1202, 225)
    while myRobot.getPixelColor(1202, 225) != frontPageColor:
        myRobot.delay(1000)
    myRobot.delay(1000)

def goToTargetMission():
    nextStepColor = Color(0, 39, 90) # (931, 951)
    Utilities.waitForColorAndDo(931, 951, nextStepColor, wait_time_period=2000,
            func_while_wait=Utilities.fastClick, arg_while_wait=(959, 424))

    # wait for follower menu
    followerColor = Color(143,89,48) # (1015,223)
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
            func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)
    myRobot.delay(2000)

    # confirm to enter stroy mode menu
    Utilities.fastClick(1042, 637)
    menuColor = Color(213, 174, 163) # (1195, 224)
    yesColor = Color(110, 0, 0) # (1042, 637)
    while myRobot.getPixelColor(1195, 224) != menuColor:
        if myRobot.getPixelColor(1042, 637) == yesColor:
            Utilities.fastClick(1045, 638)
        myRobot.delay(2000)


def process(numRound):
    Utilities.log('StoryModeLog.txt', 'process', 'start process')
    changeToRightTeam()
    myRobot.delay(3000)
    goToMissionMenu()
    myRobot.delay(3000)
    count = 0
    Utilities.log('StoryModeLog.txt', 'process', 'start fighting')
    while count < numRound:
        start = time.time()
        count = count + 1
        goToTargetMission()
        myRobot.delay(2000)
        doOneRound()
        myRobot.delay(3000)
        total_time = time.time() - start
        Utilities.log('StoryModeLog.txt', 'round ' + str(count), 'completedOneRound: ' + str(total_time))
    # go back to front page
    Utilities.fastClick(1213, 224)
    myRobot.delay(2000)

if __name__ == "__main__":
    process(1)
    #doBigBossRound1()
    #goToTargetMission()
    #doOneRound()
    #doBigBossRound2()
