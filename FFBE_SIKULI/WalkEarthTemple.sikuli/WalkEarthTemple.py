import java.awt.Robot as JRobot
import java.awt.Color as Color
import Utilities
import TrainLB as LB

reload(Utilities)
reload(LB)
myRobot = JRobot()
battle_count = 0

missionNextStepRegion = Region(914,909,90,44)
missionNextStepPicture = "1479022885841.png"
FollowerRegion = Region(768,209,139,47)
LaunchRegion = Region(910,883,107,65)
total_LB = 0
fastMode = True
def main():
    global total_LB
    global battle_count
    while True:
        total_LB = 0
        start = time.time()
        # enter the explore
        # java.awt.Color[r=20,g=78,b=45]   (700, 389)
        exploreColor = Color(0x14, 0x4E, 0x2D)
        while not myRobot.getPixelColor(700,389) == exploreColor:
            print "waiting for explore color"
            wait(1)
        while myRobot.getPixelColor(700,389) == exploreColor:
            click(Location(700,389))
            print "clicking explore"
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
    
        
        while not FollowerRegion.exists("1479022675016.png"):
            print "iteration ", count, ": waiting follower"
            click(missionNextStepRegion)
            myRobot.delay(500)
    
        # choose no follower
        Utilities.selectNoFollower()
    
        # ready to launch
        while not LaunchRegion.exists("1479022755293.png"):
            click(Location(810, 404))
            wait(1)
        click(LaunchRegion)
        wait(3)
        # make sure entered the explore
        #java.awt.Color[r=57,g=114,b=194] (1135, 1030)
        switchMapColor = Color(0x39, 0x72, 0xC2)
        while not myRobot.getPixelColor(1135, 1030) == switchMapColor:
            click(Location(962, 646))
            print "waiting for switch map"
            wait(1)
        wait(1)
        battle_count = 0
        walkthrough()

        
        LB_time, num_LB_used = LB.doTrainLB(14 - battle_count, 'LeftRight')
        myRobot.delay(1000)
        total_LB += num_LB_used
        
        # go to left most reference point
        myRobot.mouseMove(961, 494)
        mouseDown(Button.LEFT)
        mouseMove(-270, 0)
        myRobot.delay(3000)
        mouseUp(Button.LEFT)
    
        count = 0
        while count < 6:
            MoveRightAndCheckBattle()
            myRobot.delay(300)
            count = count + 1
            
        # Go meet Boss
        myRobot.mouseMove(961, 494)
        mouseDown(Button.LEFT)
        mouseMove(0, -270)
        myRobot.delay(3000)
        mouseUp(Button.LEFT)
    
        # fight Boss
        click(Location(1121, 291))
        wait(3)
        click(Location(1121, 291))
        wait(2)
        total_LB += LB.doBattle(True)
        click(Location(962, 583))
        myRobot.delay(500)
        click(Location(962, 583))
        myRobot.delay(500)
        click(Location(962, 583))
        myRobot.delay(500)
        click(Location(1142, 292))
        
        # The last mine
        wait(2)
        count = 0
        while count < 3:
            Utilities.moveLeft()
            myRobot.delay(300)
            count = count + 1
        Utilities.moveDown()
        myRobot.delay(300)
        Utilities.moveDown()
        myRobot.delay(300)
        Utilities.moveUp()
        myRobot.delay(300)
        Utilities.moveUp()
        myRobot.delay(300)
        count = 0
        while count < 3:
            Utilities.moveRight()
            myRobot.delay(300)
            count = count + 1
        
        myRobot.mouseMove(961, 494)
        mouseDown(Button.LEFT)
        mouseMove(0, -270)
        myRobot.delay(3000)
        mouseUp(Button.LEFT)
        
        click(Location(1162, 291))
        wait(3)
    
        Utilities.handleMissionEnd()
        
        total_time = time.time() - start
        Utilities.log('LbLog.csv', 'LB', str(total_time) + ',' + str(LB_time) + ',' + str(total_LB))
        remaining = 900 - (time.time() - start)
        #break
        #if remaining > 0: wait(remaining)


def walkthrough():
    global battle_count
    # return to reference point
    myRobot.mouseMove(961, 494)
    mouseDown(Button.LEFT)
    mouseMove(0, 270)
    myRobot.delay(3000)
    mouseUp(Button.LEFT)
    MoveUpAndCheckBattle()
    myRobot.delay(2000)
    count = 0
    while count < 7:    
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 16:    
        MoveLeftAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 20:    
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 32:    
        MoveRightAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 16:    
        MoveDownAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 3:
        MoveRightAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    MoveDownAndCheckBattle()
    myRobot.delay(300)
    MoveUpAndCheckBattle()
    myRobot.delay(300)
    MoveLeftAndCheckBattle()
    myRobot.delay(300)
    MoveLeftAndCheckBattle()
    myRobot.delay(300)
    MoveLeftAndCheckBattle()
    myRobot.delay(300)
    count = 0
    while count < 37:
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    MoveRightAndCheckBattle()
    myRobot.delay(300)
    MoveRightAndCheckBattle()
    myRobot.delay(300)
    MoveRightAndCheckBattle()
    myRobot.delay(300)
    count = 0
    while count < 5:
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    count = 0
    while count < 2:
        MoveLeftAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    count = 0
    while count < 4:
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    MoveLeftAndCheckBattle()
    myRobot.delay(300)
    MoveUpAndCheckBattle()
    myRobot.delay(300)
    count = 0
    while count < 12:
        MoveUpAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    count = 0
    while count < 16:
        MoveDownAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 3:
        MoveRightAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 5:
        MoveDownAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    
    count = 0
    while count < 19:
        MoveLeftAndCheckBattle()
        myRobot.delay(300)
        count = count + 1
    MoveUpAndCheckBattle()
    myRobot.delay(300)
    MoveUpAndCheckBattle()
    myRobot.delay(300)


def checkAndDoBattle():
    global total_LB
    if Utilities.isInBattle():
        myRobot.delay(1000)
        total_LB += LB.doBattle(False)
        myRobot.delay(1000)
        return True
    else:
        return False

def MoveUpAndCheckBattle():
    global battle_count
    Utilities.moveUp()
    if (checkAndDoBattle()):
        battle_count += 1
        Utilities.moveUp()

def MoveDownAndCheckBattle():
    global battle_count
    Utilities.moveDown()
    if checkAndDoBattle():
        battle_count += 1
        Utilities.moveDown()

def MoveLeftAndCheckBattle():
    global battle_count
    Utilities.moveLeft()
    if checkAndDoBattle():
        battle_count += 1
        Utilities.moveLeft()

def MoveRightAndCheckBattle():
    global battle_count
    Utilities.moveRight()
    if checkAndDoBattle():
        battle_count += 1
        Utilities.moveRight()

if __name__ == "__main__":
    main()
    #walkthrough()

