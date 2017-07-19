import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

def selectUnit1_AccurateShoot():
    Utilities.openMagicMenu(1)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(759, 952)
    myRobot.delay(800)

def selectUnit1Manual_AccurateShoot():
    Utilities.openMagicMenu(1)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1045, 839)
    myRobot.delay(800)

def selectUnit2_chainSaw():
    Utilities.openMagicMenu(2)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1500)
    # select the skill
    Utilities.fastClick(1091, 819)
    myRobot.delay(1500)

def selectUnit2Manual_chainSaw():
    Utilities.openMagicMenu(2)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1500)
    # select the skill
    Utilities.fastClick(812, 821)
    myRobot.delay(1500)

def selectUnit4_BreakShoot():
    Utilities.openMagicMenu(4)
    myRobot.delay(2000)
    # select the skill
    Utilities.fastClick(1052, 921)
    myRobot.delay(800)

def selectUnit4Manual_BreakShoot():
    Utilities.openMagicMenu(4)
    myRobot.delay(2000)
    # select the skill
    Utilities.fastClick(736, 927)
    myRobot.delay(800)

def selectUnit4_AccurateShoot():
    Utilities.openMagicMenu(4)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(737, 939)
    myRobot.delay(800)

def selectUnit3_encourage():
    Utilities.openMagicMenu(3)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1049, 935)
    myRobot.delay(1000)
    # select the team
    Utilities.fastClick(796, 856)
    myRobot.delay(1000) 

def selectUnit3Manual_encourage():
    Utilities.openMagicMenu(3)
    myRobot.delay(2000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(806, 914)
    myRobot.delay(1000)
    # select the team
    Utilities.fastClick(796, 856)
    myRobot.delay(1000) 


def selectUnit5_chainSaw():
    Utilities.openMagicMenu(5)
    myRobot.delay(1500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1031, 833)
    myRobot.delay(800)

def selectUnit5Manual_chainSaw():
    Utilities.openMagicMenu(5)
    myRobot.delay(1500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(772, 926)
    myRobot.delay(800)

def selectUnit6_defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[5])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1000)

def selectUnit3_defense():
    mouseMove(Utilities.UNIT_CENTER_LOCATIONS[2])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(1000)
    
def checkProtectionSettingMenu():
    noColor = Color(205, 217, 232) # (842, 748)
    if myRobot.getPixelColor(842, 748) == noColor:
        Utilities.fastClick(842,748)
    dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
    getRewardColor = Color(2, 16, 64) # (918, 883)
    if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
        Utilities.fastClick(1223, 149)

def isInBattle():
    menuColor = Color(0, 58, 130) # (1129, 1029)
    if myRobot.getPixelColor(1129, 1029) == menuColor:
        return True
    else:
        return False

def set1stCommand():
    selectUnit1_AccurateShoot()
    myRobot.delay(1000)
    selectUnit2_chainSaw()
    myRobot.delay(1000)
    selectUnit3_encourage()
    myRobot.delay(1000)
    selectUnit4_BreakShoot()
    myRobot.delay(1000)
    selectUnit5_chainSaw()
    myRobot.delay(1000)
    selectUnit6_defense()
    myRobot.delay(1000)

def set2ndCommand():
    selectUnit1_AccurateShoot()
    myRobot.delay(1000)
    selectUnit2_chainSaw()
    myRobot.delay(1000)
    selectUnit4_AccurateShoot()
    myRobot.delay(1000)
    selectUnit5_chainSaw()
    myRobot.delay(1000)
    selectUnit6_defense()
    myRobot.delay(1000)
    selectUnit3_defense()

def processManual():
    setManualCommand()
    myRobot.delay(2000)
    launchAttackManual()
    myRobot.delay(5000)
    

def setManualCommand():
    selectUnit1Manual_AccurateShoot()
    myRobot.delay(1000)
    selectUnit2Manual_chainSaw()
    myRobot.delay(1000)
    selectUnit3Manual_encourage()
    myRobot.delay(1000)
    selectUnit4Manual_BreakShoot()
    myRobot.delay(1000)
    selectUnit5Manual_chainSaw()
    myRobot.delay(1000)
    
def launchAttackManual():
    Utilities.fastClick(809, 946) # unit 3
    myRobot.delay(3000)
    
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(100)
    Utilities.fastClick(1062, 943) # unit 6

    myRobot.delay(1700)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(20000)

def launchAttackManual2():
    Utilities.fastClick(809, 946) # unit 3
    myRobot.delay(3000)

    Utilities.fastClick(1062, 943) # unit 6
    myRobot.delay(100)
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(793, 720) # unit 1
   
    

    myRobot.delay(1700)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(20000)

def launchAttack():
    Utilities.fastClick(809, 946) # unit 3
    Utilities.fastClick(1062, 943) # unit 6
    myRobot.delay(2000)
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(793, 720) # unit 1

    myRobot.delay(1700)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2

def doOneFight():
    Utilities.log('CoFight.txt', 'One Battle', 'Started')
    enterMission()
    myRobot.delay(3000)
    # waiting for waiting for command
    while not isInBattle():
        myRobot.delay(1000)
    Utilities.log('CoFight.txt', 'One Battle', 'is in battle')
    # wait for waiting for command
    roundCount = 1
    while isInBattle():
        if Utilities.isWaitingForCommand():
            myRobot.delay(2000)
            if Utilities.isWaitingForCommand():
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
    Utilities.log('CoFight.txt', 'One Battle', 'ended')
    #battleEndMessageColor = Color(0, 18, 70) # (1046, 143)
    #Utilities.waitForColorAndDo(1046, 143, battleEndMessageColor)
    # Battle End
    CofightMenuHeaderColor = Color(228, 121, 122)  # (981,404)
    Utilities.handleMissionEnd(targetX=981, targetY=404, waitTargetColor=CofightMenuHeaderColor)
    # wait for mission menu
    targetMissionColor = Color(195, 177, 179) # (826,783)
    Utilities.waitForColor(826,783, targetMissionColor, "waiting for back to mission menu")

def enterMission():
    targetMissionColor = Color(195, 177, 179) # (826,783)
    Utilities.waitForColorAndDo(826,783, targetMissionColor)

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)
    # select follower
    followerColor = Color(143,89,48) # (1015,223)
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
        func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 66, 15) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetUnitColor = Color(73, 45, 7)  # (834,413)
    while myRobot.getPixelColor(834,413) != targetUnitColor:
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

def gotoCofightMenu():
    #CofightBannerColor = Color(97, 244, 245) # (1015,446)
    #Utilities.waitForColorAndDo(1015,446, CofightBannerColor, wait_time_period=2000,
    #        func_while_wait=Utilities.fastClick, arg_while_wait=(822, 514))
    rewardExchangeColor = Color(110, 84, 63) # (1212, 89)
    while myRobot.getPixelColor(1212, 89) != rewardExchangeColor:
        Utilities.fastClick(822, 514)
        myRobot.delay(3000)

    cofightBannerIcon = "cofightBannerIcon.png"
    cofightBannerRegion = Region(664,156,202,911)
    cofightBannerRegion.click(cofightBannerIcon)
    myRobot.delay(1000)
    # wait for cofight menu
    CofightMenuHeaderColor = Color(228, 121, 122)  # (981,404)
    Utilities.waitForColor(981,404, CofightMenuHeaderColor, "waiting for CofightMenuHeader")
    myRobot.delay(1000)

def setFollowerFilter():
    targetMissionColor = Color(195, 177, 179) # (826,783)
    Utilities.waitForColorAndDo(826, 783, targetMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(826, 783))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=Utilities.buyStrength)

    # click filter
    followerColor = Color(143, 89, 48) # (1015,223) 
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
            func_after_wait=Utilities.fastClick, arg_after_wait=(1094, 233))
    myRobot.delay(1000)

    # choose Filtering
    Utilities.fastClick(1072, 86)
    myRobot.delay(1000)
    
    # clear everything
    Utilities.fastClick(740, 1024)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)

    # select preferred weapons
    Utilities.fastClick(702, 543) # 1st row
    myRobot.delay(500)
    #Utilities.fastClick(778, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 543)
    #smyRobot.delay(500)
    #Utilities.fastClick(925, 543)
    #myRobot.delay(500)
    Utilities.fastClick(999, 545)
    myRobot.delay(500)
    Utilities.fastClick(1071, 543)
    myRobot.delay(500)
    Utilities.fastClick(1140, 548)
    myRobot.delay(500)
    Utilities.fastClick(1214, 545)
    myRobot.delay(500)
    #Utilities.fastClick(702, 623) # 2nd row
    #myRobot.delay(500)
    #Utilities.fastClick(778, 623)
    #myRobot.delay(500)
    Utilities.fastClick(854, 623)
    myRobot.delay(500)
    Utilities.fastClick(925, 622)
    myRobot.delay(500)
    Utilities.fastClick(995, 624)
    myRobot.delay(500)
    #Utilities.fastClick(1066, 619)
    #myRobot.delay(500)
    Utilities.fastClick(1135, 624)
    myRobot.delay(500)
    Utilities.fastClick(1213, 627)
    myRobot.delay(500)
    Utilities.fastClick(710, 700) # 3rd row
    myRobot.delay(500)
    Utilities.fastClick(779, 698)
    myRobot.delay(500)
    #Utilities.fastClick(854, 698)
    #myRobot.delay(500)
    #Utilities.fastClick(927, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(995, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(1143, 695)
    #myRobot.delay(500)
    Utilities.fastClick(1213, 693)
    myRobot.delay(1000)

    # click confirm
    Utilities.fastClick(958, 1008)
    myRobot.delay(2000)

    def clickReturnAndWait():
        Utilities.fastClick(709,221)
        myRobot.delay(1000)

    # click two return
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor, wait_time_period=2000,
            func_while_wait=clickReturnAndWait,
            func_after_wait=clickReturnAndWait)
    myRobot.delay(1000)                


def process():
    changeToRightTeam() 
    myRobot.delay(2000)
    gotoCofightMenu()
    myRobot.delay(2000)
    setFollowerFilter()
    myRobot.delay(2000)
    
    firstBallColor = Color(57, 181, 47) # (1142, 305)
    forthBallColor = Color(90, 235, 45) # (1221, 301)
    targetBallColor = forthBallColor
    targetBallX = 1221
    targetBallY = 301
    while myRobot.getPixelColor(targetBallX, targetBallY) == targetBallColor:
        # got ball
        doOneFight()
        myRobot.delay(2000)
    # back to front page, click "Return"
    Utilities.fastClick(1213, 234)
    myRobot.delay(2000)

if __name__ == "__main__":
    #print(isInBattle())
    #doOneFight()
    #titanHeadColor = Color(87, 61, 41)  # (945, 365)
    #Utilities.handleMissionEnd(targetX=932, targetY=364, waitTargetColor=titanHeadColor)
    #enterMission()
    #changeToRightTeam()
    #process()
    #set1stCommand()
    #set2ndCommand()
    #myRobot.delay(2000)
    #launchAttack()
    #myRobot.delay(20000)
    launchAttackManual2()
    #processManual()