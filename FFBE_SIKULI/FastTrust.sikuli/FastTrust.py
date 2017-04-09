import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)

myRobot = JRobot()
selectFollower = True
buyStrength = False

def enterFastMission():
    fastMissionColor = Color(99, 5, 8) # (703, 672)
    Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
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

def steal():
    # To steal
    Utilities.openMagicMenu(1)
    myRobot.delay(700)
    Utilities.fastClick(820, 918)
    myRobot.delay(700)

def doBattles():
    nextStepColor = Color(0, 39, 113) # (958, 943)
    AutoColor = Color(0, 136, 175) # (725, 1023)
    def attack():
        monsterBloodColor = Color(143, 222, 77) # (846, 628)
        waitingForCommandColor = Color(6, 51, 120) # (850, 701)
        if myRobot.getPixelColor(846, 628) == monsterBloodColor and myRobot.getPixelColor(850, 701) == waitingForCommandColor:
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

    def checkAndRestartBSFFBE():
        BSFFBEColor = Color(230,191,216) # (330, 196)
        if myRobot.getPixelColor(330, 196) == BSFFBEColor:
            Utilities.fastClick(330, 196)
            myRobot.delay(5000)
            menuColor = Color(0, 17, 51) # (1150, 1032)
            while myRobot.getPixelColor(1189,1025) != menuColor:
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
    worldColor = Color(244, 137, 60) # (944, 808)
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
        count += 1
        executeOneRound()
        #if count % 10 == 0:
        #    harvestAndMakeHeal()
        if count == 50:
            total_time = time.time() - start
            Utilities.log('FastTrustLog.csv', 'FastTrust', str(total_time) + ',' + str(count))
            count = 0

if __name__ == "__main__":
    main()
    #steal()
    #harvestAndMakeHeal()
    