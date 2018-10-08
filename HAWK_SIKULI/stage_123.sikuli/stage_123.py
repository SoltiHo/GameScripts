import java.awt.Color as Color
import WatchAds
import Utilities as util
from Utilities import myRobot
reload(util)
reload(WatchAds)


def enterStage123(isWorldPlay=True):
    stage123Region = Region(999,122,110,887)
    stage123Icon = "stage123Icon.png"
    while not stage123Region.exists(Pattern(stage123Icon).similar(0.9)):
        wheel(stage123Region, WHEEL_DOWN, 70)
        util.log('stage123.txt', 'enter', 'scroll down for stage 123')
        # somehow during the process, it might click into a certain stage.
        # so want to go back to stage menu
        util.leaveStageDetailPage()
        myRobot.delay(1500)
    util.log('stage123.txt', 'enter', 'saw stage 123')
    
    while stage123Region.exists(Pattern(stage123Icon).similar(0.9)):
        stage123Region.click(Pattern(stage123Icon).similar(0.9))
        myRobot.delay(2000)

    if isWorldPlay:
        selectWorldToPlay()
    else:
        selectFriendToPlay()
        

def selectWorldToPlay():
    util.selectWorldPlay()
    myRobot.delay(1000)

    while not util.isInGame():   
        util.spendEnergyPlayIfAvailable()
        myRobot.delay(1000)
    util.log('stage123.txt', 'enter', 'entered stage 123')
    
def selectFriendToPlay():
    friendIcon = "friendIcon.png"
    while True:
        if util.selectFriendToPlay(friendIcon):
            break
        else:
            # go back and re-enter friend list
            type(Key.ESC)
            myRobot.delay(1500)
            playLocation = Location(962, 1062)
            util.fastClick(playLocation.x, playLocation.y)
    myRobot.delay(2000)
           
    # wait for game to start
    while not util.isInGame():   
        util.clickPlayIfAvailable()
        myRobot.delay(1000)
    util.log('stage123.txt', 'enter', 'entered stage 123 with friend')
        
def playStage123():
    util.log('stage123.txt', 'play', 'start playing stage 123')
    moveCount = 0
    start_time = time.time()
    stopped = False
    while not util.isGameFinished():       
        util.moveRight(interval=500, num_steps=15)
        util.myRobot.delay(100)
        util.moveLeft(interval=500, num_steps=15)
        util.myRobot.delay(100)
        if moveCount > 5:
            util.clickAbility()
        moveCount += 1
        if not stopped and time.time() - start_time > 26.0:
            stopped = True
            util.moveLeft(interval=500, num_steps=15)
            util.moveRight(interval=500, num_steps=15, ratio=0.13)
            myRobot.delay(7200)
    #myRobot.delay(3000)
    util.log('stage123.txt', 'play', 'completed stage 123')



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
                'stage123.txt',
                'result', 
                'win: ' + str(countWin) + \
                ', lose: ' + str(countLose) + \
                ', unknown: ' + str(countUnknown) + \
                ', total = ' + str(countTotal)
        )
        util.leaveGameResultPage()
        myRobot.delay(2000)

        if countTotal % checkPeriod == 0:
            util.log('stage123.txt', 'result', 'check rewards and ads')
            util.goBackToHomePage()
            myRobot.delay(2000)
            WatchAds.checkAdsOneRound()

            # go back to stage menu
            bigPlayLocation = Location(876, 894)
            bigPlayColor = Color(255, 186, 38)
            util.waitForColorAndDo(bigPlayLocation.x, bigPlayLocation.y, bigPlayColor)


if __name__ == "__main__":
    play()
    exit(0)
    util.launchHawk()
    bigPlayLocation = Location(876, 894)
    bigPlayColor = Color(255, 186, 38)
    util.waitForColorAndDo(bigPlayLocation.x, bigPlayLocation.y, bigPlayColor)
    play()
