import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()


class CoFightRunner:
    # Global Data --------------------------
    CofightMenuHeaderColor = Color(8, 3, 7)  # (894,384)
    targetMissionColor = Color(58, 205, 40) # (1134,616)
    buyBallsColor = Color(94, 0, 0) # (1031, 617)
    cofightBannerIcon = "cofightBannerIcon.png"
    cofightBannerRegion = Region(835,166,246,873)
    # --------------------------------------
    @staticmethod
    def selectUnit1_Mirage():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1068, 935)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit1_Shield():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(760, 915)
        myRobot.delay(1000)
        Utilities.fastClick(796, 716)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit1_Kill():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(784, 727)
        myRobot.delay(1500)
    
    @staticmethod    
    def selectUnit2_WaterBon():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(775, 908)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit2_Debuff():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(781, 814)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit4_LBIfAvailable():
        if Utilities.lookHavingLB(4):
            Utilities.openMagicMenu(4)
            myRobot.delay(1000)
            return Utilities.isLBAvailable_BS(True)
        return False

    @staticmethod
    def selectUnit4_DarkProtection():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1062, 718)
        myRobot.delay(1000)
        Utilities.fastClick(1097, 730)    
        myRobot.delay(1500)

    @staticmethod
    def selectUnit4_Defense():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1060, 732)
        myRobot.delay(1000)
        Utilities.fastClick(1097, 730)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit4_Attack():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(778, 736)
        myRobot.delay(1000)
        Utilities.fastClick(1097, 730)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit4_MagicBuffFina():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(799, 932)
        myRobot.delay(1000)
        Utilities.fastClick(750, 827)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit4_AtkBuffLuneth():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(793, 828)
        myRobot.delay(1000)
        Utilities.fastClick(789, 728)
        myRobot.delay(1500)


    @staticmethod
    def selectUnit4_MPSelf():
        Utilities.openMagicMenu(4)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1075, 905)
        myRobot.delay(1000)
        Utilities.fastClick(1071, 721)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit3_Mirage():
        Utilities.openMagicMenu(3)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1070, 916)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit3_Debuff():
        Utilities.openMagicMenu(3)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(786, 837)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit5_StrongRecover():
        Utilities.openMagicMenu(5)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1055, 934)
        myRobot.delay(1000)
        Utilities.fastClick(1080, 719)    
        myRobot.delay(1500)

    @staticmethod
    def selectUnit5_Miracle():
        Utilities.openMagicMenu(5)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(789, 937)
        myRobot.delay(1000)
        Utilities.fastClick(1074, 815)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit5_Shield():
        Utilities.openMagicMenu(5)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(789, 937)
        myRobot.delay(1000)
        Utilities.fastClick(798, 833)
        myRobot.delay(1500)

    @staticmethod
    def checkProtectionSettingMenu():
        noColor = Color(205, 217, 232) # (842, 748)
        if myRobot.getPixelColor(842, 748) == noColor:
            Utilities.fastClick(842,748)
        dailyRewardBoxColor = Color(255, 255, 221) # (804, 800)
        getRewardColor = Color(2, 16, 64) # (918, 883)
        if (myRobot.getPixelColor(804, 800) == dailyRewardBoxColor) and (myRobot.getPixelColor(918, 883) == getRewardColor):
            Utilities.fastClick(1223, 149)

    @staticmethod
    def isInBattle():
        menuColor = Color(0, 58, 130) # (1129, 1029)
        if myRobot.getPixelColor(1129, 1029) == menuColor:
            return True
        else:
            return False

    @staticmethod
    def launchAttack(roundNum):
        Utilities.fastClick(1076, 724) # unit 4
        Utilities.fastClick(1065, 830) # unit 5
        myRobot.delay(1000)
    
        Utilities.fastClick(809, 946) # unit 3   
        myRobot.delay(200)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(300)
        Utilities.fastClick(796, 831) # unit 2
    
        # click Auto twice
        Utilities.fastClick(720, 1037) # Auto
        myRobot.delay(500)
        Utilities.fastClick(720, 1037) # Auto
        myRobot.delay(2000)

    @staticmethod
    def setUnit1Cmd(round):
        if round == 1:
            CoFightRunner.selectUnit1_Shield()
        elif round % 3 == 1:
            CoFightRunner.selectUnit1_Kill()
        else:
            CoFightRunner.selectUnit1_Mirage()

    @staticmethod
    def setUnit2Cmd(round):
        CoFightRunner.selectUnit2_WaterBon()

    @staticmethod
    def setUnit3Cmd(round):
        if round % 3 == 1:
            CoFightRunner.selectUnit3_Debuff()
        else:
            CoFightRunner.selectUnit3_Mirage()

    @staticmethod
    def setUnit4Cmd(round):
        if round % 5 == 1:
            CoFightRunner.selectUnit4_DarkProtection()
        elif round % 5 == 2:
            if Utilities.lookHavingLB(4):
                if not CoFightRunner.selectUnit4_LBIfAvailable():
                    CoFightRunner.selectUnit4_Defense()
            else:
                CoFightRunner.selectUnit4_Defense()
        elif round % 5 == 3:
            if Utilities.lookHavingLB(4):
                if not CoFightRunner.selectUnit4_LBIfAvailable():
                    CoFightRunner.selectUnit4_MPSelf()
            else:
                CoFightRunner.selectUnit4_MPSelf()
        elif round % 5 == 4:
            CoFightRunner.selectUnit4_MagicBuffFina()
        else:
            CoFightRunner.selectUnit4_AtkBuffLuneth()
    
    @staticmethod
    def setUnit5Cmd(round):
        if round == 1:
            CoFightRunner.selectUnit5_StrongRecover()
        elif round % 2 == 0:
            CoFightRunner.selectUnit5_Miracle()
        else:
            CoFightRunner.selectUnit5_Shield()

    @staticmethod
    def doOneFight():
        Utilities.log('CoFight.txt', 'One Battle', 'Started')
        #myRobot.delay(5000)
        # waiting for waiting for command
        while not CoFightRunner.isInBattle():
            myRobot.delay(1000)
        Utilities.log('CoFight.txt', 'One Battle', 'is in battle')
        # wait for waiting for command
        roundCount = 1
        while CoFightRunner.isInBattle():
            if Utilities.isWaitingForCommand():
                myRobot.delay(2000)
                CoFightRunner.setUnit1Cmd(roundCount)
                myRobot.delay(1000)
                CoFightRunner.setUnit2Cmd(roundCount)
                myRobot.delay(1000)
                CoFightRunner.setUnit3Cmd(roundCount)
                myRobot.delay(1000)
                CoFightRunner.setUnit4Cmd(roundCount)
                myRobot.delay(1000)
                CoFightRunner.setUnit5Cmd(roundCount)
                myRobot.delay(1000)
                CoFightRunner.launchAttack(roundCount)
                roundCount += 1
                myRobot.delay(3000)
            else:
                print("waiting for waiting for command")
                myRobot.delay(1000)
        print("One Battle Ended")
        
        Utilities.handleMissionEnd(targetX=894, targetY=384, waitTargetColor=CoFightRunner.CofightMenuHeaderColor)
        Utilities.log('CoFight.txt', 'One Battle', 'ended. ' + str(roundCount) + ' rounds')
        
    @staticmethod
    def enterMission(buyStrength=False):
        Utilities.waitForColor(1134,616, CoFightRunner.targetMissionColor, 'waiting for target mission')
        if buyStrength:
            while myRobot.getPixelColor(1134, 616) == CoFightRunner.targetMissionColor:
                Utilities.fastClick(1134, 616)
                myRobot.delay(1000)
                if myRobot.getPixelColor(1031, 617) == CoFightRunner.buyBallsColor:
                    Utilities.fastClick(1031, 617)
        else:
            Utilities.waitForColorAndDo(1134,616, CoFightRunner.targetMissionColor)
    
        # wait for mission dismiss color and buy strength if necessary
        missionDescNextStepColor = Color(0, 92, 201) # (954, 923)
        Utilities.waitForColorAndDo(954, 923, missionDescNextStepColor)
        # select follower
        followerColor = Color(143,89,48) # (1015,223)
        Utilities.waitForColorAndDo(1015, 223, followerColor, 
            func_after_wait=Utilities.fastClick, arg_after_wait=(810, 404))
        launchColor = Color(0, 43, 68)  # (913,951)
        Utilities.waitForColorAndDo(913, 951, launchColor)

    @staticmethod
    def changeToRightTeam():
        # select team
        strengthenColor = Color(246, 66, 15) # 701,851
        while myRobot.getPixelColor(701,851) != strengthenColor:
            Utilities.fastClick(808, 1021)
            CoFightRunner.checkProtectionSettingMenu()
            myRobot.delay(2000)
        myRobot.delay(1000)
    
        targetUnitColor = Color(90, 73, 77)  # (1066,402)
        while myRobot.getPixelColor(1066,402) != targetUnitColor:
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
    def gotoCofightMenu():
        #CofightBannerColor = Color(97, 244, 245) # (1015,446)
        #Utilities.waitForColorAndDo(1015,446, CofightBannerColor, wait_time_period=2000,
        #        func_while_wait=Utilities.fastClick, arg_while_wait=(822, 514))
        rewardExchangeColor = Color(110, 84, 63) # (1212, 89)
        while myRobot.getPixelColor(1212, 89) != rewardExchangeColor:
            Utilities.fastClick(822, 514)
            myRobot.delay(3000)
        CoFightRunner.cofightBannerRegion.click(CoFightRunner.cofightBannerIcon)
        myRobot.delay(1000)
        CoFightRunner.waitForCofightMenuHeader()
        myRobot.delay(1000)

    @staticmethod
    def waitForCofightMenuHeader():
        # wait for cofight menu
        Utilities.waitForColor(894,384, CoFightRunner.CofightMenuHeaderColor, "waiting for CofightMenuHeader")
        myRobot.delay(1000)
    
    def setFollowerFilter():
        Utilities.waitForColorAndDo(1134,616, CoFightRunner.targetMissionColor, 
                func_while_wait=Utilities.fastClick, arg_while_wait=(1134,616))
    
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
        Utilities.fastClick(702, 543) # 1st row
        myRobot.delay(500)
        #Utilities.fastClick(778, 543)
        #myRobot.delay(500)
        #Utilities.fastClick(854, 543)
        #smyRobot.delay(500)
        #Utilities.fastClick(925, 543)
        #myRobot.delay(500)
        Utilities.fastClick(999, 545)
        myRobot.delay(500)
        Utilities.fastClick(1071, 543)
        myRobot.delay(500)
        Utilities.fastClick(1140, 548)
        myRobot.delay(500)
        Utilities.fastClick(1214, 545)
        myRobot.delay(500)
        #Utilities.fastClick(702, 623) # 2nd row
        #myRobot.delay(500)
        #Utilities.fastClick(778, 623)
        #myRobot.delay(500)
        Utilities.fastClick(854, 623)
        myRobot.delay(500)
        Utilities.fastClick(925, 622)
        myRobot.delay(500)
        Utilities.fastClick(995, 624)
        myRobot.delay(500)
        #Utilities.fastClick(1066, 619)
        #myRobot.delay(500)
        Utilities.fastClick(1135, 624)
        myRobot.delay(500)
        Utilities.fastClick(1213, 627)
        myRobot.delay(500)
        Utilities.fastClick(710, 700) # 3rd row
        myRobot.delay(500)
        Utilities.fastClick(779, 698)
        myRobot.delay(500)
        #Utilities.fastClick(854, 698)
        #myRobot.delay(500)
        #Utilities.fastClick(927, 697)
        #myRobot.delay(500)
        #Utilities.fastClick(995, 697)
        #myRobot.delay(500)
        #Utilities.fastClick(1143, 695)
        #myRobot.delay(500)
        Utilities.fastClick(1213, 693)
        myRobot.delay(1000)
    
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
    def process(numFight=0):
        CoFightRunner.changeToRightTeam() 
        myRobot.delay(2000)
        CoFightRunner.gotoCofightMenu()
        myRobot.delay(2000)
        #setFollowerFilter()
        #myRobot.delay(2000)
        if numFight == 0:
            firstBallColor = Color(57, 181, 47) # (1142, 305)
            forthBallColor = Color(90, 235, 45) # (1221, 301)
            targetBallColor = firstBallColor
            targetBallX = 1142
            targetBallY = 305
            while myRobot.getPixelColor(targetBallX, targetBallY) == targetBallColor:
                CoFightRunner.enterMission()
                myRobot.delay(3000)
                # got ball
                CoFightRunner.doOneFight()
                myRobot.delay(2000)
        else:
            while numFight > 0:
                numFight -= 1
                CoFightRunner.enterMission(True)
                myRobot.delay(3000)
                CoFightRunner.doOneFight()
                myRobot.delay(2000)
                
                
        # back to front page, click "Return"
        Utilities.fastClick(1213, 234)
        myRobot.delay(2000)

    @staticmethod
    def testRun(num):
        if num == 1:
            set1stCommand()
        else:
            set2ndCommand()
        myRobot.delay(2000)
        launchAttack(num)
        myRobot.delay(20000)
    
    def test(roundCount):
        setUnit1Cmd(roundCount)
        myRobot.delay(1000)
        setUnit2Cmd(roundCount)
        myRobot.delay(1000)
        setUnit3Cmd(roundCount)
        myRobot.delay(1000)
        setUnit4Cmd(roundCount)
        myRobot.delay(1000)
        setUnit5Cmd(roundCount)
        myRobot.delay(2000)
        launchAttack(roundCount)
        myRobot.delay(1000)
        
    
    def testTiming():
        myRobot.delay(1000)
        
        #Utilities.fastClick(809, 946) # unit 3   
        myRobot.delay(200)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(300)
        Utilities.fastClick(796, 831) # unit 2

if __name__ == "__main__":
    CoFightRunner.process()
    #CoFightRunner.doOneFight()
