import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)
DeepestSwordRegion = Region(680,506,51,45)
SwordPicture = "1479022584013.png"
missionNextStepRegion = Region(914,909,90,44)
missionNextStepPicture = "1479022885841.png"
count = 0
while True:
    start = time.time()
    count = count + 1

    while not DeepestSwordRegion.exists(SwordPicture,1):
        print "iteration ", count, ": waiting deepest sword"
        wait(1)
    click(DeepestSwordRegion)
    wait(0.5)

    # Dismiss mission description    
    while not missionNextStepRegion.exists(missionNextStepPicture,1):
        click(DeepestSwordRegion)
        wait(1)
    
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

    wait(2)
    click(AutoRegion)


    #1st next step
    NextStepRegion = Region(862,837,206,120)
    while not NextStepRegion.exists("1479079732102.png",1):
        print "iteration ", count, ": waiting 1st next step"
        click(Location(712, 745))
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

    remaining = 300 - (time.time() - start)
    if remaining > 0: wait(remaining)

