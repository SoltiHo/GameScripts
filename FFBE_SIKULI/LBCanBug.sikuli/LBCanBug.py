#type("\t", KEY_ALT) 
import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import Utilities

reload(Utilities)
myRobot = JRobot()

SkipExpMerge = True
expTarget = Location(962, 548)
lbTarget = Location(962, 548)

def main():
    while True:
        # open FFBE in BS
        Utilities.enterBSFFBE()
        myRobot.delay(3000)
    
        # wait for desktopLocation(687, 265)
        Utilities.waitForBSFFBEDesktop()
        myRobot.delay(2000)
        
        # sell and merge units
        mergeAndSell()
        myRobot.delay(2000)
        
        # enter the mission again
        enterBSMission()
        myRobot.delay(1000)
    
        # close FFBE BS app
        Utilities.closeBSFFBE()
    
        # switch to DuOS
        Utilities.switchEmulator()
    
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
            click(Location(954, 939))
            myRobot.delay(1000)
        myRobot.delay(1000)
    
        # close DuOS FFBE
        closeMuOSFFBE()
    
        # switch back to BS
        type("\t", KEY_ALT)
        myRobot.delay(1000)
    
        # wait for DuOS to close completely
        BSFFBEColor = Color(224, 132, 169) # (335, 198)
        while myRobot.getPixelColor(335, 198) != BSFFBEColor:
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
    strengthenColor = Color(243, 187, 161) # (864, 848)
    click(Location(807, 1026)) # click Units
    myRobot.delay(2000)
    while myRobot.getPixelColor(864, 848) != strengthenColor:
        myRobot.delay(1000)
    myRobot.delay(2000)

    # click sell unit
    sellColor = Color(93, 11, 20)  # (1180, 246)
    Utilities.waitForColorAndDo(1180, 246, sellColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[816, 708])
    myRobot.delay(2000)


    Utilities.fastClick(712, 378)
    myRobot.delay(500)
    if SkipExpMerge:
        Utilities.fastClick(839, 383) # 2nd
        myRobot.delay(500)
        Utilities.fastClick(959, 373) # 3rd
        myRobot.delay(500)
        Utilities.fastClick(1082, 382) # 4
        myRobot.delay(500)
        Utilities.fastClick(1197, 390) # 5
        myRobot.delay(500)
        Utilities.fastClick(715, 551) # 6
        myRobot.delay(500)
    myRobot.delay(1000)

    # sell
    confirmSellColor = Color(147, 0, 7)  # (1047, 823)
    Utilities.waitForColorAndDo(1047, 823, confirmSellColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[998, 893])
    myRobot.delay(1000)

    # 2nd confirm
    secondConfirmColor = Color(102, 0, 0)  # (1034, 588)
    Utilities.waitForColorAndDo(1034, 588, secondConfirmColor)
    myRobot.delay(1000)

    # OK
    okColor = Color(0, 79, 178) # (900, 577)
    Utilities.waitForColorAndDo(900, 577, okColor)
    myRobot.delay(3000)
    
    # go back to frontpage and click vertex
    vertexColor = Color(223, 225, 240) # (802, 614)
    while myRobot.getPixelColor(802, 614) != vertexColor:
        myRobot.delay(4000)
        Utilities.fastClick(705, 1026)  # click front page
    print("back at front page")
    
def mergeUnits():
    global lbTarget
    strengthenColor = Color(243, 187, 161) # (864, 848)
    click(Location(807, 1026)) # click Units
    myRobot.delay(2000)
    Utilities.waitForColorAndDo(864, 848, strengthenColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[807, 1026])
    myRobot.delay(2000)
    # Merge
    click(lbTarget)  # select Target
    myRobot.delay(2000)

    firstSpotColor = Color(174, 174, 174) # (719, 753)
    Utilities.waitForColorAndDo(719, 753, firstSpotColor)

    lbCanColor = Color(111, 113, 41)  # (1068, 394)
    while myRobot.getPixelColor(1068, 394) != lbCanColor:
        myRobot.delay(1000)

    Utilities.fastClick(1068, 394)
    myRobot.delay(1000)

    okColor = Color(255, 255, 255) # (942, 898)
    print('waiting for okColor')
    Utilities.waitForColorAndDo(942, 898, okColor)
    myRobot.delay(1000)

    mergeColor = Color(255, 255, 255) # (981, 890)
    print('waiting for mergeColor')
    while myRobot.getPixelColor(981, 890) == mergeColor:
        myRobot.delay(1000)
        Utilities.fastClick(981, 890)
    myRobot.delay(2000)

    # wait for merge animation
    while myRobot.getPixelColor(981, 890) != mergeColor:
        myRobot.delay(1000)
        Utilities.fastClick(1070, 893)
        print('waiting for 2nd merge color')
    myRobot.delay(2000)
        

def mergeExpUnits():
    global expTarget
    strengthenColor = Color(243, 187, 161) # (864, 848)
    click(Location(807, 1026)) # click Units
    myRobot.delay(2000)
    Utilities.waitForColorAndDo(864, 848, strengthenColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[807, 1026])
    myRobot.delay(2000)
    # Merge
    click(expTarget)  # select Target
    myRobot.delay(2000)

    firstSpotColor = Color(174, 174, 174) # (719, 753)
    Utilities.waitForColorAndDo(719, 753, firstSpotColor)
    myRobot.delay(1000)
    click(Location(717, 384)) # 1st
    myRobot.delay(500)
    click(Location(834, 391)) # 2nd
    myRobot.delay(500)
    click(Location(958, 391)) # 3rd
    myRobot.delay(500)
    click(Location(1076, 386)) # 4th
    myRobot.delay(500)
    click(Location(714, 560)) # 6th
    myRobot.delay(500)

    click(Location(958, 901)) # ok
    myRobot.delay(1000)
    click(Location(966, 901))  # merge confirm
    myRobot.delay(1000)
    cleanSelectionColor = Color(143,93,98) # (1132,889)
    while myRobot.getPixelColor(1132, 889) != cleanSelectionColor:
        click(Location(1185, 898))
        myRobot.delay(500)

def enterBSMission():
    mazeColor = Color(254, 179, 239) # (877, 518)
    Utilities.waitForColorAndDo(877, 518, mazeColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=[839, 566])
    myRobot.delay(2000)

    def checkAndBuyStrength():
        Utilities.fastClick(911, 384)
        myRobot.delay(1500)
        Utilities.fastClick(1051, 538)
        myRobot.delay(1500)
        Utilities.fastClick(1011, 590)
        myRobot.delay(1500)
    nextStepColor = Color(247, 247, 249) # (960, 948)
    Utilities.waitForColorAndDo(960, 948, nextStepColor,
            func_while_wait=checkAndBuyStrength)
    myRobot.delay(2000)

    # select first follower
    Utilities.fastClick(843, 377)
    myRobot.delay(1000)

    # launch
    menuColor = Color(134, 113, 70)  # (1229, 1022)
    while myRobot.getPixelColor(1229, 1022) != menuColor:
        myRobot.delay(1000)
        Utilities.fastClick(902, 949) # click launch
        print('waiting for menu')

def waitForDuOSFFBEandOpen():
    print 'waitForDuOSFFBEandOpen'
    DuOSFFBEColor = Color(237,170,198) #(503, 988)
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
    DuOSFFBEColor = Color(237,170,198) #(503, 988)
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
    #sellRemainingUnits()
    #waitForDuOSFFBEandOpen()