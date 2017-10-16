import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

class ExpeditionRunner:
    LockColor = Color(138, 138, 138) # (1030,706)
    MissionFailColor = Color(166, 187, 200) # (1046,510)
    AchievementColor = Color(186, 101, 225) # (1203,233)
    completedIcon = "completedIcon.png"
    completedIconRegion = Region(908,465,135,544)
    missionTypeA = "missionTypeA.png"
    missionTypeB = "missionTypeB.png"
    missionTypeC = "missionTypeC.png"
    missionTypeD = "missionTypeD.png"
    missionTypeS = "missionTypeS.png"
    missionRegion = Region(1132,412,89,430)
    autoFillColor = Color(19,49,84) # (852,1019)
    launchColor = Color(0, 40, 82) # (1135,1024)
    secondLevelLaunchColor = Color(239, 242, 246) # (975,799)



    
    @staticmethod
    def hasMissionCompleted():
        NoMissionCompleteColor = Color(13, 18, 52) # (1253,836)
        return myRobot.getPixelColor(1253,836) != NoMissionCompleteColor
    
    @staticmethod
    def enterExpeditionMenu():
        ExpeditionColor = Color(102, 148, 149) # (1180,796)
        while myRobot.getPixelColor(1203,233) != ExpeditionRunner.AchievementColor:
            if myRobot.getPixelColor(1180,796) == ExpeditionColor:
                Utilities.fastClick(1180,796)
            myRobot.delay(1000)


    @staticmethod
    def clickAllCompletedMissions():
        while ExpeditionRunner.completedIconRegion.exists(ExpeditionRunner.completedIcon):
            ExpeditionRunner.clickCompletedMission()
            
    @staticmethod
    def clickCompletedMission():
        ExpeditionRunner.completedIconRegion.click(ExpeditionRunner.completedIcon)
        myRobot.delay(2000)
        
        FailColor = Color(0, 0, 0) # (...)
        while True:
            if myRobot.getPixelColor(1030,706) == ExpeditionRunner.LockColor:
                Utilities.fastClick(1030,706)
                Utilities.log('Expedition.txt', 'Log', 'One succeeded')
                ExpeditionRunner.collectItems()
                break
            elif myRobot.getPixelColor(1046,510) == ExpeditionRunner.MissionFailColor:
                Utilities.fastClick(1046,510)
                Utilities.log('Expedition.txt', 'Log', 'One succeeded')
                ExpeditionRunner.collectItems()
                break
            Utilities.handleCommunicationError()
            myRobot.delay(1000)
        Utilities.log('Expedition.txt', 'Log', 'No more completed mission')

    @staticmethod
    def collectItems():
        nextStepColor = Color(18, 71, 141) # (942,1025)
        while myRobot.getPixelColor(942,1025) != nextStepColor:
            Utilities.fastClick(942,1025)
            Utilities.handleCommunicationError()
            myRobot.delay(500)
        while myRobot.getPixelColor(1203,233) != ExpeditionRunner.AchievementColor:
            Utilities.fastClick(959, 1032)
            Utilities.handleCommunicationError()
            myRobot.delay(1000)
        Utilities.log('Expedition.txt', 'Log', 'Item collected')

    @staticmethod
    def autoFillAndLaunch():
        Utilities.waitForColor(852,1019, ExpeditionRunner.autoFillColor, 'waiting for auto fill')
        myRobot.delay(1000)
        # click auto fill
        Utilities.fastClick(852,1019)
        myRobot.delay(1000)
        Utilities.waitForColorAndDo(1135,1024, ExpeditionRunner.launchColor)
        Utilities.waitForColor(975,799, ExpeditionRunner.secondLevelLaunchColor, 'waiting for 2nd Launch')
        myRobot.delay(1000)
        # click item boost
        Utilities.fastClick(1153, 552)
        myRobot.delay(1000)
        # click 2nd level launch
        Utilities.fastClick(975,799)
        ExpeditionRunner.waitForAchievementColor()

    @staticmethod
    def waitForAchievementColor():
        Utilities.waitForColor(1203,233, ExpeditionRunner.AchievementColor, 'waiting for achievenment color', wait_time_period=1000)

    @staticmethod
    def refillMissions():
        ExpeditionRunner.waitForAchievementColor()
        missionFullColor = Color(71, 255, 255) # (1003,371)
        myRobot.delay(1000)
        while myRobot.getPixelColor(1003,371) != missionFullColor:
            # A --> B --> C --> S --> D
            if ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeA):
                ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeA)
                Utilities.log('Expedition.txt', 'Log', 'Selected type A')
            elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeB):
                ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeB)
                Utilities.log('Expedition.txt', 'Log', 'Selected type B')
            elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeC):
                ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeC)
                Utilities.log('Expedition.txt', 'Log', 'Selected type C')
            elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeS):
                ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeS)
                Utilities.log('Expedition.txt', 'Log', 'Selected type S')
            elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeD):
                ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeD)
                Utilities.log('Expedition.txt', 'Log', 'Selected type D')
            else:
                print 'suppose mission full'
                sys.exit(-1)
                # mission full, no need to click more
            ExpeditionRunner.autoFillAndLaunch()
            ExpeditionRunner.waitForAchievementColor()
            myRobot.delay(2000)

    @staticmethod
    def returnHome():
        ExpeditionRunner.waitForAchievementColor()
        worldColor = Color(248, 145, 65) # (944,808)
        returnColor = Color(137, 149, 184) # (723,239)
        Utilities.waitForColorAndDo(723,239,returnColor)
        Utilities.waitForColor(944,808,worldColor, 'waiting for world')


    @staticmethod
    def process():
        if ExpeditionRunner.hasMissionCompleted():
            ExpeditionRunner.enterExpeditionMenu()
            myRobot.delay(1000)
            ExpeditionRunner.clickAllCompletedMissions()
            myRobot.delay(1000)
            ExpeditionRunner.refillMissions()
            myRobot.delay(1000)
            ExpeditionRunner.returnHome()
        else:
            Utilities.log('Expedition.txt', 'Log', 'no mission to harvest')


if __name__ == "__main__":
    #ExpeditionRunner.clickAllCompletedMissions()
    #ExpeditionRunner.collectItems()
    #ExpeditionRunner.refillMissions()
    #print(ExpeditionRunner.hasMissionCompleted())
    ExpeditionRunner.process()