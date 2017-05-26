import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)
myRobot = JRobot()


def selectUnit1_AttackAll():
    Utilities.openMagicMenu(1)
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(1027, 928)
    myRobot.delay(800)

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

def selectUnit3_weaken():
    Utilities.openMagicMenu(3)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.fastClick(1061, 723)
    myRobot.delay(800)

def battle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    myRobot.delay(2000)
    selectUnit1_AttackAll()
    myRobot.delay(500)
    selectUnit3_randomAttack()

    Utilities.fastClick(794, 728)
    myRobot.delay(1000)
    Utilities.fastClick(792, 941)
    menuColor = Color(0, 56, 149) # 1148, 1020
    while myRobot.getPixelColor(1148, 1020) == menuColor:
        print("waiting for battle to end")
        myRobot.delay(300)
    print("battle ended")

def bossBattle():
    while not Utilities.isWaitingForCommand():
        myRobot.delay(1000)
    myRobot.delay(2000)
    selectUnit3_weaken()
    myRobot.delay(500)
    selectUnit1_rose()

    Utilities.fastClick(792, 941)
    myRobot.delay(900)
    Utilities.fastClick(794, 728)
    myRobot.delay(500)
    Utilities.fastClick(721, 1034) # click auto
    myRobot.delay(500)
    Utilities.fastClick(721, 1034) # click auto


    menuColor = Color(0, 56, 149) # 1148, 1020
    while myRobot.getPixelColor(1148, 1020) == menuColor:
        print("waiting for battle to end")
        if Utilities.isWaitingForCommand():
            selectUnit1_rose()
            myRobot.delay(500)
            selectUnit3_randomAttack()
            myRobot.delay(500)
            # launch
            Utilities.fastClick(792, 941)
            myRobot.delay(500)
            Utilities.fastClick(794, 728)
            myRobot.delay(500)
            Utilities.fastClick(721, 1034) # click auto
            myRobot.delay(500)
            Utilities.fastClick(721, 1034) # click auto
        myRobot.delay(300)
    print("battle ended")

def doOneRound():
    battle()
    myRobot.delay(1000)
    battle()
    myRobot.delay(1000)
    battle()
    myRobot.delay(1000)
    bossBattle()
    myRobot.delay(1000)
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
    missionColor = Color(107, 5, 8) # (702, 364)
    Utilities.waitForColorAndDo(702, 364, missionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 83, 196) # (954, 923)

    # must buy strength
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=Utilities.buyStrength)
         

    # select follower
    followerColor = Color(145,60,32) # (1015,223)    
    # must select Follower
    Utilities.waitForColorAndDo(1015, 223, followerColor, 
            func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))

    launchColor = Color(0, 43, 68)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

def setFollowerFilter():
    missionColor = Color(107, 5, 8) # (702, 364)
    Utilities.waitForColorAndDo(702, 364, missionColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 83, 196) # (954, 923)

    # must buy strength
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=Utilities.buyStrength)
    
    # click filter
    followerColor = Color(145,60,32) # (1015,223)    
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
    Utilities.fastClick(999, 550)  # wand
    myRobot.delay(1000)

    # click confirm
    Utilities.fastClick(958, 1008)
    myRobot.delay(1000)

    def clickReturnAndWait():
        Utilities.fastClick(709,221)
        myRobot.delay(1000)
    # click two return
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor, 
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
    while numRound > 0:
        enterMission()
        doOneRound()
        handleMissionEnd()
        Utilities.log('BonusGame.txt', 'round completed', 'remaining ' + str(numRound))
        numRound -= 1
    print("process bonus game completed")
    myRobot.delay(2000)
    # return to front page
    worldColor = Color(244, 137, 60) # (944, 808)
    while myRobot.getPixelColor(944, 808) != worldColor:
        Utilities.fastClick(1214, 233)
        myRobot.delay(2000)
    myRobot.delay(2000)
def checkProtectionSettingMenu():
    noColor = Color(227, 234, 243) # (842, 748)
    if myRobot.getPixelColor(842, 748) == noColor:
        Utilities.fastClick(842,748)
    dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
    getRewardColor = Color(2, 16, 64) # (918, 883)
    if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
        Utilities.fastClick(1223, 149)

def changeToRightTeam():
    # select team
    strengthenColor = Color(246, 72, 16) # 701,851
    while myRobot.getPixelColor(701,851) != strengthenColor:
        Utilities.fastClick(808, 1021)
        checkProtectionSettingMenu()
        myRobot.delay(2000)
    myRobot.delay(1000)

    firionColor = Color(154, 98, 0)  # (732, 401)
    while myRobot.getPixelColor(732,401) != firionColor:
        Utilities.fastClick(1254, 408)
        myRobot.delay(2000)
        print("waiting for firionColor")
    myRobot.delay(1000)

    # back to front page
    letterColor = Color(184,123,108) # (1150,175)
    while myRobot.getPixelColor(1150, 175) != letterColor:
        Utilities.fastClick(707, 1013)
        print("waiting for letter color, ", myRobot.getPixelColor(1150, 175))
        myRobot.delay(3000)
    myRobot.delay(1000)

def goToMissionMenu():
    dicaColor = Color(18,186,5) # 853,271
    while myRobot.getPixelColor(853,271) != dicaColor:
        Utilities.fastClick(828, 547) # click on vertex
        myRobot.delay(3000)

    missionColor = Color(107, 5, 8) # (702, 364)
    while myRobot.getPixelColor(702,364) != missionColor:
        Utilities.fastClick(853,271) # click on dica
        myRobot.delay(2000)
    myRobot.delay(1000)
    

if __name__ == "__main__":
    process(3)
    #changeToRightTeam()
 
