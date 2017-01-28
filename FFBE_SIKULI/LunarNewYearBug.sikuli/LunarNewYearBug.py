import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import Utilities

reload(Utilities)
myRobot = JRobot()

def enterBSFFBE():
    BSFFBEColor = Color(222,171,131) # (330, 196)
    Utilities.waitForColorAndDo(330, 196, BSFFBEColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(330, 196))
    print 'entered BS FFBE'

def waitForBSFFBEDesktop():
    friendColor = Color(255,184,254) # (1189, 1025)
    while myRobot.getPixelColor(1189,1025) != friendColor:
        Utilities.fastClick(962, 940)
    print 'saw BS FFBE Desktop'

def enterNewYearExplore():
    vertexColor = Color(66,27,183) # (1151, 788)
    Utilities.waitForColorAndDo(1151, 788, vertexColor)

    lunarNewYearColor = Color(253, 255, 96) # (748, 246)
    Utilities.waitForColorAndDo(748, 246, lunarNewYearColor)

    middleLevelColor = Color(65, 122, 89)  # (706, 535)
    Utilities.waitForColorAndDo(706, 535, middleLevelColor)

    nextStepColor = Color(250, 251, 252)  # (935,933)
    Utilities.waitForColorAndDo(935, 933, nextStepColor)

    # Choose follower
    sortingColor = Color(163, 173, 195) # (1124, 245)
    Utilities.waitForColorAndDo(1124, 245, sortingColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(744, 372)) 
    # Launch
    launchColor = Color(255, 255, 255) # (945, 912)
    Utilities.waitForColorAndDo(945, 912, launchColor)
    print 'Entered explore mission'

def waitForMissionMenu():
    menuColor = Color(166,127,116) # (1209, 1026)
    while myRobot.getPixelColor(1209, 1026) != menuColor:
        myRobot.delay(1000)
    print 'saw explore mission menu'

def closeBSFFBE():
    myRobot.mouseMove(327, 5)
    myRobot.delay(500)

    FFBETopColor = Color(226, 176, 156) # (202, 10)
    Utilities.waitForColorAndDo(202, 10, FFBETopColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(310, 10))
    print 'BS FFBE closed'

def switchEmulator():
    # switch emulator
    type("\t", KEY_ALT)
    myRobot.delay(1000)

def openDuOSFFBE():
    duOSFFBEColor = Color(171, 116, 84) # (495, 986)
    Utilities.waitForColorAndDo(495, 986, duOSFFBEColor)

def waitForDuOSFFBEMissionEnd():
    nextStepColor = Color(214, 223, 233)
    Utilities.waitForColorAndDo(495, 986, duOSFFBEColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=(925, 590))

    secondNextStepColor = Color(210, 218, 227) # (938, 955)
    Utilities.waitForColorAndDo(938, 955, secondNextStepColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=(925, 590))

    thirdNextStepColor = Color(129, 150, 176) # (936, 904)
    Utilities.waitForColorAndDo(936, 904, thirdNextStepColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=(925, 590))

    frontPageColor = Color(154, 2, 10) # (1190, 270)
    while myRobot.getPixelColor(1190, 270) != frontPageColor:
        myRobot.delay(1000)
    print 'DuOS mission Completed'

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


def mainLoop():
    while True:
        enterBSFFBE()
        myRobot.delay(2000)
        waitForBSFFBEDesktop()
        myRobot.delay(2000)
        enterNewYearExplore()
        myRobot.delay(2000)
        waitForMissionMenu()
        myRobot.delay(2000)
        closeBSFFBE()
        myRobot.delay(2000)
        switchEmulator()
        myRobot.delay(2000)
        openDuOSFFBE()
        myRobot.delay(2000)
        waitForDuOSFFBEMissionEnd()
        myRobot.delay(2000)
        closeMuOSFFBE()
        myRobot.delay(2000)
        switchEmulator()
        myRobot.delay(2000)

if __name__ == "__main__":
    mainLoop()
    