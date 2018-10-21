import java.awt.Color as Color
import Utilitites as util
from Utilitites import myRobot
reload(util)


def enterStage8(isWorldPlay=True):
    stage8Region = Region(249,62,93,729)
    stage8Icon = "stage8Icon.png"
    while not stage8Region.exists(Pattern(stage8Icon).similar(0.9)):
        wheel(stage8Region, WHEEL_UP, 20)
        util.log('stage8_server.txt', 'enter', 'scroll down for stage 8')
        # somehow during the process, it might click into a certain stage.
        # so want to go back to stage menu
        #util.leaveStageDetailPage()
        myRobot.delay(500)
    util.log('stage8_server.txt', 'enter', 'saw stage server')

    stage8Location = stage8Region.find(Pattern(stage8Icon).similar(0.9))
    while stage8Region.exists(Pattern(stage8Icon).similar(0.9)):
        util.fastClick(stage8Location.x, stage8Location.y)
        myRobot.delay(1000)

    if isWorldPlay:
        selectWorldToPlay()
    else:
        selectFriendToPlay()
        

def selectWorldToPlay():
    util.selectWorldPlay()
    myRobot.delay(500)

    while not util.isInGame():   
        util.spendEnergyPlayIfAvailable()
        myRobot.delay(1000)
    util.log('stage8_server.txt', 'enter', 'entered stage 8')
    
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
        
def playStage8():
    util.log('stage8_server.txt', 'play', 'start playing stage 8')
    moveCount = 0
    start_time = time.time()
    stopped = False
    while not util.isGameFinished():       
        util.moveRight(interval=500, num_steps=15)
        util.myRobot.delay(100)
        util.moveLeft(interval=500, num_steps=15)
        util.myRobot.delay(100)
        moveCount += 1
        # starting from 35s, the bombs come
        if not stopped and time.time() - start_time > 35.0:
            stopped = True
            util.moveLeft(interval=500, num_steps=15)
            util.moveRight(interval=500, num_steps=15, ratio=0.55)
            myRobot.delay(1500)
            util.clickAbility(1)
            myRobot.delay(4000)
            util.clickOD()
            
    #myRobot.delay(3000)
    util.log('stage8_server.txt', 'play', 'completed stage 8')



def play():
    countWin = 0
    countLose = 0
    countUnknown = 0
    countTotal = 0
    checkPeriod = 10
    while True:
        countTotal += 1
        enterStage8(isWorldPlay=True)
        playStage8()
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
            util.log('stage8_server.txt', 'result', 'check rewards and ads')
            util.goBackToHomePage()
            myRobot.delay(2000)
            WatchAds.checkAdsOneRound()

            # go back to stage menu
            bigPlayLocation = Location(876, 894)
            bigPlayColor = Color(255, 186, 38)
            util.waitForColorAndDo(bigPlayLocation.x, bigPlayLocation.y, bigPlayColor)


if __name__ == "__main__":
    myRobot.delay(1000)
    enterStage8(isWorldPlay=True)
    playStage8()
    exit(0)
    util.launchHawk()
    bigPlayLocation = Location(876, 894)
    bigPlayColor = Color(255, 186, 38)
    util.waitForColorAndDo(bigPlayLocation.x, bigPlayLocation.y, bigPlayColor)
    play()