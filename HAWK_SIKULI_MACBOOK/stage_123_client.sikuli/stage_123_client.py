import java.awt.Color as Color
import Utilitites as util
from Utilitites import myRobot
reload(util)


def enterStage123(isWorldPlay=True):
    stage123Region = Region(235,109,112,677)
    stage123Icon = "stage123Icon.png"
    while not stage123Region.exists(Pattern(stage123Icon).similar(0.9)):
        wheel(stage123Region, WHEEL_UP, 70)
        util.log('stage123_client.txt', 'enter', 'scroll down for stage 123')
        # somehow during the process, it might click into a certain stage.
        # so want to go back to stage menu
        util.leaveStageDetailPage()
        myRobot.delay(1500)
    util.log('stage123_client.txt', 'enter', 'saw stage 123')

    stage123Location = stage123Region.find(Pattern(stage123Icon).similar(0.9))
    while stage123Region.exists(Pattern(stage123Icon).similar(0.9)):
        util.fastClick(stage123Location.x + 25, stage123Location.y + 30)
        myRobot.delay(1000)

    if isWorldPlay:
        selectWorldToPlay()
    else:
        selectFriendToPlay()
        

def selectWorldToPlay():
    util.selectGameLevel('easy')
    util.selectWorldPlay()
    myRobot.delay(1000)

    while not util.isInGame():   
        util.spendEnergyPlayIfAvailable()
        myRobot.delay(1000)
    util.log('stage123_client.txt', 'enter', 'entered stage 123')
    
       
def playStage123():
    util.log('stage123_client.txt', 'play', 'start playing stage 123')
    moveCount = 0
    start_time = time.time()
    stopped = False
    while not util.isGameFinished():       
        util.moveRight(interval=400, num_steps=15)
        util.myRobot.delay(100)
        if moveCount > 5:
            util.clickAbility()
        util.moveLeft(interval=400, num_steps=15)
        util.myRobot.delay(100)

        moveCount += 1
        #if not stopped and time.time() - start_time > 26.0:
        #    stopped = True
        #    util.moveLeft(interval=500, num_steps=15)
        #    util.moveRight(interval=500, num_steps=15, ratio=0.13)
        #    myRobot.delay(7200)
        spectateLocation = Location(79, 669)
        spectateColor = Color(25, 155, 191)
        if myRobot.getPixelColor(79, 669) == spectateColor:
            util.fastClick(spectateLocation.x, spectateLocation.y)
        
    #myRobot.delay(3000)
    util.log('stage123_client.txt', 'play', 'completed stage 123')


def play():
    countWin = 0
    countLose = 0
    countUnknown = 0
    countTotal = 0
    checkPeriod = 10
    while True:
        countTotal += 1
        enterStage123(isWorldPlay=True)
        playStage123()
        myRobot.delay(2000)
        result = util.getGameResult()
        if result == 'lose':
            countLose += 1
        elif result == 'win':
            countWin += 1
        else:
            countUnknown += 1
        util.log(
                'stage123_client.txt',
                'result', 
                'win: ' + str(countWin) + \
                ', lose: ' + str(countLose) + \
                ', unknown: ' + str(countUnknown) + \
                ', total = ' + str(countTotal)
        )
        util.leaveGameResultPage()
        myRobot.delay(2000)


if __name__ == "__main__":
    play()
    exit(0)
    util.launchHawk()
    bigPlayLocation = Location(876, 894)
    bigPlayColor = Color(255, 186, 38)
    util.waitForColorAndDo(bigPlayLocation.x, bigPlayLocation.y, bigPlayColor)
    play()
