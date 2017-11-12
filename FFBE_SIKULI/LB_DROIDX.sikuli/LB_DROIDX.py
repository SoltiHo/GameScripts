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

resetCycleInMin = 120
doFightClub = True
doCoFight = True
doBonusGame = False
numBonusGame = 1

class LBTrainner:
    resetCycleInMin = 120
    targetTeamX = 0
    targetTeamY = 0
    targetTeamColor = Color(0, 0, 0)
    FFBEIcon = "FFBEIcon.png"
    FFBEIconRegion = Region(762,160,469,265)
    IgnoreUpdate = "IgnoreUpdate.png"
    IgnoreUpdateRegion = Region(847,611,108,42)
    # ------------------------------------------------------------ #
    def run(self):
        self.launch()
        self.gotoTrainingMission()
        self.enterMission()
        self.preTrainingPrep()
        self.startTraining()
        self.monitorTraining()
        self.stopTraining()
        self.postTraining()

    def getCombatBackgroundInfo(self):
        print('implement getCombatBackgroundInfo()')
        exit(1)

    def gotoTrainingMission(self):
        print('implement gotoTrainingMission()')
        exit(1)
        
    def enterMission(self):
        print('implement enterMissioniningMission()')
        exit(1)

    def preTrainingPrep(self):
        print('implement preTrainingPrep()')
        exit(1)

    def postTraining(self):
        print('implement postTraining()')
        exit(1)
                
    def startTraining(self):
        # enable autokey
        Utilities.fastClick(996, 75)
        myRobot.delay(3000)
        # click auto
        Utilities.fastClick(768, 1046)
        myRobot.delay(3000)

    def monitorTraining(self):
        minCount = 0
        while minCount < self.resetCycleInMin:
            if not self.isStillRunning():
                self.recover()
            myRobot.delay(60000)
            minCount = minCount + 1

    def stopTraining(self):
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

    def closeDroidX(self):
        FFBEColor = Color(213, 177, 169) # (1171, 234)
        while myRobot.getPixelColor(1171, 234) != FFBEColor:
            Utilities.fastClick(1899, 20)
            myRobot.delay(10000)
            
    def isStillRunning(self):
        FFBEColor = Color(213, 177, 169) # (1171, 234)
        if myRobot.getPixelColor(1171, 234) == FFBEColor:
            return False
        return True
       
    def recover(self):
        Utilities.log('LBDroidXLog.txt', 'recover', 'recover')
        # first, go back to FFBE
        Utilities.fastClick(1171, 234)
        myRobot.delay(5000)
        # wait for combat screen
        
        playMissionYesColor = Color(255, 255, 255) # (1087, 626)
        combatBackgroundX, combatBackgroundY, combatBackgroundColor = self.getCombatBackgroundInfo()
        while myRobot.getPixelColor(combatBackgroundX, combatBackgroundY) != combatBackgroundColor:
            Utilities.fastClick(1054, 911)
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
        
        # check if hanging
        AutoColor = Color(0, 46, 63) # (774,1042)
        checkCount = 0
        isHanging = False
        while True:
            if myRobot.getPixelColor(774,1042) == AutoColor:
                checkCount += 1
            else:
                break
            myRobot.delay(500)
            if checkCount == 10:
                # it's hanging!!!! :(
                isHanging = True
                break
            
        if isHanging:
            # close this DroidX
            self.closeDroidX()
            
        return isHanging

    def launch(self):
        self.launchDroidX()
        myRobot.delay(30000)
        self.loadAutoKey()
        myRobot.delay(3000)
        self.launchFFBEToDesktop()
        myRobot.delay(5000)
        self.changeToRightTeam()
        myRobot.delay(3000)
        
    def launchDroidX(self):
        Utilities.log('DroidXNewLog.txt', 'launch', 'launching DroidX')
        myRobot.delay(3000)
        droidXColor = Color(234, 132, 132) # (414, 1060)
        while myRobot.getPixelColor(414, 1060) != droidXColor:
            print "waiting for droidXColor"
            myRobot.delay(1000)
        Utilities.fastClick(414,1060)
        myRobot.delay(7000)
    
        # click ignore
        while self.IgnoreUpdateRegion.exists(Pattern(self.IgnoreUpdate).similar(0.9)) is None:
            myRobot.delay(1000)
            print('waiting for Ignore Update')
        self.IgnoreUpdateRegion.click(Pattern(self.IgnoreUpdate).similar(0.9))
        Utilities.log('DroidXNewLog.txt', 'launch', 'update ignored')
        
        # wait for Game Icon
        while self.FFBEIconRegion.exists(Pattern(self.FFBEIcon)) is None:
            myRobot.delay(1000)
            print('waiting for FFBE Icon')

        # wait for 30 sec more
        myRobot.delay(30000)
            
        # maximize window
        type(' ', KeyModifier.ALT)
        myRobot.delay(3000)
        type('x')
        myRobot.delay(10000)
        Utilities.log('DroidXNewLog.txt', 'launch', 'droidX maximized')
        Utilities.log('DroidXNewLog.txt', 'launch', 'DroidX launch completed')
        
    def loadAutoKey(self):
        # open key auto
        Utilities.log('DroidXNewLog.txt', 'launch', 'loading autokey')
        autoKeyColor = Color(0, 119, 217) # (811, 340)
        Utilities.waitForColorAndDo(811, 340, autoKeyColor, wait_time_period=6000)    
        
        noCategoryColor = Color(59, 131, 225) # (754, 327)
        ignoreUpdateColor = Color(68, 68, 68) # (859, 1018)
        while myRobot.getPixelColor(754, 327) != noCategoryColor:
            if myRobot.getPixelColor(859, 1018) == ignoreUpdateColor:
                Utilities.fastClick(859, 1018)
            myRobot.delay(3000)
            
        myScriptColor = Color(59, 131, 225) # (776, 210)
        Utilities.waitForColorAndDo(776, 210, myScriptColor, wait_time_period=3000,
                func_while_wait=Utilities.fastClick, arg_while_wait=(754, 327))
        Utilities.log('DroidXNewLog.txt', 'launch', 'autokey loaded')

    def launchFFBEToDesktop(self):
        Utilities.log('DroidXNewLog.txt', 'launch', 'launching FFBE in DroidX')
        # launch FFBE
        while self.FFBEIconRegion.exists(Pattern(self.FFBEIcon)) is None:
            myRobot.delay(1000)
            print('waiting for FFBE Icon')
        self.FFBEIconRegion.click(Pattern(self.FFBEIcon))
        desktopFriendColor = Color(108, 37, 76) # (1218, 1043)
        while myRobot.getPixelColor(1218, 1043) != desktopFriendColor:
            Utilities.fastClick(1037, 653)
            myRobot.delay(7000)
        Utilities.log('DroidXNewLog.txt', 'launch', 'saw desktop friend color')
        Utilities.log('DroidXNewLog.txt', 'launch', 'launching FFBE in DroidX completed')

    def changeToRightTeam(self):
        Utilities.log('DroidXNewLog.txt', 'launch', 'changing to the right team')
        # select team
        strengthenColor = Color(136, 30, 7) # 753, 857
        while myRobot.getPixelColor(753, 857) != strengthenColor:
            Utilities.fastClick(842, 1023)
            myRobot.delay(2000)
        myRobot.delay(1000)
    
        targetUnitColor = Color(11, 57, 37)  # (1023,397)
        while myRobot.getPixelColor(self.targetTeamX, self.targetTeamY) != self.targetTeamColor:
            Utilities.fastClick(1268, 423)
            myRobot.delay(2000)
            print("waiting for targetUnitColor")
        myRobot.delay(1000)
    
        # back to front page
        #letterColor = Color(217, 186, 180) # (1164, 203)
        letterColor = Color(134, 93, 91) # (1164, 203) Halloween
        while myRobot.getPixelColor(1164, 203) != letterColor:
            Utilities.fastClick(757, 1013)
            print("waiting for letter color, ", myRobot.getPixelColor(1164, 203))
            myRobot.delay(3000)
        myRobot.delay(1000)
        Utilities.log('DroidXNewLog.txt', 'launch', 'now at the right team')

    def waitForFrontPage(self):
        FriendsColor = Color(250, 92, 191)  # (1217,1024)
        Utilities.waitForColor(1217,1024,FriendsColor,"waiting for front page friends")



class FireLB(LBTrainner):
    targetTeamX = 1023
    targetTeamY = 397
    targetTeamColor = Color(11, 57, 37)
    combatBackgroundX = 1126
    combatBackgroundY = 161
    combatBackgroundColor = Color(185, 69, 48) 
    # ------------------------------------------------------------ #
    def gotoTrainingMission(self):
        worldColor = Color(160, 155, 125) # (944,808)
        Utilities.waitForColorAndDo(944,808, worldColor)
        myRobot.delay(2000)
        # find 1st island group
        islandRegion = Region(822,290,459,342)
        island = "island.png"
        while islandRegion.exists(Pattern(island).similar(0.9)) is None:
            # scroll left down
            mouseMove(Location(1093, 690))
            mouseDown(Button.LEFT)
            mouseMove(-400, 200)
            mouseUp(Button.LEFT)
            myRobot.delay(2000)
        islandRegion.click(Pattern(island).similar(0.9))
        myRobot.delay(2000)
        
    def preTrainingPrep(self):
        print("no preTrainingPrep needed for fireLB")
        
        # go to the 1st island
        firstIslandColor = Color(112, 151, 81) # (1130,469)
        Utilities.waitForColorAndDo(1130,469, firstIslandColor)
        myRobot.delay(2000)

        # go to moutain
        mountainRegion = Region(825,281,456,183)
        mountain = "mountain.png"
        while mountainRegion.exists(Pattern(mountain).similar(0.9)) is None:
            # scroll left down
            mouseMove(Location(1093, 690))
            mouseDown(Button.LEFT)
            mouseMove(-400, 200)
            mouseUp(Button.LEFT)
            myRobot.delay(2000)
        mountainRegion.click(Pattern(mountain).similar(0.9))
        myRobot.delay(2000)

    def getCombatBackgroundInfo(self):
        return self.combatBackgroundX, self.combatBackgroundY, self.combatBackgroundColor

    def enterMission(self):
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

    def postTraining(self):
        

        
                    
    







    
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

    targetUnitColor = Color(11, 57, 37)  # (1023,397)
    while myRobot.getPixelColor(1023,397) != targetUnitColor:
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
    mouseMove(-400, 200)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    mouseMove(Location(1189, 406))
    mouseDown(Button.LEFT)
    mouseMove(-400, 200)
    mouseUp(Button.LEFT)
    myRobot.delay(2000)
    firstIslandGroup = "firstIslandGroup.png"
    firstGroupRegion = Region(753,242,456,372)
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




    

def setupAttackCmd():
    Utilities.openMagicMenu(3)
    myRobot.delay(2000)
    #scrollMenuDown_fast()
    #myRobot.delay(2000)
    Utilities.fastClick(1059, 804)
    myRobot.delay(2000)
    # click AUTO
    Utilities.fastClick(768, 1033)
    myRobot.delay(2000)
    Utilities.fastClick(768, 1033)
    myRobot.delay(1000)

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
    def clickAndCheckCommError():
        commErrorColor = Color(3, 47, 97) # (966, 639)
        if myRobot.getPixelColor(966, 639) == commErrorColor:
            Utilities.fastClick(966, 639)
        Utilities.fastClick(844, 572)
    firstNextStepColor = Color(0, 14, 66) # (956, 956)
    Utilities.waitForColorAndDo(956, 956, firstNextStepColor, 
            func_while_wait=clickAndCheckCommError, arg_while_wait=())
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
            while recover():
                print("recovering")
        myRobot.delay(60000)
        minCount = minCount + 1

def launchLBMissionFromDesktop():
    launchDroidXToDesktop()
    Utilities.log('LBDroidXLog.txt', 'launch', 'arrived Desktop')
    myRobot.delay(30000)
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
    DroidXBackgroundColor = Color(240, 240, 240) # (378, 863)
    if myRobot.getPixelColor(378, 863) != DroidXBackgroundColor:
        resetCycleInMin = minToReset
        launchLBMissionFromDesktop()
        myRobot.delay(3000)
    main()
    myRobot.delay(5000)
    terminateAndCloseMission()
    myRobot.delay(5000)

def old_main():
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
            CoFight.CoFightRunner.process()
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


if __name__ == "__main__":
    trainer = FireLB()
    trainer.monitorTraining()