#type("\t", KEY_ALT) 
import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import Utilities

reload(Utilities)
myRobot = JRobot()

SkipExpMerge = True
expTarget = Location(516, 421)
lbTarget = Location(832, 641)

def main():
    while True:
        # open FFBE in BS
        click(Location(282, 323))
        myRobot.delay(3000)
    
        # wait for desktopLocation(687, 265)
        floorColor = Color(255, 195, 250) # Location(830, 830)
        while myRobot.getPixelColor(830, 830) != floorColor:
            myRobot.mouseMove(521, 599)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
            myRobot.delay(500)
        myRobot.delay(2000)
        
        # sell and merge units
        mergeAndSell()
        myRobot.delay(1000)
        
        # enter the mission again
        enterBSMission()
        myRobot.delay(1000)
    
        # wait for mission start
        menuColor = Color(149,116,13) # 845, 845
        while myRobot.getPixelColor(845,845) != menuColor:
            myRobot.delay(1000)
        myRobot.delay(1000)
    
        # close FFBE BS app
        click(Location(377, 166))
        myRobot.delay(2000)
    
        # switch to DuOS
        type("\t", KEY_ALT)
        myRobot.delay(1000)
    
        # wait for DuOS to boot
        waitForDuOSFFBEandOpen()
        # wait for DuOS FFBE result window
        resultRedColor = Color(126, 0, 3) # (986, 264)
        while myRobot.getPixelColor(986, 264) != resultRedColor:
            click(Location(961, 649))
            click(Location(986, 264))
            myRobot.delay(1000)
            print('waiting for result color')
        print('saw result red color')
        myRobot.delay(1000)
    
        # next step and wait for front page
        frontPageColor = Color(180, 29, 37) # (1187, 265)
        while myRobot.getPixelColor(1187, 265) != frontPageColor:
            click(Location(961, 895))
            click(Location(825, 801))
            myRobot.delay(1000)
        myRobot.delay(1000)
    
        # close DuOS FFBE
        closeMuOSFFBE()
    
        # switch back to BS
        type("\t", KEY_ALT)
        myRobot.delay(1000)
    
        # wait for DuOS to close completely
        BSFFBEColor = Color(152, 106, 67) # (273, 316)
        while myRobot.getPixelColor(273, 316) != BSFFBEColor:
            myRobot.delay(1000)
        myRobot.delay(1000)
        print 'saw BS FFBE, continue'
    myRobot.delay(2000)
    




def mergeAndSell():
    mergeUnits()
    if not SkipExpMerge:
        mergeExpUnits()
    sellRemainingUnits()

def sellRemainingUnits():
    global SkipExpMerge
    click(Location(581, 846))
    myRobot.delay(2000)
    # sell
    click(Location(764, 640))
    myRobot.delay(1000)
    click(Location(526, 411)) # 1st
    myRobot.delay(500)
    if SkipExpMerge:
        click(Location(602, 430)) # 2nd
        myRobot.delay(500)
        click(Location(679, 420)) # 3rd
        myRobot.delay(500)
        click(Location(761, 423)) # 4th
        myRobot.delay(500)
        click(Location(831, 420)) # 5th
        myRobot.delay(500)
        click(Location(522, 538)) # 6th
        myRobot.delay(500)

    # sell
    click(Location(675, 753))
    myRobot.delay(1000)
    # confirm 1
    click(Location(756, 576))
    myRobot.delay(1000)
    # confirm 2
    click(Location(756, 576))
    myRobot.delay(1000)
    # OK
    click(Location(675, 567))
    myRobot.delay(1000) 


def mergeUnits():
    global lbTarget
    unitOneColor = Color(254, 254, 254) # (585, 638)
    click(Location(581, 846)) # click Units
    wait_count = 0
    while myRobot.getPixelColor(585, 638) != unitOneColor:
        myRobot.delay(500)
        wait_count += 1
        if wait_count == 4:
            click(Location(581, 846)) # click Units
            wait_count = 0
    myRobot.delay(1000)
    # Merge
    click(Location(573, 731))
    myRobot.delay(2000)
    click(lbTarget)  # select Target
    myRobot.delay(1500)
    click(Location(522, 648))
    myRobot.delay(1000)
    click(Location(756, 430))
    myRobot.delay(500)
    click(Location(674, 763))
    myRobot.delay(1000)
    click(Location(674, 763))  # merge confirm
    myRobot.delay(1000)
    cleanSelectionColor = Color(87,10,18) # (779, 753)
    while myRobot.getPixelColor(779, 753) != cleanSelectionColor:
        click(Location(797, 715))
        myRobot.delay(500)

def mergeExpUnits():
    global expTarget
    click(Location(581, 846))
    myRobot.delay(2000)
    # Merge
    click(Location(556, 733))
    myRobot.delay(2000)
    click(expTarget)   # select Target
    myRobot.delay(1500)
    click(Location(522, 648))  # select spot
    myRobot.delay(1000)
    click(Location(526, 411)) # 1st
    myRobot.delay(500)
    click(Location(602, 430)) # 2nd
    myRobot.delay(500)
    click(Location(679, 420)) # 3rd
    myRobot.delay(500)
    click(Location(761, 423)) # 4th
    myRobot.delay(500)
    click(Location(522, 538)) # 6th
    myRobot.delay(500)

    click(Location(674, 763))
    myRobot.delay(1000)
    click(Location(674, 763))  # merge confirm
    myRobot.delay(1000)
    cleanSelectionColor = Color(87,10,18) # (779, 753)
    while myRobot.getPixelColor(779, 753) != cleanSelectionColor:
        click(Location(818, 750))
        myRobot.delay(500)

def enterBSMission():
    click(Location(520, 844))
    myRobot.delay(1000)
    vertexColor = Color(152, 145, 186) # (820, 688)
    Utilities.waitForColorAndDo(820, 688, vertexColor)
    #while myRobot.getPixelColor(820, 688) != vertexColor:
    #    myRobot.delay(1000)
    #    print('wait for vertex')
    #myRobot.delay(500)
    #click(Location(832, 695)) # vertex
    myRobot.delay(1000)
    missionColor = Color(202,23,139) # (629, 375)
    while myRobot.getPixelColor(629, 375) != missionColor:
        myRobot.delay(1000)
        print('waiting for mission color')
    myRobot.delay(500)
    click(Location(629,375)) 
    myRobot.delay(1000)
    click(Location(603, 427)) # easy 
    myRobot.delay(1000)
    # waiting for next step
    stoneColor = Color(4,36,189) # (839, 703)
    while myRobot.getPixelColor(839, 703) != stoneColor:
        print 'waiting for stone'
        # buying strength
        click(Location(788, 576))
        myRobot.delay(500)
    click(Location(674, 782))
    myRobot.delay(1000)
    click(Location(562, 422)) # select the 1st follower
    myRobot.delay(1000)
    click(Location(681, 771)) # depart

def waitForDuOSFFBEandOpen():
    print 'waitForDuOSFFBEandOpen'
    DuOSFFBEColor = Color(192,129,81) #(503, 988)
    while myRobot.getPixelColor(503, 988) != DuOSFFBEColor:
        print 'wait for DuOS FFBE color'
        myRobot.delay(1000)
    myRobot.delay(1000)
    print 'after loop'
    # open DuOS FFBE
    click(Location(503, 988))
    myRobot.delay(500)


def closeMuOSFFBE():
    myRobot.mouseMove(912, 1080)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(912, 780)    
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

    myRobot.delay(500)
    myRobot.mouseMove(1027, 1070)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(2500)

    # wait for DuOS background color
    backgroundColor = Color(200,237,230) # (1569, 449)
    while myRobot.getPixelColor(1569,449) != backgroundColor:
        myRobot.delay(500)
        print('waiting for DuOS background Color')
    myRobot.delay(500)

    # close
    myRobot.mouseMove(1330, 192)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

    # wait for DuOS FFBE Desktop
    DuOSFFBEColor = Color(192,129,81) #(503, 988)
    while myRobot.getPixelColor(503, 988) != DuOSFFBEColor:
        print 'wait for DuOS FFBE color'
        myRobot.delay(1000)
    myRobot.delay(1000)


if __name__ == "__main__":
    #enterBSMission()
    #mergeUnits()
    #mergeExpUnits()
    #wait(10)
    main()
    #waitForDuOSFFBEandOpen()