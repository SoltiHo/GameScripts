import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()


def selectUnit1_DecreaseLighting():
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(785, 924)
    myRobot.delay(800)

def selectUnit1_Destroy():
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(1052, 833)
    myRobot.delay(800)

def selectUnit2_Rose():
    Utilities.openMagicMenu(2)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(782, 827)
    myRobot.delay(800)

def selectUnit3_chainSaw():
    Utilities.openMagicMenu(3)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(797, 927)
    myRobot.delay(800)

def selectUnit4_encourage():
    Utilities.openMagicMenu(4)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(786, 909)
    myRobot.delay(700)
    # select the team
    Utilities.fastClick(786, 909)
    myRobot.delay(1000) 
    
def selectUnit4_defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[3])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1000)

def selectUnit5_chainSaw():
    Utilities.openMagicMenu(5)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(797, 927)
    myRobot.delay(800)

def selectUnit6_defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[5])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1000)


def checkProtectionSettingMenu():
    noColor = Color(227, 234, 243) # (842, 748)
    if myRobot.getPixelColor(842, 748) == noColor:
        Utilities.fastClick(842,748)
    dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
    getRewardColor = Color(2, 16, 64) # (918, 883)
    if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
        Utilities.fastClick(1223, 149)

def isInBattle():
    menuColor = Color(0, 61, 130) # (1129, 1029)
    if myRobot.getPixelColor(1129, 1029) == menuColor:
        return True
    else:
        return False

def set1stCommand():
    selectUnit1_DecreaseLighting()
    myRobot.delay(1000)
    selectUnit2_Rose()
    myRobot.delay(1000)
    selectUnit3_chainSaw()
    myRobot.delay(1000)
    selectUnit4_encourage()
    myRobot.delay(1000)
    selectUnit5_chainSaw()
    myRobot.delay(1000)
    selectUnit6_defense()
    myRobot.delay(1000)

def set2ndCommand():
    selectUnit1_Destroy()
    myRobot.delay(1000)
    selectUnit2_Rose()
    myRobot.delay(1000)
    selectUnit3_chainSaw()
    myRobot.delay(1000)
    selectUnit4_defense()
    myRobot.delay(1000)
    selectUnit5_chainSaw()
    myRobot.delay(1000)
    selectUnit6_defense()
    myRobot.delay(1000)

def launchAttack():
    Utilities.fastClick(1076, 724) # unit 4
    Utilities.fastClick(1062, 943) # unit 6
    myRobot.delay(2000)

    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(1600)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(809, 946) # unit 3
    myRobot.delay(500)
    Utilities.fastClick(796, 831) # unit 2

def doOneFight():
    enterMission()
    myRobot.delay(3000)
    # waiting for waiting for command
    while not isInBattle():
        myRobot.delay(1000)
    # wait for waiting for command
    roundCount = 1
    while isInBattle():
        if Utilities.isWaitingForCommand():
            myRobot.delay(2000)
            if roundCount == 1:
                set1stCommand()
            else:
                set2ndCommand()
            roundCount += 1
            myRobot.delay(1000)
            launchAttack()
        else:
            print("waiting for waiting for command")
        myRobot.delay(3000)
    print("One Battle Ended")
    battleEndMessageColor = Color(0, 18, 70) # (1046, 143)
    Utilities.waitForColorAndDo(1046, 143, battleEndMessageColor)
    # Battle End
    bachHeadColor = Color(7, 8, 11)  # (932, 364)
    Utilities.handleMissionEnd(targetX=932, targetY=364, waitTargetColor=bachHeadColor)
    # wait for mission menu
    topMissionColor = Color(116, 22, 29) # (703, 611)
    Utilities.waitForColor(703, 611, topMissionColor, "waiting for back to mission menu")

def enterMission():
    topMissionColor = Color(116, 22, 29) # (703, 611)
    Utilities.waitForColorAndDo(703, 611, topMissionColor)

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 83, 196) # (954, 923)
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)
    # select follower
    followerColor = Color(145,60,32) # (1015,223)
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
        func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 72, 16) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetUnitColor = Color(49, 108, 216)  # (1210, 415)
    while myRobot.getPixelColor(1210, 415) != targetUnitColor:
        Utilities.fastClick(1254, 408)
        myRobot.delay(2000)
        print("waiting for targetUnitColor")
    myRobot.delay(1000)

    # back to front page
    letterColor = Color(184,123,108) # (1150,175)
    while myRobot.getPixelColor(1150, 175) != letterColor:
        Utilities.fastClick(707, 1013)
        print("waiting for letter color, ", myRobot.getPixelColor(1150, 175))
        myRobot.delay(3000)
    myRobot.delay(1000)

def process():
    changeToRightTeam()
    
    BachShadowColor = Color(20, 5, 1) # (1005, 494)
    Utilities.waitForColorAndDo(1005, 494, BachShadowColor, wait_time_period=1000,
            func_while_wait=Utilities.fastClick, arg_while_wait=(822, 514))
    myRobot.delay(1000)
    # wait for Bach page
    bachHeadColor = Color(7, 8, 11)  # (932, 364)
    Utilities.waitForColor(932, 364, bachHeadColor, "waiting for Bach head")
    myRobot.delay(2000)
    firstBallColor = Color(60, 189, 45) # (1142, 305)
    while myRobot.getPixelColor(1142, 305) == firstBallColor:
        # got ball
        doOneFight()
        myRobot.delay(2000)
    # back to front page, click "Return"
    Utilities.fastClick(1213, 234)
    myRobot.delay(2000)

if __name__ == "__main__":
    process()
    #set2ndCommand()
    #myRobot.delay(2000)
    #launchAttack()
