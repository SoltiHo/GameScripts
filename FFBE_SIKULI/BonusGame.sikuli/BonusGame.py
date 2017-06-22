import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)
myRobot = JRobot()


def selectUnit1_AttackAll():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1031, 830)
    myRobot.delay(1500)

def selectUnit1_rose():
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(802, 842)
    myRobot.delay(800)

def selectUnit3_randomAttack():
    Utilities.openMagicMenu(3)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.fastClick(1057, 839)
    myRobot.delay(800)

def selectUnit5_MPDance():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(778, 839)
    myRobot.delay(1500)

def selectUnit5_reduceDefence():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.fastClick(793, 730)
    myRobot.delay(1500)

def battle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    myRobot.delay(2000)
    selectUnit1_AttackAll()
    myRobot.delay(1000)
    selectUnit5_MPDance()
    myRobot.delay(1000)

    Utilities.fastClick(794, 728)
    myRobot.delay(300)
    Utilities.fastClick(1071, 819)
    menuColor = Color(0, 57, 153) # 1148, 1020
    while myRobot.getPixelColor(1148, 1020) == menuColor:
        print("waiting for battle to end")
        myRobot.delay(300)
    print("battle ended")

def bossBattle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    myRobot.delay(2000)
    selectUnit1_AttackAll()
    myRobot.delay(1000)
    selectUnit5_reduceDefence()
    myRobot.delay(1000)

    Utilities.fastClick(1071, 819)
    myRobot.delay(1000)
    Utilities.fastClick(794, 728)
    myRobot.delay(500)
    menuColor = Color(0, 57, 153) # 1148, 1020
    while myRobot.getPixelColor(1148, 1020) == menuColor:
        print("waiting for battle to end")
        myRobot.delay(1000)
    print("battle ended")

def doOneRound():
    bossBattle()
    myRobot.delay(1000)
    bossBattle()
    myRobot.delay(1000)
    bossBattle()
    myRobot.delay(5000)
    menuColor = Color(0, 57, 153) # 1148, 1020
    if myRobot.getPixelColor(1148, 1020) == menuColor:
        bossBattle()
        myRobot.delay(1000)

def handleMissionEnd():
    frontPageColor = Color(219, 33, 33) # 1204, 228
    firstNextStepIsDone = False
    secondNextStepIsDone = False
    EXPisDone = False
    while myRobot.getPixelColor(1204, 228) != frontPageColor:
        Utilities.handleCommunicationError()
        
        # first next step
        firstNextStepColor = Color(0, 39, 113) # (958, 943)
        if (not firstNextStepIsDone) and myRobot.getPixelColor(958, 943) == firstNextStepColor:
            firstNextStepIsDone = True
            myRobot.mouseMove(958, 943)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        # EXP_X color java.awt.Color[r=189,g=204,b=230], (912, 143)
        EXP_X_color = Color(189, 204, 230)
        if (not EXPisDone) and myRobot.getPixelColor(912, 143) == EXP_X_color:
            EXPisDone = True
            myRobot.mouseMove(912, 143)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        # 2nd next step color java.awt.Color[r=254,g=254,b=254] (938,939)
        secondNextStepColor = Color(254, 254, 254)
        if (not secondNextStepIsDone) and myRobot.getPixelColor(938,939) == secondNextStepColor:
            print '2nd next step click'
            secondNextStepIsDone = True
            myRobot.mouseMove(959, 940)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        print '2nd next  = ', secondNextStepIsDone

        # Friend
        noApplyColor = Color(255, 255, 255) # (780, 784)
        if myRobot.getPixelColor(780, 784) == noApplyColor:
            myRobot.mouseMove(780, 784)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # Close Mission
        goingRewardColor = Color(77, 9, 17) #(1053, 666)
        if myRobot.getPixelColor(1053, 666) == goingRewardColor:
            myRobot.mouseMove(810, 673)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # click empty place to speed up
        myRobot.mouseMove(717, 157)
        myRobot.mousePress(InputEvent.BUTTON1_MASK)
        myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # pause for a while        
        myRobot.delay(500)

def enterMission():
    missionColor = Color(107, 6, 9) # (702, 364)
    Utilities.waitForColorAndDo(702, 364, missionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)

    # must buy strength
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=Utilities.buyStrength)
         

    # select follower
    followerColor = Color(143,89,48) # (1015,223)    
    # must select Follower
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
            func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))

    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

def setFollowerFilter():
    missionColor = Color(107, 6, 9) # (702, 364)
    Utilities.waitForColorAndDo(702, 364, missionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 92, 201) # (954, 923)

    # must buy strength
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=Utilities.buyStrength)
    
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
    Utilities.fastClick(776, 619)  # spear
    myRobot.delay(1000)

    # click confirm
    Utilities.fastClick(958, 1008)
    myRobot.delay(1000)

    def clickReturnAndWait():
        Utilities.fastClick(709,221)
        myRobot.delay(1000)
    # click two return
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor, wait_time_period=2000,
            func_while_wait=clickReturnAndWait,
            func_after_wait=clickReturnAndWait)
    myRobot.delay(1000)        
    
def process(numRound):
    Utilities.log('BonusGame.txt', 'Process', 'Start')
    changeToRightTeam()
    Utilities.log('BonusGame.txt', 'Process', 'team changed')
    goToMissionMenu()
    Utilities.log('BonusGame.txt', 'Process', 'arrive missions')
    setFollowerFilter()
    Utilities.log('BonusGame.txt', 'Process', 'filter set')
    starColor=Color(255, 187, 80)  # (1136, 333)
    while numRound > 0:
        enterMission()
        doOneRound()
        Utilities.handleMissionEnd(targetX=1136, targetY=333, waitTargetColor=starColor)
        Utilities.log('BonusGame.txt', 'round completed', 'remaining ' + str(numRound))
        numRound -= 1
    print("process bonus game completed")
    myRobot.delay(2000)
    # return to front page
    worldColor = Color(248, 145, 65) # (944, 808)
    while myRobot.getPixelColor(944, 808) != worldColor:
        Utilities.fastClick(1214, 233)
        myRobot.delay(2000)
    myRobot.delay(2000)
def checkProtectionSettingMenu():
    noColor = Color(205,217,232) # (842, 748)
    if myRobot.getPixelColor(842, 748) == noColor:
        Utilities.fastClick(842,748)
    dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
    getRewardColor = Color(2, 16, 64) # (918, 883)
    if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
        Utilities.fastClick(1223, 149)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 66, 15) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetColor = Color(39, 35, 44)  # (731, 410)
    while myRobot.getPixelColor(731, 410) != targetColor:
        Utilities.fastClick(1254, 408)
        myRobot.delay(2000)
        print("waiting for targetUnitColor")
    myRobot.delay(1000)

    # back to front page
    letterColor = Color(180,113,99) # (1150,175)
    while myRobot.getPixelColor(1150, 175) != letterColor:
        Utilities.fastClick(707, 1013)
        print("waiting for letter color, ", myRobot.getPixelColor(1150, 175))
        myRobot.delay(3000)
    myRobot.delay(1000)

def goToMissionMenu():
    fireHeroColor = Color(33, 8, 19) # 996, 267
    while myRobot.getPixelColor(996, 267) != fireHeroColor:
        Utilities.fastClick(828, 547) # click on vertex
        myRobot.delay(3000)

    missionColor = Color(58, 2, 10) # (840, 378)
    while myRobot.getPixelColor(840, 378) != missionColor:
        Utilities.fastClick(996, 267) # click on fireHeroColor
        myRobot.delay(2000)
    myRobot.delay(1000)
    

if __name__ == "__main__":
    #checkProtectionSettingMenu()
    process(3)
    
 
