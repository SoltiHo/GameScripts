import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

class BonusGame:
    # Global Data --------------------------
    targetTeamColor = {'color': Color(248, 156, 230), 'x': 723, 'y': 411}
    targetGameBanner = {'image': "1508002119056.png", 'region': Region(955,248,179,803)}
    targetMissionColor = {'color': Color(107, 6, 9), 'x': 702, 'y': 364}
    sList = [5, 6]
    eqList = [25]
    genList = [15]
    # --------------------------------------
    @staticmethod
    def isBoss():
        bossColor = Color(45,45,53) # (872,498)
        return myRobot.getPixelColor(872,498) == bossColor

    @staticmethod
    def isHard():
        footColor = Color(87, 92, 104) # (732,540)
        return myRobot.getPixelColor(732,540) == footColor

    @staticmethod
    def selectUnit1_MagicAndDraw():
        clickList = [
                {'move': 2, 'pos':(1067, 718)},
                {'move': -2, 'pos':(1064, 820)},
                {'move': 0, 'pos':(831, 821)}
                ]
        Utilities.setCommand(1, clickList)

    @staticmethod
    def selectUnit1_DoubleThunder():
        clickList = [
                {'move': 2, 'pos':(1067, 718)},
                {'move': -2, 'pos':(1064, 820)},
                {'move': 0, 'pos':(1064, 820)}
                ]
        Utilities.setCommand(1, clickList)

    @staticmethod
    def selectUnit1_DoubleUltima():
        clickList = [
                {'move': 2, 'pos':(1067, 718)},
                {'move': -1, 'pos':(1064, 840)},
                {'move': 0, 'pos':(1064, 840)}
                ]
        Utilities.setCommand(1, clickList)

    @staticmethod
    def selectUnit2_Destroy():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        destroyImage = "destroyImage.png"
        Utilities.findSkill(destroyImage)
        myRobot.delay(1000)

    @staticmethod
    def selectUnit3_Bomb():
        Utilities.openMagicMenu(3)
        myRobot.delay(1000)
        bombImage = "bombImage.png"
        Utilities.findSkill(bombImage)
        myRobot.delay(1000)

    @staticmethod
    def selectUnit4_Storm():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        stormImage = "stormImage.png"
        Utilities.findSkill(stormImage)
        myRobot.delay(1000)

    @staticmethod
    def battleNormal():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        # click Repeat
        Utilities.fastClick(867, 1037)
        myRobot.delay(2000)
        # wait for ending
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for normal battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("normal battle ended")

    @staticmethod
    def battleFirstOne():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_MagicAndDraw()
        myRobot.delay(1000)
        Utilities.defense(2)
        myRobot.delay(1000)
        Utilities.defense(3)
        myRobot.delay(1000)
        Utilities.defense(4)
        myRobot.delay(1000)
        Utilities.defense(5)
        myRobot.delay(1000)
        Utilities.defense(6)
        myRobot.delay(1000)
    
        # launch
        Utilities.fastClick(745, 1032)  # click AUTO
        myRobot.delay(500)
        Utilities.fastClick(745, 1032)  # click AUTO
        myRobot.delay(500)

        # wait for ending
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for first battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("first battle ended")

    @staticmethod
    def battleHard():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_DoubleThunder()
        myRobot.delay(1000)
    
        # launch
        Utilities.launch(1)
        myRobot.delay(500)
        # click Repeat
        Utilities.fastClick(867, 1037)
        myRobot.delay(2000)

        # wait for ending
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for first battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("first battle ended")


    @staticmethod
    def battleBoss():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_DoubleUltima()
        myRobot.delay(1000)
        BonusGame.selectUnit2_Destroy()
        myRobot.delay(1000)
        BonusGame.selectUnit3_Bomb()
        myRobot.delay(1000)
        BonusGame.selectUnit4_Storm()
        myRobot.delay(1000)
    
        # launch
        Utilities.launch(2)
        Utilities.launch(3)
        Utilities.launch(4)
        myRobot.delay(2000)
           
        #Utilities.fastClick(1090, 934) # unit 6
        Utilities.fastClick(734, 1043) # Auto
        myRobot.delay(1000)
        Utilities.fastClick(734, 1043) # Auto
    
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("boss battle ended")

    
    @staticmethod
    def doOneRound():
        #expBarColor = Color(92, 183, 90) # (1060,656)
        battleEndTopBannerColor = Color(155, 149, 54) # (1031,214)
        battleCount = 0
        #while myRobot.getPixelColor(1060, 656) != expBarColor:
        while myRobot.getPixelColor(1031,214) != battleEndTopBannerColor:
            if Utilities.isWaitingForCommand():
                battleCount += 1
                if battleCount == 1:
                    BonusGame.battleFirstOne()
                elif BonusGame.isHard():
                    BonusGame.battleHard()
                elif BonusGame.isBoss():
                    BonusGame.battleBoss()
                else:
                    BonusGame.battleNormal()
            Utilities.fastClick(1079, 485)
            Utilities.handleCommunicationError()
            myRobot.delay(2000)
        Utilities.log('BonusGame.txt', 'round completed', str(battleCount) + ' battles')
    
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

    @staticmethod
    def enterMission():
        Utilities.waitForColorAndDo(
                BonusGame.targetMissionColor['x'], BonusGame.targetMissionColor['y'], 
                BonusGame.targetMissionColor['color'], 
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
    
        # wait for MENU in battle
        menuColor = Color(0, 50, 130) # (1148, 1022)
        #Utilities.waitForColor(1148, 1022, menuColor, wait_time_period=1000, wait_msg='waiting for battle entry')
        while myRobot.getPixelColor(1148, 1022) != menuColor:
            Utilities.handleCommunicationError()
            myRobot.delay(1000)

    @staticmethod
    def process(numRound):
        Utilities.log('BonusGame.txt', 'Process', 'Start')
        Utilities.changeToRightTeam(
                BonusGame.targetTeamColor['x'],
                BonusGame.targetTeamColor['y'],
                BonusGame.targetTeamColor['color'])
        Utilities.log('BonusGame.txt', 'Process', 'team changed')
        BonusGame.goToMissionMenu()
        Utilities.log('BonusGame.txt', 'Process', 'arrive missions')
        Utilities.setFollowerFilter(
                BonusGame.targetMissionColor['x'],
                BonusGame.targetMissionColor['y'],
                BonusGame.targetMissionColor['color'],
                BonusGame.sList,
                BonusGame.eqList,
                BonusGame.genList)
        Utilities.log('BonusGame.txt', 'Process', 'filter set')
        starColor=Color(255, 187, 80)  # (1136, 333)
        while numRound > 0:
            BonusGame.enterMission()
            BonusGame.doOneRound()
            Utilities.handleMissionEnd(
                    targetX=BonusGame.targetMissionColor['x'],
                    targetY=BonusGame.targetMissionColor['y'],
                    waitTargetColor=BonusGame.targetMissionColor['color'])
            Utilities.log('BonusGame.txt', 'round completed', 'remaining ' + str(numRound))
            numRound -= 1
        print("process bonus game completed")
        myRobot.delay(2000)
        # return to front page
        #worldColor = Color(248, 145, 65) # (944, 808)
        worldColor = Color(209, 188, 158) # (944, 808)  Halloween
        while myRobot.getPixelColor(944, 808) != worldColor:
            Utilities.fastClick(1214, 233)
            Utilities.closeMissionMenu()
            BonusGame.checkProtectionSettingMenu()
            myRobot.delay(2000)
        myRobot.delay(2000)

    @staticmethod
    def checkProtectionSettingMenu():
        noColor = Color(205,217,232) # (842, 748)
        if myRobot.getPixelColor(842, 748) == noColor:
            Utilities.fastClick(842,748)
        dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
        getRewardColor = Color(2, 16, 64) # (918, 883)
        if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
            Utilities.fastClick(1223, 149)
            
    @staticmethod
    def goToMissionMenu():
        rewardExchangeColor = Color(110, 84, 63) # (1212, 89)
        while myRobot.getPixelColor(1212, 89) != rewardExchangeColor:
            Utilities.fastClick(822, 514)
            myRobot.delay(3000)

        if not BonusGame.targetGameBanner['region'].exists(BonusGame.targetGameBanner['image']):
            Utilities.scrollMenuDown_fast()
        if not BonusGame.targetGameBanner['region'].exists(BonusGame.targetGameBanner['image']):
            Utilities.scrollMenuDown_fast()
        BonusGame.targetGameBanner['region'].click(BonusGame.targetGameBanner['image'])
        myRobot.delay(1000)
        
        missionColor = Color(255, 253, 91) # (1139,337)
        while myRobot.getPixelColor(
                BonusGame.targetMissionColor['x'], BonusGame.targetMissionColor['y']) != \
                BonusGame.targetMissionColor['color']:
            myRobot.delay(2000)
        myRobot.delay(1000)

        

def process(numRound):
    obj = BonusGame()
    obj.process(numRound)
    

if __name__ == "__main__":
    #BonusGame.goToMissionMenu()
    #BonusGame.setFollowerFilter()
    #BonusGame.enterMission()
    #BonusGame.selectUnit4_Storm()
    #BonusGame.selectUnit5_MagicAndDraw()
    #BonusGame.battleBoss()
    #while True:
    #    if not BonusGame.isBoss():
    #        break
    #BonusGame.battleBlueHorse()
    #BonusGame.battleBlue() 
    #BonusGame.battleBoss()
    #BonusGame.doOneRound()
    #exit(1)
    print(BonusGame.isHard())
    print(BonusGame.isBoss())
    process(10)
    
 
