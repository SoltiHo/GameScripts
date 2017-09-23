import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
import BonusGame
import FightClub
import CoFight
from sikuli import *
reload(Utilities)

myRobot = JRobot()
selectFollower = True
setFilter = False
buyStrength = True
resetPeriod = 100
doBonusGame = False
numBonusGame = 4
doFightClub = True
doCoFight = True


def selectFollowerAndLaunch():
    while True:
        # select follower
        followerColor = Color(143,89,48) # (1015,223)
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
    
        # wait for menu before exiting
        menuColor = Color(0, 17, 51) # (1185, 1054)
        errorOColor = Color(0, 34, 98) # (945, 599)
        completed = True
        while myRobot.getPixelColor(1185, 1054) != menuColor:
            myRobot.delay(1000)
            if myRobot.getPixelColor(945, 599) == errorOColor:
                Utilities.fastClick(945, 599)
                completed = False
                break
            Utilities.handleCommunicationError()
        if completed:
            break

def enterFastMission():
    fastMissionColor = Color(99, 4, 7) # (703, 672)
    Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
    if buyStrength:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
                func_while_wait=Utilities.buyStrength)
    else:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)

    selectFollowerAndLaunch()
         

def steal():
    # To steal
    Utilities.openMagicMenu(1)
    myRobot.delay(700)
    Utilities.fastClick(820, 918)
    myRobot.delay(700)

def doBattles():
    nextStepColor = Color(0, 40, 117) # (958, 943)
    AutoColor = Color(0, 140, 180) # (725, 1023)
    def attack():
        monsterBloodColor = Color(145, 222, 79) # (950, 628)
        waitingForCommandColor = Color(6, 51, 120) # (850, 701)
        if myRobot.getPixelColor(950, 628) == monsterBloodColor and myRobot.getPixelColor(850, 701) == waitingForCommandColor:
            #steal()
            myRobot.mouseMove(Utilities.UNIT_CENTER_LOCATIONS[0].x, Utilities.UNIT_CENTER_LOCATIONS[0].y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            myRobot.mouseMove(Utilities.UNIT_CENTER_LOCATIONS[1].x, Utilities.UNIT_CENTER_LOCATIONS[1].y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            #myRobot.mouseMove(Utilities.UNIT_CENTER_LOCATIONS[2].x, Utilities.UNIT_CENTER_LOCATIONS[2].y)
            #myRobot.mousePress(InputEvent.BUTTON1_MASK)
            #myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        else:
            print "not waiting for command"

        if myRobot.getPixelColor(725, 1023) != AutoColor:
            myRobot.mouseMove(1001, 353)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        Utilities.handleCommunicationError()
        Utilities.handleFollowerError()

    def checkAndRestartBSFFBE():
        BSFFBEColor = Color(230,191,216) # (330, 196)
        if myRobot.getPixelColor(330, 196) == BSFFBEColor:
            Utilities.fastClick(330, 196)
            myRobot.delay(5000)
            menuColor = Color(0, 17, 51) # (1150, 1032)
            while myRobot.getPixelColor(1150, 1032) != menuColor:
                blackColor = Color(0, 0, 0)
                if myRobot.getPixelColor(353, 220) == blackColor:
                    Utilities.fastClick(998, 242)
                if myRobot.getPixelColor(330, 196) == BSFFBEColor:
                    Utilities.fastClick(330, 196)
                myRobot.delay(500)
            myRobot.delay(3000)
            Utilities.log('RestartLog.txt', 'Restart', 'Restarted BS FFBE')

    Utilities.waitForColorAndDo(958, 943, nextStepColor, 
            func_while_wait=attack,
            func_wait_too_long=checkAndRestartBSFFBE,
            func_after_wait=Utilities.handleMissionEnd)
    print("mission end handled")

def executeOneRound():
    enterFastMission()
    doBattles() 

def chooseAndMakeHeal():
    hatColor = Color(243, 224, 181) # (712, 354)
    Utilities.waitForColorAndDo(712, 354, hatColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(1124, 358))
    myRobot.delay(1000)
    Utilities.fastClick(1050, 784)  # Make
    myRobot.delay(1000)
    Utilities.fastClick(1051, 598)  # Yes
    myRobot.delay(1000)
    
    abilityColor = Color(0, 179, 238)  # (1141, 225)
    while myRobot.getPixelColor(1141, 225) != abilityColor:
        myRobot.delay(1000)
    

def harvestHeal(healIdx):
    healLocation = [Location(752, 445), Location(751, 602), Location(750, 755)]
    Utilities.fastClick(healLocation[healIdx].getX(), healLocation[healIdx].getY())
    myRobot.delay(2000)
    
    okColor = Color(255, 255, 255) # (963, 733)
    Utilities.waitForColorAndDo(963, 733, okColor)
    myRobot.delay(2000)

    # check if extra stone
    stoneColor = Color(2, 56, 36)  # (774, 607)
    if myRobot.getPixelColor(774, 607) == stoneColor:
        myRobot.delay(1000)
        Utilities.fastClick(963, 733)  # click OK

    # wait for menu
    plusColor = Color(0, 132, 143) # (966, 899)
    while myRobot.getPixelColor(966, 899) != plusColor:
        myRobot.delay(500)

    # make a new one
    Utilities.fastClick(healLocation[healIdx].getX(), healLocation[healIdx].getY())
    myRobot.delay(2000)
    healColor = Color(108, 218, 244) # (717, 569)
    Utilities.waitForColorAndDo(717, 569, healColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=(838, 321),
            func_after_wait=Utilities.fastClick, arg_after_wait=(996, 569))
    myRobot.delay(1000)
    makeColor = Color(25, 66, 120) # (1065, 815)
    Utilities.waitForColorAndDo(1065, 815, makeColor)

    myRobot.delay(1000)
    print('waiting for yes')
    yesColor = Color(205, 214, 229) # (1085, 587)
    Utilities.waitForColorAndDo(1085, 587, yesColor)
    
    # back to menu
    print('waiting for menu')
    myRobot.delay(2000)
    while myRobot.getPixelColor(966, 899) != plusColor:
        myRobot.delay(500)
    print('completed')

def harvestAndMakeHeal():
    # go back frontpage
    frontpageColor = Color(155, 15, 16)  # (1194, 223)
    Utilities.waitForColorAndDo(1194, 223, frontpageColor)
    myRobot.delay(2000)

    # craft
    craftColor = Color(152, 155, 129) # (1168, 802)
    Utilities.waitForColorAndDo(1168, 802, craftColor)
    myRobot.delay(2000)

    # go to ability page
    healColor = Color(162, 219, 204) # (750, 451)
    while myRobot.getPixelColor(750, 451) != healColor:
        myRobot.delay(1000)

    myRobot.delay(1000)
    harvestHeal(0)
    myRobot.delay(1000)
    harvestHeal(1)
    myRobot.delay(1000)
    harvestHeal(2)
    myRobot.delay(2000)

    # click return
    worldColor = Color(248, 145, 65) # (944, 808)
    Utilities.waitForColorAndDo(944, 808, worldColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[723, 228])
    myRobot.delay(2000)
    Utilities.fastClick(958, 574)  # earth temple.  center of the screen
    

def main():
    count = 0
    start = time.time()
    total_time = 0
    
    while True:
        if count == 0:
            start = time.time()
            if setFilter:
                setFollowerFilter()
        count += 1
        executeOneRound()
        #if count % 10 == 0:
        #    harvestAndMakeHeal()
        if count % 50 == 0:
            total_time = time.time() - start
            Utilities.log('FastTrustLog.csv', 'FastTrust', str(total_time) + ',' + str(count))
        if count == resetPeriod:
            Utilities.log('FastTrustLog.csv', 'reset', 'reset period triggerred:' + str(resetPeriod))
            # back to front page
            worldColor = Color(248, 145, 65) # (944, 808)
            gotoFrontPageColor = Color(209,3,3) # (1214,225)
            while myRobot.getPixelColor(944, 808) != worldColor:
                # checkProtectionSettingMenu
                if myRobot.getPixelColor(1214,225) == gotoFrontPageColor:
                    Utilities.log('FastTrustLog.csv', 'reset', 'click gotoFrontPage')
                    Utilities.fastClick(1214, 225)
                BonusGame.BonusGame.checkProtectionSettingMenu()
                myRobot.delay(2000)
                # check info menu here
            Utilities.log('FastTrustLog.csv', 'reset', 'saw world coor')
            myRobot.delay(5000)
            # play bonus game
            if doFightClub:
                Utilities.log('FastTrustLog.csv', 'reset', 'do fight club')
                FightClub.process()
                Utilities.log('FastTrustLog.csv', 'reset', 'fight club completed')
                myRobot.delay(2000)
            if doBonusGame:
                Utilities.log('FastTrustLog.csv', 'reset', 'do bonus game')
                BonusGame.process(numBonusGame)
                Utilities.log('FastTrustLog.csv', 'reset', 'bonus game completed')
                myRobot.delay(2000)
            if doCoFight:
                Utilities.log('FastTrustLog.csv', 'reset', 'do co-fight')
                CoFight.CoFightRunner.process()
                Utilities.log('FastTrustLog.csv', 'reset', 'co-fight completed')
                myRobot.delay(2000)
            Utilities.log('FastTrustLog.csv', 'reset', 'restart BS and the mission')
            restartBSandTheMission()
            Utilities.log('FastTrustLog.csv', 'reset', 'restart the mission completed')
            count = 0

def goToEarthTemple():
    # wait for "World"
    worldColor = Color(248, 145, 65) # (944, 808)
    Utilities.waitForColorAndDo(944, 808, worldColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[723, 228])
    myRobot.delay(2000)
    print("world seen")

    # 1st level map, choose 1st island group
    myRobot.delay(3000)
    mouseMove(Location(693, 690))
    mouseDown(Button.LEFT)
    mouseMove(-400, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    mouseMove(Location(693, 690))
    mouseDown(Button.LEFT)
    mouseMove(-400, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    firstIslandGroup = "firstIslandGroup.png"
    firstGroupRegion = Region(706,237,541,407)
    firstGroupRegion.click(firstIslandGroup)
    myRobot.delay(5000)
    print("1st island done")

    # 2nd level map, choose 1st island
    firstIslandColor = Color(115, 147, 105)  # (1061, 462)
    Utilities.waitForColorAndDo(1061, 462, firstIslandColor)
    myRobot.delay(2000)
    print("2nd island done")

    # pull right to show earth temple
    mouseMove(Location(693, 690))
    mouseDown(Button.LEFT)
    mouseMove(200, 0)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    print("earth temple shown")

    # find temple and click it
    templeRegion = Region(635,585,248,308)
    templeRegion.click("1493178397516.png")
    myRobot.delay(2000)


def restartBSandTheMission():
    Utilities.closeBS()
    myRobot.delay(60000)
    Utilities.launchBS()
    myRobot.delay(1000)
    Utilities.enterBSFFBE()
    myRobot.delay(1000)
    Utilities.waitForBSFFBEDesktop()
    myRobot.delay(2000)
    changeToRightTeam()
    myRobot.delay(2000)
    goToEarthTemple()
    myRobot.delay(1000)
    Utilities.log('RestartLog.txt', 'Restart', 'Restart the whole BS')

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 66, 15) # 701,851
    print("finding strengthen color")
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        myRobot.delay(2000)
    myRobot.delay(1000)

    print("finding waterAxeColor color")
    waterAxeColor = Color(97, 75, 75)  # (1194,417)
    while myRobot.getPixelColor(1194,417) != waterAxeColor:
        Utilities.fastClick(1254, 408)
        BonusGame.BonusGame.checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    # back to front pag
    print("finding letter color")
    letterColor = Color(180, 113, 99) # (1150, 175)
    while myRobot.getPixelColor(1150, 175) != letterColor:
        Utilities.fastClick(707, 1013)
        myRobot.delay(3000)
    myRobot.delay(1000)
    print("leaving chang team")

def setFollowerFilter():
    fastMissionColor = Color(99, 4, 7) # (703, 672)
    Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
    if buyStrength:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
                func_while_wait=Utilities.buyStrength)
    else:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)

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
    #Utilities.fastClick(702, 543) # 1st row
    #myRobot.delay(500)
    #Utilities.fastClick(778, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(925, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(999, 545)
    #myRobot.delay(500)
    #Utilities.fastClick(1071, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(1140, 548)
    #myRobot.delay(500)
    #Utilities.fastClick(1214, 545)
    #myRobot.delay(500)
    #Utilities.fastClick(702, 623) # 2nd row
    #myRobot.delay(500)
    #Utilities.fastClick(778, 623)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 623)
    #myRobot.delay(500)
    #Utilities.fastClick(925, 622)
    #myRobot.delay(500)
    #Utilities.fastClick(995, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1066, 619)
    #myRobot.delay(500)
    #Utilities.fastClick(1135, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1213, 627)
    #myRobot.delay(500)
    #Utilities.fastClick(710, 700) # 3rd row
    #myRobot.delay(500)
    #Utilities.fastClick(779, 698)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 698)
    #myRobot.delay(500)
    #Utilities.fastClick(927, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(995, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(1066, 695)
    #myRobot.delay(500)
    #Utilities.fastClick(1143, 695)
    #myRobot.delay(500)
    #Utilities.fastClick(1213, 693)
    #myRobot.delay(1000)

    # select generation
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    
    Utilities.fastClick(721, 624) # 1st row, FFBE
    myRobot.delay(500)
    Utilities.fastClick(814, 624) # FFI
    myRobot.delay(500)
    Utilities.fastClick(907, 624)
    myRobot.delay(500)
    #Utilities.fastClick(1000, 624)
    #myRobot.delay(500)
    Utilities.fastClick(1093, 624)
    myRobot.delay(500)
    Utilities.fastClick(1186, 624)
    myRobot.delay(500)
    Utilities.fastClick(721, 699) # 2nd row, FFVI
    myRobot.delay(500)
    Utilities.fastClick(814, 699)
    myRobot.delay(500)
    Utilities.fastClick(907, 699)
    myRobot.delay(500)
    Utilities.fastClick(1000, 699)
    myRobot.delay(500)
    Utilities.fastClick(1093, 699)
    myRobot.delay(500)
    Utilities.fastClick(1186, 699)
    myRobot.delay(500)
    Utilities.fastClick(721, 774) # 3rd row, FFXIV
    myRobot.delay(500)
    Utilities.fastClick(814, 774)
    myRobot.delay(500)
    Utilities.fastClick(907, 774)  # FFT
    myRobot.delay(500)
    Utilities.fastClick(1000, 774)
    myRobot.delay(500)
    Utilities.fastClick(767, 918)  # sepcial row, ANOTHER
    myRobot.delay(500)

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

def setFollowerFilterSpecial():
    fastMissionColor = Color(99, 4, 7) # (703, 672)
    Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
    if buyStrength:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
                func_while_wait=Utilities.buyStrength)
    else:
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)

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
    #Utilities.fastClick(702, 543) # 1st row
    #myRobot.delay(500)
    #Utilities.fastClick(778, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 543)
    #smyRobot.delay(500)
    #Utilities.fastClick(925, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(999, 545)
    #myRobot.delay(500)
    #Utilities.fastClick(1071, 543)
    #myRobot.delay(500)
    #Utilities.fastClick(1140, 548)
    #myRobot.delay(500)
    Utilities.fastClick(1214, 545)
    myRobot.delay(500)
    #Utilities.fastClick(702, 623) # 2nd row
    #myRobot.delay(500)
    #Utilities.fastClick(778, 623)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 623)
    #myRobot.delay(500)
    #Utilities.fastClick(925, 622)
    #myRobot.delay(500)
    #Utilities.fastClick(995, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1066, 619)
    #myRobot.delay(500)
    #Utilities.fastClick(1135, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1213, 627)
    #myRobot.delay(500)
    #Utilities.fastClick(710, 700) # 3rd row
    #myRobot.delay(500)
    #Utilities.fastClick(779, 698)
    #myRobot.delay(500)
    #Utilities.fastClick(854, 698)
    #myRobot.delay(500)
    #Utilities.fastClick(927, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(995, 697)
    #myRobot.delay(500)
    #Utilities.fastClick(1143, 695)
    #myRobot.delay(500)
    #Utilities.fastClick(1213, 693)
    #myRobot.delay(1000)    
    
    # select green magic
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(1141, 842)
    myRobot.delay(500) 

    # select generation 
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    
    #Utilities.fastClick(721, 624) # 1st row, FFBE
    #myRobot.delay(500)
    #Utilities.fastClick(814, 624) # FFI
    #myRobot.delay(500)
    #Utilities.fastClick(907, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1000, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1093, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(1186, 624)
    #myRobot.delay(500)
    #Utilities.fastClick(721, 699) # 2nd row, FFVI
    #myRobot.delay(500)
    #Utilities.fastClick(814, 699)
    #myRobot.delay(500)
    #Utilities.fastClick(907, 699)
    #myRobot.delay(500)
    #Utilities.fastClick(1000, 699)
    #myRobot.delay(500)
    #Utilities.fastClick(1093, 699)
    #myRobot.delay(500)
    #Utilities.fastClick(1186, 699)
    #myRobot.delay(500)
    #Utilities.fastClick(721, 774) # 3rd row, FFXIV
    #myRobot.delay(500)
    #Utilities.fastClick(814, 774)
    #myRobot.delay(500)
    Utilities.fastClick(907, 774)  # FFT
    myRobot.delay(500)
    #Utilities.fastClick(1000, 774)
    #myRobot.delay(500)
    #Utilities.fastClick(767, 918)  # sepcial row, ANOTHER
    #myRobot.delay(500)

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



if __name__ == "__main__":
    FFBEonDesktopColor = Color(131,181,22) # (113, 932)
    startFromNothing = myRobot.getPixelColor(113, 932) == FFBEonDesktopColor
    if startFromNothing:
        Utilities.launchBS()
        myRobot.delay(1000)
        Utilities.enterBSFFBE()
        myRobot.delay(1000)
        Utilities.waitForBSFFBEDesktop()
        print("after initial desktop")
        myRobot.delay(1000)
        changeToRightTeam()
        print("after change to right teima")
        myRobot.delay(2000)
        goToEarthTemple()
        myRobot.delay(1000)
    
    main()
    #steal()
    #harvestAndMakeHeal()
    