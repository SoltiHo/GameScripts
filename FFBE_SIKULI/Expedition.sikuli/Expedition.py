import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
from sikuli import *
import Utilities
reload(Utilities)
myRobot = JRobot()

class ExpeditionRunner:
    LockColor = Color(138, 138, 138) # (1030,706)
    AchievementColor = Color(186, 101, 225) # (1203,233)
    completedIcon = "completedIcon.png"
    completedIconRegion = Region(908,465,135,544)
    missionTypeA = "missionTypeA.png"
    missionTypeB = None
    missionTypeC = "missionTypeC.png"
    missionTypeD = None
    missionTypeS = "missionTypeS.png"
    missionRegion = Region(1132,412,89,430)
    autoFillColor = Color(19,49,84) # (852,1019)
    launchColor = Color(0, 40, 82) # (1135,1024)
    secondLevelLaunchColor = Color(239, 242, 246) # (975,799)



    
    @staticmethod
    def hasMissionCompleted():
        NoMissionCompleteColor = Color(0, 0, 0) # (1253,836)
        return myRobot.getPixelColor(1253,836) != NoMissionCompleteColor
    
    @staticmethod
    def enterExpeditionMenu():
        ExpeditionColor = Color(102, 148, 149) # (1180,796)
        while myRobot.getPixelColor(1203,233) != ExpeditionRunner.AchievementColor:
            if myRobot.getPixelColor(1180,796) == ExpeditionColor:
                Utilities.fastClick(1180,796)
            myRobot.delay(1000)

        Utilities.waitForColorAndDo(703, 672, fastMissionColor, 
        func_while_wait=Utilities.fastClick, arg_while_wait=(929, 160))

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
                ExpeditionRunner.collectItems()
                break
            myRobot.delay(1000)

    @staticmethod
    def collectItems():
        nextStepColor = Color(18, 71, 141) # (942,1025)
        Utilities.waitForColorAndDo(942,1025, nextStepColor)
        while myRobot.getPixelColor(1203,233) != ExpeditionRunner.AchievementColor:
            Utilities.fastClick(959, 1032)
            myRobot.delay(1000)

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
    def clickOneMission():
        ExpeditionRunner.waitForAchievementColor()
        # A --> B --> C --> S --> D
        if ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeA):
            ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeA)
        elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeC):
            ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeC)
        elif ExpeditionRunner.missionRegion.exists(ExpeditionRunner.missionTypeS):
            ExpeditionRunner.missionRegion.click(ExpeditionRunner.missionTypeS)

        ExpeditionRunner.autoFillAndLaunch()

if __name__ == "__main__":
    #ExpeditionRunner.clickAllCompletedMissions()
    #ExpeditionRunner.collectItems()
    ExpeditionRunner.clickOneMission()