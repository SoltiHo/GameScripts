import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)

myRobot = JRobot()
selectFollower = False

def enterFastMission():
    fastMissionColor = Color(99, 5, 8) # (703, 672)
    Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 51, 141) # (954, 923)
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor, 
            func_while_wait=Utilities.buyStrength)

    # select follower
    followerColor = Color(0, 39, 93) # (1096, 223)    
    if selectFollower:
        Utilities.waitForColorAndDo(1096, 223, followerColor, 
                func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
    else:
        def waitAndSelectNoFollower():
            myRobot.delay(500)
            func_after_wait=Utilities.selectNoFollower()
        #followerColor = Color(22, 41, 54) # (916, 248)
        Utilities.waitForColorAndDo(1096, 223, followerColor, 
            func_after_wait=waitAndSelectNoFollower)

    launchColor = Color(0, 141, 218)  # (917, 892)
    Utilities.waitForColorAndDo(917, 892, launchColor)

def doBattles():
    nextStepColor = Color(0, 70, 182) # (925, 869)
    def attack():
        inBattleColor = Color(236, 218, 147) # (920, 204)
        waitingForCommandColor = Color(6, 51, 120) # (850, 701)
        if myRobot.getPixelColor(920, 204) == inBattleColor and myRobot.getPixelColor(850, 701) == waitingForCommandColor:
            myRobot.mouseMove(UNIT_CENTER_LOCATIONS[0].x, UNIT_CENTER_LOCATIONS[0].y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            myRobot.mouseMove(UNIT_CENTER_LOCATIONS[1].x, UNIT_CENTER_LOCATIONS[1].y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        Utilities.handleCommunicationError()

    Utilities.waitForColorAndDo(925, 869, nextStepColor, 
            func_while_wait=attack,
            func_after_wait=Utilities.handleMissionEnd)

def executeOneRound():
    enterFastMission()
    doBattles() 

def main():
    count = 0
    start = time.time()
    total_time = 0
    while True:
        if count == 0:
            start = time.time()
        count += 1
        executeOneRound()
        if count == 50:
            total_time = time.time() - start
            Utilities.log('FastTrustLog.csv', 'FastTrust', str(total_time) + ',' + str(count))
            count = 0

if __name__ == "__main__":
    main()
    