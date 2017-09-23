import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

class BonusGame:
    # Global Data --------------------------
    targetTeamColor = {'color': Color(211, 232, 250), 'x': 945, 'y': 425}
    targetGameBanner = {'image': "targetBanner.png", 'region': Region(816,189,214,838)}
    targetMissionColor = {'color': Color(107, 6, 9), 'x': 702, 'y': 364}
    # --------------------------------------
    @staticmethod
    def isBoss():
        bossColor = Color(204, 61, 24) # (743,541)
        bossHead = "bossHead.png"
        bossHeadRegion = Region(750,269,76,75)
        #return myRobot.getPixelColor(743,541) == bossColor
        return bossHeadRegion.exists(bossHead) is not None

    @staticmethod
    def isBlue():
        return BonusGame.isBlueDevil() or BonusGame.isBlueHorse()

    @staticmethod
    def isBlueDevil():
        blueDevilColor = Color(28, 55, 55) # (771,553)
        isBlueDevil = myRobot.getPixelColor(771,553) == blueDevilColor
        return isBlueDevil

    @staticmethod
    def isBlueHorse():
        groundColor = Color(74,57,36)  # (703,339)
        seeGound = myRobot.getPixelColor(703,339) == groundColor
        targetColor = myRobot.getPixelColor(739,427)
        isBlueHorse = (targetColor.getGreen() > 90) and not seeGound
        return isBlueHorse
    
    def isFocus():
        dragon1Color = Color(136, 141, 116) # (777, 517)
        isDragon1 = myRobot.getPixelColor(777, 517) == dragon1Color
        dragon2Color = Color(171, 141, 57) # (777, 517)
        isDragon2 = myRobot.getPixelColor(777, 517) == dragon2Color
        lionColor = Color(184, 151, 105) # (823, 553)
        isLion = myRobot.getPixelColor(823, 553) == lionColor
        blackBirdColor = Color(179, 101, 52) # (770, 503)
        isBlackBird = myRobot.getPixrlColor(770, 503) == blackBirdColor
        
        return isDragon1 or isDragon2 or isLion or isBlackBird

    @staticmethod
    def selectUnit1_MagicAndDraw():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(756, 837)  # double magic
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1071, 864)  # Ultima
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(799, 821)  # Draw
        myRobot.delay(1500)

    @staticmethod
    def selectUnit1_DoubleMagic():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(756, 837)  # double magic
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1071, 864)  # Ultima
        myRobot.delay(1000)
        Utilities.fastClick(1071, 864)  # Ultima
        myRobot.delay(1500)


    def selectUnit1_FocusAttack():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1046, 927)  # double magic
        myRobot.delay(1500)
    
    
    def selectUnit1_SkyWaive():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1041, 913)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit2_Storm():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1087, 908)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit3_Debuff():
        Utilities.openMagicMenu(3)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.fastClick(796, 832) # Debuff
        myRobot.delay(1500)


    @staticmethod
    def selectUnit4_Bomb():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1085, 737) # Bomb
        myRobot.delay(1500)


    @staticmethod
    def selectUnit4_LB():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        hasLB = Utilities.isLBAvailable(True)
        myRobot.delay(1000)
        if not hasLB:
            # click return
            Utilities.fastClick(1183, 1024)
            myRobot.delay(1000)
        else:
            # click the team
            Utilities.fastClick(1098, 734)
            myRobot.delay(1000)
        return hasLB
    
    @staticmethod
    def selectUnit2_LB():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        hasLB = Utilities.isLBAvailable(True)
        myRobot.delay(1000)
        if not hasLB:
            # click return
            Utilities.fastClick(1183, 1024)
            myRobot.delay(1000)
        else:
            # click the team
            Utilities.fastClick(1098, 734)
            myRobot.delay(1000)
        return hasLB
    
    @staticmethod
    def selectUnit5_MagicAndDraw():
        Utilities.openMagicMenu(5)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1041, 742) # double magic
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1036, 882) # stone
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(749, 925) # draw
        myRobot.delay(1500)

    @staticmethod
    def selectUnit5_DoubleMagic():
        Utilities.openMagicMenu(5)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1041, 742) # double magic
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuUp_fast()
        myRobot.delay(1000)
        Utilities.fastClick(1036, 882) # stone
        myRobot.delay(1000)
        Utilities.fastClick(1036, 882) # stone
        myRobot.delay(1500)


    @staticmethod
    def battleNormal():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_MagicAndDraw()
        myRobot.delay(1000)
        BonusGame.selectUnit5_MagicAndDraw()
        myRobot.delay(2000)

        # select  one enemy
        Utilities.fastClick(845, 427)
        myRobot.delay(1000)
    
        # launch
        Utilities.fastClick(1065, 830) # unit 5
        myRobot.delay(100)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(5000)
    
        Utilities.fastClick(1076, 724) # unit 4
        Utilities.fastClick(809, 946) # unit 3
        Utilities.fastClick(796, 831) # unit 2
        Utilities.fastClick(1090, 934) # unit 6
    
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("normal battle ended")

    @staticmethod
    def battleBlue():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_MagicAndDraw()
        myRobot.delay(1000)
        BonusGame.selectUnit5_MagicAndDraw()
        myRobot.delay(1000)
        BonusGame.selectUnit3_Debuff()
        myRobot.delay(2000)

        # select  one enemy
        Utilities.fastClick(845, 427)
        myRobot.delay(1000)
    
        # launch
        Utilities.fastClick(809, 946) # unit 3
        myRobot.delay(3000)
        
        Utilities.fastClick(1065, 830) # unit 5
        myRobot.delay(100)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(5000)
    
        Utilities.fastClick(1076, 724) # unit 4       
        Utilities.fastClick(796, 831) # unit 2
        Utilities.fastClick(1090, 934) # unit 6
    
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            print("waiting for battle to end")
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(2000)
            myRobot.delay(1000)
        print("blue battle ended")

    @staticmethod
    def battleBoss():
        while not Utilities.isWaitingForCommand():
            myRobot.delay(1000)
        myRobot.delay(2000)
        BonusGame.selectUnit1_DoubleMagic()
        myRobot.delay(1000)
        BonusGame.selectUnit5_DoubleMagic()
        myRobot.delay(1000)
        BonusGame.selectUnit3_Debuff()

        hasLB = False
        if Utilities.lookHavingLB(4):
            hasLB = BonusGame.selectUnit4_LB()
            if not hasLB:
                # bomb
                BonusGame.selectUnit4_Bomb()
        else:
             BonusGame.selectUnit4_Bomb()
        myRobot.delay(1000)
        
        if not hasLB and Utilities.lookHavingLB(2):
            hasLB = BonusGame.selectUnit2_LB()
            if not hasLB:
                # storm
                BonusGame.selectUnit2_Storm()
        else:
            BonusGame.selectUnit2_Storm()
        myRobot.delay(2000)
    
        # launch
        Utilities.fastClick(809, 946) # unit 3
        Utilities.fastClick(796, 831) # unit 2
        Utilities.fastClick(1076, 724) # unit 4       
        myRobot.delay(3000)
        
        Utilities.fastClick(1065, 830) # unit 5
        myRobot.delay(100)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(5000)
    
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
                if BonusGame.isBlue():
                    BonusGame.battleBlue()
                elif BonusGame.isBoss():
                    BonusGame.battleBoss()
                else:
                    BonusGame.battleNormal()
            Utilities.fastClick(1079, 485)
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
    def setFollowerFilter():
        targetMission = Color(255, 238, 83) # (1138,336)
        Utilities.waitForColorAndDo(1138,336, targetMission, 
                func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))
    
        # wait for mission dismiss color and buy strength if necessary
        missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
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
        #Utilities.fastClick(702, 543) # 1st row
        #myRobot.delay(500)
        #Utilities.fastClick(778, 543)
        #myRobot.delay(500)
        Utilities.fastClick(854, 543)
        myRobot.delay(500)
        #Utilities.fastClick(925, 543)
        #myRobot.delay(500)
        #Utilities.fastClick(999, 545)
        #myRobot.delay(500)
        #Utilities.fastClick(1071, 543)
        #myRobot.delay(500)
        #Utilities.fastClick(1140, 548)
        #myRobot.delay(500)
        #Utilities.fastClick(1214, 545)
        #myRobot.delay(500)
        #Utilities.fastClick(702, 623) # 2nd row
        #myRobot.delay(500)
        #Utilities.fastClick(778, 623)
        #myRobot.delay(500)
        #Utilities.fastClick(854, 623)
        #myRobot.delay(500)
        #Utilities.fastClick(925, 622)
        #myRobot.delay(500)
        #Utilities.fastClick(995, 624)
        #myRobot.delay(500)
        #Utilities.fastClick(1066, 619)
        #myRobot.delay(500)
        #Utilities.fastClick(1135, 624)
        #myRobot.delay(500)
        #Utilities.fastClick(1213, 627)
        #myRobot.delay(500)
        #Utilities.fastClick(710, 700) # 3rd row
        #myRobot.delay(500)
        #Utilities.fastClick(779, 698)
        #myRobot.delay(500)
        #Utilities.fastClick(854, 698)
        #myRobot.delay(500)
        #Utilities.fastClick(927, 697)
        #myRobot.delay(500)
        #Utilities.fastClick(995, 697)
        #myRobot.delay(500)
        #Utilities.fastClick(1066, 695)
        #myRobot.delay(500)
        #Utilities.fastClick(1143, 695)
        #myRobot.delay(500)
        #Utilities.fastClick(1213, 693)
        #myRobot.delay(1000)
    
        # select generation
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        
        #Utilities.fastClick(721, 624) # 1st row, FFBE
        #myRobot.delay(500)
        #Utilities.fastClick(814, 624) # FFI
        #myRobot.delay(500)
        #Utilities.fastClick(907, 624)
        #myRobot.delay(500)
        Utilities.fastClick(1000, 624) # FFIII
        myRobot.delay(500)
        #Utilities.fastClick(1093, 624)
        #myRobot.delay(500)
        #Utilities.fastClick(1186, 624)
        #myRobot.delay(500)
        #Utilities.fastClick(721, 699) # 2nd row, FFVI
        #myRobot.delay(500)
        #Utilities.fastClick(814, 699)
        #myRobot.delay(500)
        #Utilities.fastClick(907, 699)
        #myRobot.delay(500)
        #Utilities.fastClick(1000, 699)
        #myRobot.delay(500)
        #Utilities.fastClick(1093, 699)
        #myRobot.delay(500)
        #Utilities.fastClick(1186, 699)
        #myRobot.delay(500)
        #Utilities.fastClick(721, 774) # 3rd row, FFXIV
        #myRobot.delay(500)
        #Utilities.fastClick(814, 774)
        #myRobot.delay(500)
        #Utilities.fastClick(907, 774)  # FFT
        #myRobot.delay(500)
        #Utilities.fastClick(1000, 774)
        #myRobot.delay(500)
        #Utilities.fastClick(767, 918)  # sepcial row, ANOTHER
        #myRobot.delay(500)
    
        # click confirm
        Utilities.fastClick(958, 1008)
        myRobot.delay(2000)
    
        def clickReturnAndWait():
            Utilities.fastClick(709,221)
            myRobot.delay(1000)
    
        # click two return
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor, wait_time_period=2000,
                func_while_wait=clickReturnAndWait,
                func_after_wait=clickReturnAndWait)
        myRobot.delay(1000)                

    @staticmethod
    def process(numRound):
        Utilities.log('BonusGame.txt', 'Process', 'Start')
        BonusGame.changeToRightTeam()
        Utilities.log('BonusGame.txt', 'Process', 'team changed')
        BonusGame.goToMissionMenu()
        Utilities.log('BonusGame.txt', 'Process', 'arrive missions')
        BonusGame.setFollowerFilter()
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
        worldColor = Color(248, 145, 65) # (944, 808)
        while myRobot.getPixelColor(944, 808) != worldColor:
            Utilities.fastClick(1214, 233)
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
    def changeToRightTeam():
        # select team
        strengthenColor = Color(246, 66, 15) # 701,851
        while myRobot.getPixelColor(701,851) != strengthenColor:
            Utilities.fastClick(808, 1021)
            BonusGame.checkProtectionSettingMenu()
            myRobot.delay(2000)
        myRobot.delay(1000)
    
        while myRobot.getPixelColor(
                BonusGame.targetTeamColor['x'] ,BonusGame.targetTeamColor['y']) != \
                BonusGame.targetTeamColor['color']:
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

    @staticmethod
    def goToMissionMenu():
        rewardExchangeColor = Color(110, 84, 63) # (1212, 89)
        while myRobot.getPixelColor(1212, 89) != rewardExchangeColor:
            Utilities.fastClick(822, 514)
            myRobot.delay(3000)

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
    #BonusGame.changeToRightTeam()
    #BonusGame.goToMissionMenu()
    #BonusGame.setFollowerFilter()
    #BonusGame.enterMission()
    #BonusGame.selectUnit1_MagicAndDraw()
    #BonusGame.selectUnit5_MagicAndDraw()
    #BonusGame.battleNormal()
    #while True:
    #    if not BonusGame.isBoss():
    #        break
    #BonusGame.battleBlueHorse()
    #BonusGame.battleBlue() 
    #BonusGame.battleBoss()
    #BonusGame.doOneRound()
    print(BonusGame.isBlue())
    print(BonusGame.isBlueDevil())
    print(BonusGame.isBlueHorse())
    print(BonusGame.isBoss())
    process(10)
    
 
