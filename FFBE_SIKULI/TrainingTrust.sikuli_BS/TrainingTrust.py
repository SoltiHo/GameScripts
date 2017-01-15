import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)

myRobot = JRobot()
fastMode = False
missionNextStepPicture = "1479022885841.png"
count = 0
LB_used = 0
start = time.time()
while True:
    this_round_start = time.time()
    if count <= 20:
        count = count + 1
    else:
        start = time.time()
        LB_used = 0
        count = 1

    # sword color = [r=98,g=4,b=7]   (702, 511)
    swordColor = Color(0x62, 0x04, 0x07)
    while not myRobot.getPixelColor(702,511) == swordColor:
        print "waiting for sword color"
        wait(1)
    while myRobot.getPixelColor(702,511) == swordColor:
        click(Location(702,511))
        print "clicking sword"
        wait(0.5)

    # Dismiss mission description    
    # java.awt.Color[r=0,g=54,b=142] (1010, 946)
    dismissColor = Color(0x00, 0x36, 0x8E)
    while not myRobot.getPixelColor(1010, 946) == dismissColor:
        print "waiting for dismissColor"
        # buy strength if fast mode
        buyStrengthColor = Color(70, 0, 0) # (1039, 613)
        if myRobot.getPixelColor(1039, 613) == buyStrengthColor:
            if fastMode:
                myRobot.mouseMove(1039, 613)
                myRobot.mousePress(InputEvent.BUTTON1_MASK)
                myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            else:
                print "no more stength in normal mode"
                exit(1)
        wait(1)
    while myRobot.getPixelColor(1010, 946) == dismissColor:
        click(Location(1010, 946))
        myRobot.delay(500)
    
    # choose follower
    FollowerRegion = Region(768,209,139,47)
    while not FollowerRegion.exists("1479022675016.png"):
        print "iteration ", count, ": waiting follower"
        click(missionNextStepRegion)
        wait(0.5)

    # select the first
    click(Location(810, 404))

    LaunchRegion = Region(910,883,107,65)
    while not LaunchRegion.exists("1479022755293.png"):
        print "iteration ", count, ": waiting launch"
        click(Location(810, 404))
        wait(1)
    click(LaunchRegion)
    wait(3)


    # entering battle
    AutoRegion = Region(656,1006,146,63)
    while not AutoRegion.exists("1479023165984.png"):
        print "iteration ", count, ": waiting auto"
        #click(LaunchRegion) 
        click(Location(962, 646))
        wait(1)

    # Boss foot color java.awt.Color[r=188,g=183,b=125]
    # attacking color java.awt.Color[r=0,g=119,b=147]
    BossFootColor = Color(0xBC,0xB7,0x7D)
    NotAttackingColor = Color(0x00,0x77,0x93)
    myRobot = JRobot() 
    while myRobot.getPixelColor(857, 474) != BossFootColor:
        if myRobot.getPixelColor(1052, 1022) == NotAttackingColor:
            myRobot.mouseMove(774, 466)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            myRobot.mouseMove(868, 366)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            Utilities.manuallyKickOff()
        wait(1)

    if Utilities.lookHavingLB(1):
        LB_used += 1
    if Utilities.lookHavingLB(2):
        LB_used += 1
    if Utilities.lookHavingLB(3):
        LB_used += 1
    if Utilities.lookHavingLB(4):
        LB_used += 1
    if Utilities.lookHavingLB(5):
        LB_used += 1

            
    click(AutoRegion)
    #Utilities.manuallyKickOff()

    Utilities.handleMissionEnd()

    if count == 20:
        total_time = time.time() - start
        Utilities.log('TrustLog.csv', 'Trust', str(total_time) + ',' + str(LB_used))
    remaining = 300 - (time.time() - this_round_start)
    if remaining > 0: wait(remaining)



def backupCode():
    #1st next step
    NextStepRegion = Region(862,837,206,120)
    while not NextStepRegion.exists("1479079732102.png",1):
        print "iteration ", count, ": waiting 1st next step"
        click(Location(712, 745))
        Utilities.handleCommunicationError()
        wait(1)
    print "iteration ", count, ": 1st next step found"
    wait(1)
    while NextStepRegion.exists("1479079732102.png",1):
        click(NextStepRegion)

    # 2nd next step 
    while not NextStepRegion.exists("1479079794939.png",1):
        print "iteration ", count, ": waiting 2nd next step"
        click(Location(712, 745))
    wait(1)
    while NextStepRegion.exists("1479079794939.png",1):
        click(NextStepRegion)
    
    # Friends
    FriendApplyRegion = Region(750,747,124,79)
    wait(1)
    while FriendApplyRegion.exists("1479081918270.png"):
        click(FriendApplyRegion)
        wait(1)

    # Close Mission
    CloseMissionRegion = Region(726,620,180,87)
    while CloseMissionRegion.exists("1479197182789.png"):
        click(CloseMissionRegion)
        wait(1)


