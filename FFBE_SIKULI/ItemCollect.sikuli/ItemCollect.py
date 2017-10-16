import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

class ItemCollector:
    # Global Data --------------------------
    TargetUnitX = 835
    TargetUnitY = 374
    TargetColor = Color(248, 144, 65)

    BannerRegion = Region(982,288,149,733)
    BannerImage = "BannerImage.png"
    missionX = 1101
    missionY = 630
    missionColor = Color(255, 165, 229)

    @staticmethod
    def selectUnit1_Mirage():
        Utilities.openMagicMenu(1)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1061, 914)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit2_Mirage():
        Utilities.openMagicMenu(2)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1061, 914)
        myRobot.delay(1500)

    @staticmethod
    def selectUnit3_StealAll():
        Utilities.openMagicMenu(3)
        myRobot.delay(1000)
        Utilities.scrollMenuDown_fast()
        myRobot.delay(1000)
        # select the skill
        Utilities.fastClick(1070, 724)
        myRobot.delay(1500)
        

    # static method
    @staticmethod
    def enter2ndLevelMissionMenu():
        Utilities.waitForColorAndDo(
                ItemCollector.missionX,
                ItemCollector.missionY,
                ItemCollector.missionColor)
        missionStarColor = Color(255, 248, 89) # (1138,656)
        Utilities.waitForColor(1138,656, missionStarColor, 'waitting for mission star')
    
    @staticmethod
    def getTargetMissionLocation(roundNum):
        # return targetMissionX, targetMissionY, targetMissionColor
        if roundNum % 2:
            return 816, 537, Color(111, 66, 71)
        else:
            return 871, 689, Color(52, 2, 11)

    @staticmethod
    def doFirstBattle():
        ItemCollector.selectUnit1_Mirage()
        myRobot.delay(500)
        ItemCollector.selectUnit2_Mirage()
        myRobot.delay(500)
        ItemCollector.selectUnit3_StealAll()
        myRobot.delay(1000)

        # Launch
        Utilities.fastClick(809, 946) # unit 3
        myRobot.delay(500)
        Utilities.fastClick(796, 831) # unit 2
        myRobot.delay(300)
        Utilities.fastClick(793, 720) # unit 1
        Utilities.fastClick(734, 1043) # Auto
        myRobot.delay(500)
        Utilities.fastClick(734, 1043) # Auto
        # waiting for battle end
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(1000)
            myRobot.delay(300)

    @staticmethod
    def doOtherBattle():
        Utilities.fastClick(867, 1037)

        # waiting for battle end
        menuColor = Color(0, 57, 153) # 1148, 1020
        while myRobot.getPixelColor(1148, 1020) == menuColor:
            if Utilities.isWaitingForCommand():
                # click Repeat
                Utilities.fastClick(867, 1037)
                myRobot.delay(1000)
            myRobot.delay(300)

        
    @staticmethod
    def executeOneFight():
        battleEndTopBannerColor = Color(155, 149, 54) # (1031,214)
        battleCount = 0
        while myRobot.getPixelColor(1031,214) != battleEndTopBannerColor:
            if Utilities.isWaitingForCommand():
                battleCount += 1
                if battleCount == 1:
                    ItemCollector.doFirstBattle()
                else:
                    ItemCollector.doOtherBattle()
            Utilities.fastClick(1079, 485)
            myRobot.delay(2000)
    
    @staticmethod
    def process(numRounds):
        Utilities.changeToRightTeam(
                ItemCollector.TargetUnitX,
                ItemCollector.TargetUnitY,
                ItemCollector.TargetColor)
        myRobot.delay(1000)
        Utilities.goToMissionMenu(
                ItemCollector.BannerRegion,
                ItemCollector.BannerImage,
                ItemCollector.missionX,
                ItemCollector.missionY,
                ItemCollector.missionColor)
        myRobot.delay(1000)
        ItemCollector.enter2ndLevelMissionMenu()
        myRobot.delay(1000)

        # start fighting
        num = 0
        while num < numRounds:
            # enter mission
            targetMissionX, targetMissionY, targetMissionColor = \
                    ItemCollector.getTargetMissionLocation(num)
            Utilities.enterMission(targetMissionX, targetMissionY, targetMissionColor)
            myRobot.delay(1000)
            ItemCollector.executeOneFight()
            myRobot.delay(1000)
            Utilities.handleMissionEnd(
                targetX=targetMissionX,
                targetY=targetMissionY,
                waitTargetColor=targetMissionColor)
            
            myRobot.delay(2000)
            num += 1

if __name__ == "__main__":
    #ItemCollector.executeOneFight()
    ItemCollector.process(100)