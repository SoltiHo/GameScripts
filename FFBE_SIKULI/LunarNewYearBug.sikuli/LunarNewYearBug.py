import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import Utilities

reload(Utilities)
myRobot = JRobot()
min_cycle_time = 50

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

def sellUnits():
    Utilities.fastClick(807, 1028)
    strengthenColor = Color(222, 225, 232) # (760, 858)
    waitCount = 0
    while myRobot.getPixelColor(760,858) != strengthenColor:
        myRobot.delay(1000)
        waitCount += 1
        if waitCount == 3:
            Utilities.fastClick(807, 1028)
            waitCount = 0

    # Then click on sell units
    Utilities.fastClick(1036, 710)    
    clearChoiceColor = Color(79, 9, 17) # (1108, 892)
    waitCount = 0
    while myRobot.getPixelColor(1108, 892) != clearChoiceColor:
        myRobot.delay(1000)
        waitCount += 1
        if waitCount == 3:
            Utilities.fastClick(1036, 710)
            waitCount = 0

    # chose the unit
    myRobot.delay(1000)
    Utilities.fastClick(717, 387)

    # click sell
    myRobot.delay(500)
    Utilities.fastClick(946, 892)
    myRobot.delay(500)

    # confirm
    confirmColor = Color(0, 31, 85)  # (1064, 597)
    Utilities.waitForColorAndDo(1064, 597, confirmColor)

    # click ok
    myRobot.delay(500)
    Utilities.fastClick(938, 599)

    # click front page
    myRobot.delay(500)
    Utilities.fastClick(704, 1031)
    myRobot.delay(1000)
    
    
def enterNewYearExplore():
    vertexColor = Color(66,27,183) # (1151, 788)
    # Utilities.waitForColorAndDo(1151, 788, vertexColor)
    waitCount = 0
    while myRobot.getPixelColor(1151, 788) != vertexColor:
        myRobot.delay(1000)
        waitCount += 1
        if waitCount == 20:
            print 'Vertex Error, restart BS FFBE'
            closeBSFFBE()
            myRobot.delay(5000)
            myRobot.mouseMove(879, 532)
            myRobot.delay(1000)
            return False
        
    while myRobot.getPixelColor(1151, 788) == vertexColor:
        Utilities.fastClick(1151, 788)
        myRobot.delay(1000)

    lunarNewYearColor = Color(253, 255, 96) # (748, 246)
    Utilities.waitForColorAndDo(748, 246, lunarNewYearColor)

    middleLevelColor = Color(65, 122, 89)  # (706, 535)
    Utilities.waitForColorAndDo(706, 535, middleLevelColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(898, 694))
    # 3rd position: (898, 694)
    # 2nd position: (868, 527)

    nextStepColor = Color(250, 251, 252)  # (935,933)
    Utilities.waitForColorAndDo(935, 933, nextStepColor,
            func_while_wait=Utilities.buyStrength)

    # Choose follower
    sortingColor = Color(163, 173, 195) # (1124, 245)
    Utilities.waitForColorAndDo(1124, 245, sortingColor,
            func_after_wait=Utilities.fastClick, arg_after_wait=(744, 372)) 
    # Launch
    launchColor = Color(255, 255, 255) # (945, 912)
    Utilities.waitForColorAndDo(945, 912, launchColor)

    return True

def waitForMissionMenu():
    menuColor = Color(166,127,116) # (1209, 1026)
    while myRobot.getPixelColor(1209, 1026) != menuColor:
        Utilities.handleCommunicationError()
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
    duOSFFBEColor = Color(212,191,219) # (495, 986)
    Utilities.waitForColorAndDo(495, 986, duOSFFBEColor)

def waitForDuOSFFBEMissionEnd():
    nextStepColor = Color(229, 233, 239) # (937, 902)
    def clickAndHandleCommError():
        Utilities.fastClick(960, 646)
        myRobot.delay(1000)
        Utilities.fastClick(925, 590)
        myRobot.delay(1000)
        Utilities.fastClick(495, 986)
        myRobot.delay(1000)
    Utilities.waitForColorAndDo(937, 902, nextStepColor,
            func_while_wait=clickAndHandleCommError)

    secondNextStepColor = Color(255, 255, 255) # (933, 905)
    Utilities.waitForColorAndDo(933, 905, secondNextStepColor,
            func_while_wait=Utilities.fastClick, arg_while_wait=(925, 590))

    #thirdNextStepColor = Color(129, 150, 176) # (936, 904)
    #Utilities.waitForColorAndDo(936, 904, thirdNextStepColor,
    #        func_while_wait=Utilities.fastClick, arg_while_wait=(925, 590))

    frontPageColor = Color(154, 2, 10) # (1190, 270)
    while myRobot.getPixelColor(1190, 270) != frontPageColor:
        Utilities.fastClick(847, 803)
        myRobot.delay(2000)
    print 'DuOS mission Completed'

def openDuOSAddCloseLine():
    myRobot.mouseMove(912, 1080)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(912, 780)    
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

    myRobot.delay(500)
    myRobot.mouseMove(1027, 1070)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def waitForFloatingWindow():
    myRobot.delay(3000)
    openDuOSAddCloseLine()

def closeMuOSFFBE():
    openDuOSAddCloseLine()
    
    # wait for floating window
    floatingFrontPageColor = Color(118, 55, 80) # (1261, 462)
    count = 0
    while myRobot.getPixelColor(1261, 462) != floatingFrontPageColor:
        myRobot.delay(1000)
        count += 1
        if count == 6:
            openDuOSAddCloseLine()
            count = 0
    myRobot.delay(1000)
    Utilities.fastClick(1328, 191)
    myRobot.delay(3000)

    # wait for DuOS FFBE
    duOSFFBEColor = Color(212,191,219) # (495, 986)
    while myRobot.getPixelColor(495, 986) != duOSFFBEColor:
        myRobot.delay(1000)
    print 'back to DuOS Desktop'


def mainLoop():
    while True:
        skip_the_round = False
        start = time.time()
        enterBSFFBE()
        myRobot.delay(2000)
        waitForBSFFBEDesktop()
        myRobot.delay(2000)
        #sellUnits()
        if enterNewYearExplore():
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
    
        end = time.time()
        remaining = min_cycle_time - (end - start)
        if remaining > 0:
            wait(remaining)
        total_time = time.time() - start
        Utilities.log('LunarNewYearLog.csv', 'Explore', str(total_time))

if __name__ == "__main__":
    mainLoop()
    #waitForDuOSFFBEMissionEnd()
    #closeMuOSFFBE()