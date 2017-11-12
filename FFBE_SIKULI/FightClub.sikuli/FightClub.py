import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import BonusGame
import Utilities
reload(Utilities)
myRobot = JRobot()


def isAtFrontMenu():
    frontMenuColor = Color(2, 14, 32) # (1062, 918)
    if myRobot.getPixelColor(1062, 918) == frontMenuColor:
        return True
    else:
        return False

def isOutOfMp():
    outOfMP = True
    for waitCount in range(0,4):
        myRobot.delay(500)
        if isAtFrontMenu():
            outOfMP = False
            break
    return outOfMP

def returnToFrontMenuIfOutOfMP():
    if isOutOfMp():
        Utilities.fastClick(1188, 1018) # click on return
        myRobot.delay(2000)
        if not isAtFrontMenu():
            # double magic, needs 2 return
            Utilities.fastClick(1188, 1018) # click on return again
    myRobot.delay(500)

def selectUnit1_AttackAll():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1027, 928)
    returnToFrontMenuIfOutOfMP()

def selectUnit1_Shield():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(783, 916)
    returnToFrontMenuIfOutOfMP()

def selectUnit1_ReduceDamage():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1052, 824)
    myRobot.delay(1000)
    Utilities.fastClick(806, 725)
    returnToFrontMenuIfOutOfMP()

def selectUnit1_Storm():
    Utilities.openMagicMenu(1)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(793, 923)
    returnToFrontMenuIfOutOfMP()

def selectUnit2_Thunder():
    Utilities.openMagicMenu(2)
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1040, 820)
    returnToFrontMenuIfOutOfMP()


def selectUnit2_WaterBon():
    Utilities.openMagicMenu(2)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select skill
    Utilities.fastClick(1075, 816)
    returnToFrontMenuIfOutOfMP()


def selectUnit2_twoMagic():
    Utilities.openMagicMenu(2)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # double magic
    Utilities.fastClick(785, 936)
    myRobot.delay(700)
    Utilities.scrollMenuUp_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1058, 820) # thunder
    myRobot.delay(700)
    Utilities.fastClick(1058, 820) # thunder
    #myRobot.delay(800)
    returnToFrontMenuIfOutOfMP()


def selectUnit2_TwoUltima():
    Utilities.openMagicMenu(2)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # double magic
    Utilities.fastClick(785, 936)
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1058, 820) # Ultima
    myRobot.delay(700)
    Utilities.fastClick(1058, 820) # Ultima
    #myRobot.delay(800)
    returnToFrontMenuIfOutOfMP()



def selectUnit2_StormRain():
    Utilities.openMagicMenu(2)
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(500)
    # select the skill
    Utilities.fastClick(755, 911)
    #myRobot.delay(800)
    returnToFrontMenuIfOutOfMP()

def selectUnit3_AttackAll():
    Utilities.openMagicMenu(3)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(796, 733)
    #myRobot.delay(800)
    returnToFrontMenuIfOutOfMP()


def selectUnit3_Shield():
    Utilities.openMagicMenu(3)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1081, 907)
    returnToFrontMenuIfOutOfMP()

def selectUnit3_HP():
    Utilities.openMagicMenu(3)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1081, 805)
    myRobot.delay(1000)
    Utilities.fastClick(799, 932)
    returnToFrontMenuIfOutOfMP()


def selectUnit3_StopMovement():
    Utilities.openMagicMenu(3)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(751, 824)
    #myRobot.delay(800)
    returnToFrontMenuIfOutOfMP()

def selectUnit4_Thunder():
    Utilities.openMagicMenu(4)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1042, 725)
    returnToFrontMenuIfOutOfMP()

def selectUnit4_light():
    Utilities.openMagicMenu(4)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1033, 814)
    returnToFrontMenuIfOutOfMP()

def selectUnit4_Storm():
    Utilities.openMagicMenu(4)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1064, 916)
    returnToFrontMenuIfOutOfMP()

def selectUnit4_twoMagic():
    Utilities.openMagicMenu(4)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(742, 812)
    myRobot.delay(800)
    # select two thunder
    Utilities.scrollMenuUp_fast()
    myRobot.delay(700)
    Utilities.fastClick(1070, 831) # thunder
    #Utilities.fastClick(761, 816) # snow
    myRobot.delay(1000)
    Utilities.fastClick(1070, 831) # thunder
    #Utilities.fastClick(761, 816) # snow    
    #myRobot.delay(1000)
    returnToFrontMenuIfOutOfMP()
    
def selectUnit5_twoMagic():
    Utilities.openMagicMenu(5)
    myRobot.delay(700)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(700)
    # select the skill
    Utilities.fastClick(1069, 736)
    myRobot.delay(800)
    # select two thunder
    Utilities.scrollMenuUp_fast()
    myRobot.delay(700)
    Utilities.fastClick(774, 928) # thunder
    #Utilities.fastClick(1048, 808) # snow
    myRobot.delay(1000)
    Utilities.fastClick(774, 928) # thunder
    #Utilities.fastClick(1048, 808) # snow
    myRobot.delay(1000)
    #Utilities.fastClick(789, 829)  # for stone
    #myRobot.delay(1000)
    returnToFrontMenuIfOutOfMP()

def selectUnit5_Stone():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(789, 829)  # for stone
    returnToFrontMenuIfOutOfMP()

def selectUnit5_Thunder():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(766, 925)
    returnToFrontMenuIfOutOfMP()

def selectUnit5_TimeStop():
    Utilities.openMagicMenu(5)
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    Utilities.scrollMenuDown_fast()
    myRobot.delay(1000)
    # select the skill
    Utilities.fastClick(1074, 710)  # for stone
    returnToFrontMenuIfOutOfMP()

def isInBattle():
    menuColor = Color(0, 58, 130) # (1129, 1029)
    emptyUnitColor = Color(1, 7, 19) # (981, 930)
    if (myRobot.getPixelColor(1129, 1029) == menuColor) and (myRobot.getPixelColor(981, 930) == emptyUnitColor):
        return True
    else:
        return False

def setCommand(round):
    if Utilities.isUnitAlive(1):
        if round <= 2:
            selectUnit1_Shield()
        else:
            selectUnit1_ReduceDamage()
        myRobot.delay(1000)
    if Utilities.isUnitAlive(2):
        selectUnit2_twoMagic()
        myRobot.delay(1000)
    if Utilities.isUnitAlive(3):
        if round <= 2:
            selectUnit3_Shield()
        else:
            selectUnit3_HP()
        myRobot.delay(1000)
    if Utilities.isUnitAlive(4):
        selectUnit4_twoMagic()
        myRobot.delay(1000)
    if Utilities.isUnitAlive(5):
        if Utilities.lookAbleToSummon():
            Utilities.summonIfAvailable(5)
            myRobot.delay(2000)
        elif Utilities.lookHavingLB(5):
            Utilities.openMagicMenu(5)
            myRobot.delay(1000)
            Utilities.isLBAvailable_BS(True)
            myRobot.delay(1000)
            returnToFrontMenuIfOutOfMP()
        elif round <= 3:
            selectUnit5_twoMagic()
        else:
            selectUnit5_Stone()
        myRobot.delay(1000) 

def launchAttack_2MirageWaterBonStormTimestop(round):
    if round <= 10:
        Utilities.fastClick(1065, 830) # unit 5
        myRobot.delay(1500)
        Utilities.fastClick(809, 946) # unit 3   
        myRobot.delay(200)
        Utilities.fastClick(793, 720) # unit 1
        myRobot.delay(200)
        Utilities.fastClick(1076, 724) # unit 4
        myRobot.delay(250)
        Utilities.fastClick(796, 831) # unit 2

def launchAttack(round):
    Utilities.fastClick(809, 946) # unit 3   
    myRobot.delay(200)
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(700)
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
        

def launchAttack_typical2Mirage3Magic(round):
    Utilities.fastClick(809, 946) # unit 3   
    myRobot.delay(200)
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(700)
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
        

def launchAttack_typical3magic():
    Utilities.fastClick(1076, 724) # unit 4
    myRobot.delay(100)
    Utilities.fastClick(796, 831) # unit 2
    myRobot.delay(100)
    Utilities.fastClick(1065, 830) # unit 5
    myRobot.delay(500)
    Utilities.fastClick(793, 720) # unit 1
    myRobot.delay(300)
    Utilities.fastClick(809, 946) # unit 3



def doOneFight():
    Utilities.fastClick(967, 1009)
    myRobot.delay(1000)
    # hit OK
    OColor = Color(255, 255, 255) # (930, 1023)
    Utilities.waitForColorAndDo(930, 1023, OColor)
    myRobot.delay(1000)
    # select 1st entry
    BarColor = Color(0, 85, 128) # (909, 517)
    Utilities.waitForColorAndDo(909, 517, BarColor)
    myRobot.delay(1000)
    # confirm
    yesColor = Color(0, 41, 94) # (1036, 598)
    Utilities.waitForColorAndDo(1036, 598, yesColor)
    myRobot.delay(1000)
    # wait for "Begin Battle"
    beginBattleColor = Color(70, 0, 0) # (1053, 919)
    Utilities.waitForColorAndDo(1053, 919, beginBattleColor)    
    while not isInBattle():
        myRobot.delay(1000)
    # wait for waiting for command
    round = 0
    while isInBattle():
        if Utilities.isWaitingForCommand():
            round = round + 1
            setCommand(round)
            myRobot.delay(1000)
            launchAttack(round)
        else:
            print("waiting for waiting for command")
        myRobot.delay(3000)

    # Battle End
    endOColor = Color(244, 246, 250) # (944, 904)
    while myRobot.getPixelColor(944, 904) != endOColor:
        Utilities.handleCommunicationError()
        print("waiting for end ok")
        myRobot.delay(1000)
        Utilities.fastClick(1012, 724)
    myRobot.delay(3000)

    winColor = Color(254,254,20)  # (960, 200)
    won = myRobot.getPixelColor(960, 200) == winColor
    Utilities.fastClick(944, 904)
    myRobot.delay(3000)
    
    secondEndOColor = Color(255, 255, 255) # (941, 1006)
   
    def checkRewardFunc():
        getRewardOColor = Color(255, 255, 255) # (942, 702)
        if myRobot.getPixelColor(942, 702) == getRewardOColor:
            Utilities.fastClick(942, 702)
            myRobot.delay(1000)
    def checkOkColor():
        okColor = Color(244, 246, 250) # (944, 904)
        if myRobot.getPixelColor(944, 904) == okColor:
            Utilities.fastClick(944, 904)
            myRobot.delay(1000)
    Utilities.waitForColorAndDo(941, 1006, secondEndOColor)
    myRobot.delay(1000)
    # wait for prepare
    prepareColor = Color(103, 0, 0) # (866, 999)
    while myRobot.getPixelColor(866, 999) != prepareColor:
        print("waiting for preparation sign")
        getRewardOColor = Color(255, 255, 255) # (942, 702)
        if myRobot.getPixelColor(942, 702) == getRewardOColor:
            Utilities.fastClick(942, 702)
        myRobot.delay(1000)
    myRobot.delay(2000)
    print "exitting doOneFight()"
    return won

def closeDailyMissionMessage():
    dailyMissionCloseColor = Color(0, 6, 38) # (782,670)
    if myRobot.getPixelColor(782,670) == dailyMissionCloseColor:
        Utilities.waitForColorAndDo(782,670,dailyMissionCloseColor)
    
def consumeAllBalls():
    prepareColor = Color(103, 0, 0) # (866, 999)
    while myRobot.getPixelColor(866, 999) != prepareColor:
        print("waiting for preparation sign")
        myRobot.delay(1000)

    firstBallColor = Color(0,238,197) # (910, 980)
    while myRobot.getPixelColor(910, 980) == firstBallColor:
        result = doOneFight()
        print("One fight done, result = " + str(result))
    # no ball now, return to front page
    myRobot.delay(5000)
    beforeCheckWorldColor = myRobot.getPixelColor(944, 808)
    worldColor = Color(248, 145, 65) # (944, 808)
    prepareColor = Color(103, 0, 0) # (866, 999)

    while myRobot.getPixelColor(944, 808) != worldColor:
        if myRobot.getPixelColor(866,999) == prepareColor:
            Utilities.fastClick(706, 209)
        closeDailyMissionMessage()
        print("no more ball now, waiting for world color")
        Utilities.checkProtectionSettingMenu()
        Utilities.getDailyReward()
        myRobot.delay(5000)
    myRobot.delay(1000)

def process():
    fightClubColor = Color(153, 162, 187) # (747, 758)
    while myRobot.getPixelColor(747, 758) != fightClubColor:
        print("waiting for fight club")
        BonusGame.BonusGame.checkProtectionSettingMenu()
        Utilities.getDailyReward()
        myRobot.delay(1000)
    myRobot.delay(1000)

    firstBallColor = Color(24, 159, 146) # (703, 829)
    if myRobot.getPixelColor(703, 829) == firstBallColor:
        # got ball
        Utilities.fastClick(703, 829)
        consumeAllBalls()
        myRobot.delay(2000)

def testRun(num):
    setCommand(num)
    myRobot.delay(3000)
    launchAttack(num)
    myRobot.delay(10000)


def manual(roundNum):
    setCommand(roundNum)
    myRobot.delay(2000)
    launchAttack(roundNum) 
    myRobot.delay(10000)

if __name__ == "__main__":
    #print(isInBattle())
    #doOneFight()
    #testRun(1)
    #selectUnit3_HP()
    #manual(1)
    process()
