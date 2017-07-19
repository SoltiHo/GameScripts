import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import BonusGame
import FightClub
import CoFight
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

resetCycleInMin = 600
doFightClub = True
doCoFight = False
doBonusGame = False
numBonusGame = 1

def isStillRunning():
    FFBEColor = Color(190, 180, 180) # (1171, 234)
    if myRobot.getPixelColor(1171, 234) == FFBEColor:
        return False
    return True

def recover():
    Utilities.log('LBDroidXLog.txt', 'recover', 'recover')
    print "recover"
    #myRobot.delay(10000)
    # first, go back to FFBE
    Utilities.fastClick(1171, 234)
    myRobot.delay(5000)
    # wait for combat screen
    combatBackgroundColor = Color(185, 69, 48) # (1126, 161)
    playMissionYesColor = Color(255, 255, 255) # (1087, 626)
    while myRobot.getPixelColor(1126, 161) != combatBackgroundColor:
        Utilities.fastClick(983, 827)
        if myRobot.getPixelColor(1087, 626) == playMissionYesColor:
            Utilities.fastClick(1087, 626)
        print "waiting for combat background"
        
        myRobot.delay(3000)

    # pause speedup
    myRobot.delay(1000)
    Utilities.fastClick(1247, 163)
    myRobot.delay(1000)
    Utilities.fastClick(1247, 163)
    myRobot.delay(1000)

    # restart speedup
    Utilities.fastClick(1247, 163)
    myRobot.delay(1500)
    Utilities.fastClick(996, 82)
    myRobot.delay(2000)

    # click Auto
    Utilities.fastClick(768, 1036)
    Utilities.log('LBDroidXLog.txt', 'recover', 'recover completed')
    
def launchDroidXToDesktop():
    Utilities.log('LBDroidXLog.txt', 'launch', 'launchDroidXToDesktop')
    myRobot.delay(3000)
    droidXColor = Color(234, 132, 132) # (414, 1060)
    while myRobot.getPixelColor(414, 1060) != droidXColor:
        print "waiting for droidXColor"
        myRobot.delay(1000)
    Utilities.fastClick(414,1060)
    myRobot.delay(7000)

    # click ignore
    type(Key.F4, KeyModifier.ALT)
    myRobot.delay(60000)

    # maximize window
    type(' ', KeyModifier.ALT)
    myRobot.delay(3000)
    type('x')
    myRobot.delay(10000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'droidX maximized')

def loadAutoKey():
    # open key auto
    autoKeyColor = Color(0, 119, 217) # (811, 340)
    Utilities.waitForColorAndDo(811, 340, autoKeyColor, wait_time_period=6000)    
    noCategoryColor = Color(59, 131, 225) # (754, 327)
    Utilities.waitForColorAndDo(754, 327, noCategoryColor, wait_time_period=4000)
    myScriptColor = Color(59, 131, 225) # (776, 210)
    Utilities.waitForColorAndDo(776, 210, myScriptColor, wait_time_period=2000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'autokey loaded')

def launchFFBEToDesktop():
    # launch FFBE
    FFBEColor = Color(190, 180, 180) # (1171, 234)
    Utilities.waitForColorAndDo(1171, 234, FFBEColor, wait_time_period=3000)
    desktopFriendColor = Color(108, 37, 76) # (1218, 1043)
    while myRobot.getPixelColor(1218, 1043) != desktopFriendColor:
        Utilities.fastClick(1037, 653)
        myRobot.delay(7000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'saw desktop friend color')

def changeToRightTeam():
    # select team
    strengthenColor = Color(136, 30, 7) # 753, 857
    while myRobot.getPixelColor(753, 857) != strengthenColor:
        Utilities.fastClick(842, 1023)
        myRobot.delay(2000)
    myRobot.delay(1000)

    targetUnitColor = Color(240, 227, 212)  # (871, 413)
    while myRobot.getPixelColor(871, 413) != targetUnitColor:
        Utilities.fastClick(1268, 423)
        myRobot.delay(2000)
        print("waiting for targetUnitColor")
    myRobot.delay(1000)

    # back to front page
    letterColor = Color(217, 186, 180) # (1164, 203)
    while myRobot.getPixelColor(1164, 203) != letterColor:
        Utilities.fastClick(757, 1013)
        print("waiting for letter color, ", myRobot.getPixelColor(1164, 203))
        myRobot.delay(3000)
    myRobot.delay(1000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'change to the right team')

def gotoMonsterMountain():
    # wait for "World"
    worldColor = Color(107, 43, 8) # (944, 808)
    Utilities.waitForColorAndDo(944, 808, worldColor)
    myRobot.delay(2000)
    print("world seen")

    # 1st level map, choose 1st island group
    myRobot.delay(3000)
    mouseMove(Location(1189, 406))
    mouseDown(Button.LEFT)
    mouseMove(-200, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    mouseMove(Location(1189, 406))
    mouseDown(Button.LEFT)
    mouseMove(-200, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    firstIslandGroup = "firstIslandGroup.png"
    firstGroupRegion = Region(941,314,262,239)
    firstGroupRegion.click(firstIslandGroup)
    myRobot.delay(5000)
    print("1st island done")

    # 2nd level map, choose 1st island
    firstIslandColor = Color(139, 142, 119)  # (1061, 462)
    Utilities.waitForColorAndDo(1061, 462, firstIslandColor)
    myRobot.delay(2000)
    print("2nd island done")

    # pull right to show earth temple
    mouseMove(Location(1189, 406))
    mouseDown(Button.LEFT)
    mouseMove(-200, 100)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)    
    print("monster mountain shown")

    # find mountain and click it
    mountainRegion = Region(1021,290,220,175)
    mountainRegion.click("1496845013654.png")
    myRobot.delay(2000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'arrived the mountain')
    

def selectNoFollower():
    myRobot.delay(2000)
    #Location(1256, 291)Location(1256, 1063)
    myRobot.mouseMove(1274, 310)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(300)
    myRobot.mouseMove(1272, 663)
    myRobot.delay(300)
    myRobot.mouseMove(1272, 1063)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(900)
    myRobot.mouseMove(1017, 1004)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(2000)

def enterMission():
    missionColor = Color(254, 249, 245) # (752,538)
    Utilities.waitForColorAndDo(752, 538, missionColor)

    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(103, 164, 236) # (954, 923)
    Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)
         
    # select follower
    followerColor = Color(0, 9, 50) # (1182,257)
    Utilities.waitForColorAndDo(1182, 257, followerColor, 
        func_after_wait=selectNoFollower)

    launchColor = Color(0, 55, 90)  # (913,951)
    Utilities.waitForColorAndDo(913, 951, launchColor)

    # wait for skip
    skipColor = Color(0, 25, 113) # (799, 133)
    Utilities.waitForColorAndDo(799, 133, skipColor, wait_time_period=2000)
    # wait for battle start, wait for menu color
    menuColor = Color(0, 17, 52) # (1231, 1048)
    while myRobot.getPixelColor(1231,1048) != menuColor:
        print('waiting for menu color')
        myRobot.delay(2000)
    myRobot.delay(2000)
    Utilities.log('LBDroidXLog.txt', 'launch', 'entered the mission')

def kickoff():
    # enable autokey
    Utilities.fastClick(996, 75)
    myRobot.delay(3000)
    # click auto
    Utilities.fastClick(768, 1046)
    myRobot.delay(3000)

def setupAttackCmd():
    Utilities.openMagicMenu(2)
    myRobot.delay(2000)
    scrollMenuDown_fast()
    myRobot.delay(2000)
    Utilities.fastClick(782, 818)
    myRobot.delay(2000)
    # click AUTO
    Utilities.fastClick(768, 1033)
    myRobot.delay(1000)
    Utilities.fastClick(768, 1033)
    myRobot.delay(3000)

def setupAttackIfWaiting():
    swordColor = Color(147, 138, 124) # (718,674)
    if myRobot.getPixelColor(718,674) == swordColor:
        setupAttackCmd()
    myRobot.delay(3000)

def stopAndFinishTheFight():
    # first stop autokey
    Utilities.fastClick(1261, 167)
    myRobot.delay(1000)
    Utilities.fastClick(1261, 167)
    myRobot.delay(3000)
    # then, stop AUTO
    Utilities.fastClick(768, 1033)
    swordColor = Color(147, 138, 124) # (718,674)
    Utilities.waitForColor(718,674, swordColor, 'waiting for sword')
    myRobot.delay(3000)
    # fight till end
    resultRColor = Color(170, 182, 185) # (915, 346)
    Utilities.waitForColorAndDo(915, 346, resultRColor, wait_time_period=2000,
            func_while_wait=setupAttackIfWaiting) 
    # wait for skip
    skipColor = Color(0, 25, 113) # (799, 133)
    Utilities.waitForColorAndDo(799, 133, skipColor, wait_time_period=2000)

def handleMissionEnd():
    # 1st next step
    firstNextStepColor = Color(0, 14, 66) # (956, 956)
    Utilities.waitForColorAndDo(956, 956, firstNextStepColor, 
            func_while_wait=Utilities.fastClick, arg_while_wait=(844, 572))
    # unit results and 2nd next step
    #starColor = Color(255, 102, 204) # (764, 784)
    #Utilities.waitForColorAndDo(764, 784, starColor, 
    #        func_while_wait=Utilities.fastClick, arg_while_wait=(1063, 435),
    #        func_after_wait=Utilities.fastClick, arg_after_wait=(986, 940))
    # 3rd nexst step, items
    homePageColor = Color(85, 7, 7) # (1220, 241)
    rewardCloseColor = Color(0, 12, 48) # (863, 676) 
    while myRobot.getPixelColor(1220, 241) != homePageColor:
        Utilities.fastClick(993, 945)
        if myRobot.getPixelColor(863, 676) == rewardCloseColor:
            Utilities.fastClick(863, 676)
            myRobot.delay(2000)
        myRobot.delay(3000)


    

    
def scrollMenuDown_fast():
    myRobot.mouseMove(935, 965)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    #myRobot.delay(100)
    myRobot.mouseMove(935, 945)
    myRobot.delay(100)
    myRobot.mouseMove(935, 895)
    myRobot.delay(100)
    myRobot.mouseMove(935, 845)
    myRobot.delay(100)
    myRobot.mouseMove(935, 795)
    myRobot.delay(150)
    myRobot.mouseMove(935, 745)
    myRobot.delay(100)
    myRobot.mouseMove(935, 660)
    myRobot.delay(100)
    myRobot.mouseMove(935, 661)
    myRobot.delay(300)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)    
    myRobot.delay(1000)

def closeDroidX():
    myRobot.delay(3000)
    closeRegion = Region(1850,0,70,79)
    closeIcon = "closeIcon.png"
    closeRegion.click(closeIcon)
    myRobot.delay(3000)

def main():
    global resetCycleInMin
    minCount = 0
    while minCount < resetCycleInMin:
        if not isStillRunning():
            recover()
        myRobot.delay(60000)
        minCount = minCount + 1

def launchLBMissionFromDesktop():
    launchDroidXToDesktop()
    Utilities.log('LBDroidXLog.txt', 'launch', 'arrived Desktop')
    myRobot.delay(5000)
    loadAutoKey()
    Utilities.log('LBDroidXLog.txt', 'launch', 'autokey launched')
    myRobot.delay(5000)
    launchFFBEToDesktop()
    Utilities.log('LBDroidXLog.txt', 'launch', 'DroidX FFBE desktop seen')
    myRobot.delay(5000)
    changeToRightTeam()
    Utilities.log('LBDroidXLog.txt', 'launch', 'at a right team')
    myRobot.delay(2000)
    gotoMonsterMountain()
    Utilities.log('LBDroidXLog.txt', 'launch', 'at the mountain')
    myRobot.delay(2000)
    enterMission()
    Utilities.log('LBDroidXLog.txt', 'launch', 'in the mission')
    myRobot.delay(2000)
    kickoff()
    Utilities.log('LBDroidXLog.txt', 'launch', 'start training')
    myRobot.delay(2000)

def terminateAndCloseMission():
    stopAndFinishTheFight()
    myRobot.delay(5000)
    handleMissionEnd()
    myRobot.delay(5000)
    closeDroidX()
    myRobot.delay(5000)

def process(minToReset=180):
    global resetCycleInMin
    resetCycleInMin = minToReset
    launchLBMissionFromDesktop()
    myRobot.delay(3000)
    main()
    myRobot.delay(5000)
    terminateAndCloseMission()
    myRobot.delay(5000)

if __name__ == "__main__":
    while True:
        process(resetCycleInMin)
        Utilities.log('LBDroidXLog.txt', 'reset', 'LB training completed')
        myRobot.delay(60000)
        Utilities.launchBS()
        myRobot.delay(1000)
        Utilities.enterBSFFBE()
        myRobot.delay(1000)
        Utilities.waitForBSFFBEDesktop()
        myRobot.delay(3000)
        Utilities.log('LBDroidXLog.txt', 'reset', 'BS FFBE')
        if doBonusGame:
            Utilities.log('LBDroidXLog.txt', 'reset', 'do bonus game')
            BonusGame.process(numBonusGame)
            Utilities.log('LBDroidXLog.txt', 'reset', 'bonus game completed')
            myRobot.delay(2000)
        if doCoFight:
            Utilities.log('LBDroidXLog.txt', 'reset', 'do co-fight')
            CoFight.process()
            Utilities.log('LBDroidXLog.txt', 'reset', 'co-fight completed')
            myRobot.delay(2000)
        if doFightClub:
            Utilities.log('LBDroidXLog.txt', 'reset', 'do fight club')
            FightClub.process()
            Utilities.log('LBDroidXLog.txt', 'reset', 'fight club completed')
            myRobot.delay(2000)
        Utilities.log('LBDroidXLog.txt', 'reset', 'restart BS and the mission')
        Utilities.closeBS()
        Utilities.log('LBDroidXLog.txt', 'reset', 'restart the mission completed')
        myRobot.delay(60000)
    #scrollMenuDown_fast()
    #myRobot.delay(10000)
    #selectNoFollower()
    #launchLBMissionFromDesktop()
    #terminateAndCloseMission()
    #closeDroidX()
    #handleMissionEnd()
    #launchDroidXToDesktop()
    #main()
    #recover()
    