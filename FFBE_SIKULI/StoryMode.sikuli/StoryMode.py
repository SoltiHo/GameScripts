import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
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
    waitForMenu()

def waitForMenu():
    menuColor = Color(213, 174, 163) # (1195, 224)
    Utilities.waitForColor(1195, 224, menuColor,
            wait_time_period=1000, wait_msg='waiting for menu')


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
    Utilities.waitForColor(1134, 1039, InBattleMenuColor, wait_msg='waiting for in battle', wait_time_period=2000)

def clickAutoIfNeeded():
    AutoColor = Color(0, 38, 62) # (690, 1045)
    if myRobot.getPixelColor(690, 1045) == AutoColor:
        Utilities.fastClick(690, 1045)

def completeOneAutoCombat():
    ResultRColor = Color(192, 207, 222) # (868, 341)
    Utilities.waitForColorAndDo(868, 341, ResultRColor, wait_time_period=1000,
            func_while_wait=clickAutoIfNeeded, arg_while_wait=())
    waitForMenu()

def completeSmallBossCombat():
    doOneSimpleBattle()
    doOneSimpleBattle()
    doOneSimpleBattle()
    doSmallBoss()
    ResultRColor = Color(192, 207, 222) # (868, 341)
    Utilities.waitForColorAndDo(868, 341, ResultRColor, wait_time_period=1000,
            func_while_wait=clickAutoIfNeeded, arg_while_wait=())
    waitForMenu()

def completeBigBossCombat():
    doOneSimpleBattle()
    doOneSimpleBattle()
    doOneSimpleBattle()
    doOneSimpleBattle()
    doBigBossRound1()
    doBigBossRound2()
    ResultRColor = Color(192, 207, 222) # (868, 341)
    Utilities.waitForColorAndDo(868, 341, ResultRColor, wait_time_period=1000,
            func_while_wait=clickAutoIfNeeded, arg_while_wait=())
    waitForMenu()

def doBattle(X, Y, fightFunct=completeOneAutoCombat):
    enterACombat(X, Y) 
    fightFunct()

def selectUnit1_IncreaseAttack():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.fastClick(762, 824)
    myRobot.delay(1500)

def selectUnit1_Kill():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.fastClick(758, 925)
    myRobot.delay(1500)

def selectUnit2_ReduceDefense():
    Utilities.openMagicMenu(2)
    myRobot.delay(1000)
    Utilities.fastClick(1037, 924)
    myRobot.delay(1500)

def selectUnit2_RandomAttack():
    Utilities.openMagicMenu(2)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(1057, 723)
    myRobot.delay(1500)

def selectUnit3_Encourage():
    Utilities.openMagicMenu(3)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(784, 839)
    myRobot.delay(1000)
    Utilities.fastClick(784, 839)
    myRobot.delay(1500)

def selectUnit3_DecreaseDefense():
    Utilities.openMagicMenu(3)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(768, 711)
    myRobot.delay(1500)

def selectUnit4_evade():
    Utilities.openMagicMenu(4)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(1064, 817)
    myRobot.delay(1500)

def selectUnit4_AttackAll():
    Utilities.openMagicMenu(4)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(760, 812)
    myRobot.delay(1500)

def selectUnit5_StatusBomb():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(772, 818)
    myRobot.delay(1500)

def selectUnit6_defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[5])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1500)

def doBigBossRound1():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    selectUnit1_IncreaseAttack()
    selectUnit2_ReduceDefense()
    selectUnit3_Encourage()
    selectUnit4_evade()
    selectUnit5_StatusBomb()
    selectUnit6_defense()
    
    # select bone dragon
    Utilities.fastClick(824, 377)
    myRobot.delay(1000)

    # launch
    Utilities.fastClick(809, 946) # unit 3
    myRobot.delay(3000)
    
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(100)
    Utilities.fastClick(1062, 943) # unit 6
    myRobot.delay(100)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(500)

    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)

def doBigBossRound2():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    selectUnit1_Kill()
    selectUnit2_RandomAttack()
    selectUnit4_AttackAll()
    
    Utilities.fastClick(719, 1040) # Auto
    myRobot.delay(500)
    Utilities.fastClick(719, 1040) # Auto


def doOneSimpleBattle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    InBattleMenuColor = Color(0, 17, 51) # (1134, 1039)
    while myRobot.getPixelColor(1134, 1039) == InBattleMenuColor:
        clickAutoIfNeeded()
        myRobot.delay(300)

def doSmallBoss():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    selectUnit4_AttackAll()
    selectUnit3_DecreaseDefense()
    selectUnit2_RandomAttack()
    selectUnit1_Kill()
    Utilities.fastClick(809, 946) # unit 3
    myRobot.delay(3000)
    
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(300)
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(100)
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)

    Utilities.fastClick(719, 1040) # Auto
    myRobot.delay(500)
    Utilities.fastClick(719, 1040) # Auto
    #waitForMenu()


def doOneRound():
    skipStory(895, 443)
    myRobot.delay(3000)
    
    doBattle(1083, 591) # battle 1
    myRobot.delay(3000)
    doBattle(807, 591) # battle 2
    myRobot.delay(3000)
    
    skipStory(990, 607)
    myRobot.delay(3000)
    
    doBattle(819, 583, fightFunct=completeSmallBossCombat) # combat 3, small boss, 4 battles
    myRobot.delay(3000)

    doBattle(1015, 598) # combat 4
    myRobot.delay(3000)
    skipStory(870, 594)
    myRobot.delay(3000)
    doBattle(975, 655, fightFunct=completeBigBossCombat) # combat 5, big boss
    myRobot.delay(3000)
    skipStory(958, 951)

    frontPageColor = Color(193, 128, 128) # (1204, 223)
    Utilities.handleMissionEnd(1204, 223, frontPageColor)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 66, 15) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetColor = Color(173, 133, 58)  # (838,424)
    while myRobot.getPixelColor(838,424) != targetColor:
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
    # pull down the menu
    mouseMove(Location(961, 458))
    mouseDown(Button.LEFT)
    mouseMove(0, 500)
    mouseUp(Button.LEFT)
    myRobot.delay(1000)

    nextStepColor = Color(0, 39, 90) # (931, 951)
    Utilities.waitForColorAndDo(931, 951, nextStepColor, wait_time_period=2000,
            func_while_wait=Utilities.fastClick, arg_while_wait=(811, 321))

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
    changeToRightTeam()
    myRobot.delay(3000)
    goToMissionMenu()
    myRobot.delay(3000)
    count = 0
    while count < numRound:
        count = count + 1
        goToTargetMission()
        myRobot.delay(2000)
        doOneRound()
        myRobot.delay(3000)
    # go back to front page
    Utilities.fastClick(1213, 224)
    myRobot.delay(2000)

if __name__ == "__main__":
    process(2)
    #goToTargetMission()
    #doOneRound()
    #doBigBossRound2()
