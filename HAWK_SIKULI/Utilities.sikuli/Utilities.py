import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import time
from sikuli import *
myRobot = JRobot()

leftX = 660 
rightX = 1258

def getGameResult():
    log('util.txt', 'debug', 'getting game result')
    while not isGameFinished():
        log('util.txt', 'debug', 'confirming game ended')
        closeItemDescIfAny()
        myRobot.delay(1000)
    log('util.txt', 'debug', 'game end confirmed')
    loseResultLocation = Location(727, 187)
    loseResultColor = Color(42, 155, 175)
    winResultLocation = Location(727, 187)
    winResultColor = Color(253, 150, 26)
    if myRobot.getPixelColor(loseResultLocation.x, loseResultLocation.y) == loseResultColor:
        return 'lose'
    elif myRobot.getPixelColor(winResultLocation.x, winResultLocation.y) == winResultColor:
        return 'win'
    else:
        return 'unknown'
    

def isInGame():
    inGameLocation = Location(708, 87)
    inGameColor = Color(255, 255, 102)
    return myRobot.getPixelColor(inGameLocation.x, inGameLocation.y) == inGameColor

def clickPlayIfAvailable():
    playLocation = Location(908, 1067)
    playColor = Color(255, 135, 45)
    if myRobot.getPixelColor(playLocation.x, playLocation.y) == playColor:
        waitForColorAndDo(playLocation.x, playLocation.y, playColor)
def spendEnergyPlayIfAvailable():
    playLocation = Location(884, 1051)
    playColor = myRobot.getPixelColor(playLocation.x, playLocation.y) # Color(255, 135, 45)
    playColorRed = playColor.getRed()
    playColorGreen = playColor.getGreen()
    playColorBlue = playColor.getBlue()
    if playColorRed > 250 and playColorGreen > 130 and playColorBlue > 40:
        waitForColorAndDo(playLocation.x, playLocation.y, playColor)

def isGameFinished():
    gameFinishedLocation = Location(807, 1065)
    gameFinishedColor = Color(21, 145, 170)
    return myRobot.getPixelColor(gameFinishedLocation.x, gameFinishedLocation.y) == gameFinishedColor


def clickAbility(num=0):
    # make sure the battle is not ended already
    backgroundLocation = Location(27, 302)
    backgroundColor = Color(248, 255, 223)
    if myRobot.getPixelColor(backgroundLocation.x, backgroundLocation.y) == backgroundColor:
        return

    abilityLocations = [Location(719, 871), Location(718, 996)]
    # check if 1st ability looks available
    if num != 2 and myRobot.getPixelColor(717, 836).getBlue() > 140:
        fastClick(abilityLocations[0].x, abilityLocations[0].y)

    if num != 1 and myRobot.getPixelColor(716, 959).getBlue() > 140:
        fastClick(abilityLocations[1].x, abilityLocations[1].y)

def clickAbilityOld(num=0):
    abilityLocations = [Location(718, 873), Location(719, 999)]
    if num == 1:
        fastClick(abilityLocations[0].x, abilityLocations[0].y)
    elif num == 2:
        fastClick(abilityLocations[1].x, abilityLocations[1].y)
    else:
        for loc in abilityLocations:
            fastClick(loc.x, loc.y)

def closeItemDescIfAny():
    itemDescLocations = [Location(1205, 500), Location(1206, 435)]
    itemDescColor = Color(255, 102, 20)
    for loc in itemDescLocations:
        if myRobot.getPixelColor(loc.x, loc.y) == itemDescColor:
            waitForColorAndDo(loc.x, loc.y, itemDescColor)
            myRobot.delay(1000)

def leaveGameResultPage():
    backgroundLocation = Location(721, 345)
    backgroundColor = Color(248, 255, 223)
    while myRobot.getPixelColor(backgroundLocation.x, backgroundLocation.y) != backgroundColor:
        myRobot.delay(1000)
        closeItemDescIfAny()
        # reconnect
        log('util.txt', 'debug', 'waiting for result bar')
    while myRobot.getPixelColor(backgroundLocation.x, backgroundLocation.y) == backgroundColor:
        leaveButtonLocation = Location(712, 1069)
        leaveButtonColor = Color(247, 255, 223)
        closeItemDescIfAny()
        if myRobot.getPixelColor(leaveButtonLocation.x, leaveButtonLocation.y) == leaveButtonColor:
            fastClick(leaveButtonLocation.x, leaveButtonLocation.y)
        else:
            type(Key.ESC)
        log('util.txt', 'debug', 'leaving result page')
        myRobot.delay(2000)
    log('util.txt', 'debug', 'left result page')

def moveLeft(interval=1000, num_steps = 10, ratio=1.0):
    myRobot.mouseMove(rightX, 354)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    for i in range(0, num_steps):
        myRobot.delay(interval/num_steps)
        myRobot.mouseMove(int(rightX-(rightX-leftX)*ratio/float(num_steps)*(i+1)), 354)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveRight(interval=1000, num_steps = 10, ratio=1.0):
    myRobot.mouseMove(leftX, 354)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    for i in range(0, num_steps):
        myRobot.delay(interval/num_steps)
        myRobot.mouseMove(int(leftX+(rightX-leftX)*ratio/float(num_steps)*(i+1)), 354)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveLeftDeprecated(step_size=50):
    myRobot.mouseMove(959, 882)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(50)      
    myRobot.mouseMove(959 - step_size/2, 882)
    myRobot.delay(50)      
    myRobot.mouseMove(959 - step_size, 882)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveRightDeprecated(step_size=50):
    myRobot.mouseMove(959, 882)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(50)
    myRobot.mouseMove(959 + step_size/2, 882)
    myRobot.delay(50)
    myRobot.mouseMove(959 + step_size, 882)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def waitForColorAndDo(
        x, y, color, 
        func_while_wait=None, arg_while_wait=[], 
        func_after_wait=None, arg_after_wait=[], 
        wait_time_period=500, wait_max_count=20,
        func_wait_too_long=None, arg_wait_too_long=[]):
    print 'x = ', x, ', y = ', y, ', color = ', color
    wait_count = 0
    while not myRobot.getPixelColor(x, y) == color:
        print myRobot.getPixelColor(x, y), x, y
        if func_while_wait != None:
            func_while_wait(*arg_while_wait)
        wait_count += 1
        if wait_count == wait_max_count:
            wait_count = 0
            if func_wait_too_long != None:
                func_wait_too_long(*arg_wait_too_long)
        myRobot.delay(wait_time_period)
    while myRobot.getPixelColor(x, y) == color:
        print myRobot.getPixelColor(x, y), x, y, 'after wait'
        if func_after_wait != None:
            func_after_wait(*arg_after_wait)
        else:
            myRobot.mouseMove(x, y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        myRobot.delay(wait_time_period)

def waitForColor(x, y, color, wait_msg,  wait_time_period=500):
    while not myRobot.getPixelColor(x, y) == color:
        print wait_msg
        myRobot.delay(wait_time_period)

def fastClick(x, y):
    myRobot.mouseMove(x, y)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)


def log(log_filename, event_type, event_message, toDelete=False):
    log_file = 'C:\\Users\\Solti\\Dropbox\\Misc\GameLogs\\' + log_filename
    log_msg = time.strftime('%d/%m/%Y') + ',' + time.strftime('%H:%M:%S') + ',' + event_type + ',' + event_message + '\n'
    open_mode = 'a'
    if toDelete:
        open_mode = 'w'
    with open(log_file, open_mode) as f:
        f.write(log_msg)

def selectGameLevel(level):
    if level == 'easy':
        easyLocation = Location(17, 397)
        easySelectedColor = Color(254, 195, 52)
        while myRobot.getPixelColor(easyLocation.x, easyLocation.y) != easySelectedColor:
            fastClick(88, 358)
            myRobot.delay(500)
    else:
        print('not implemented for "' + level + '" yet')
        exit(-1)


def selectGameLevel(level):
    if level == 'easy':
        easyLocation = Location(679, 483)
        easySelectedColor = Color(255, 210, 74)
        while myRobot.getPixelColor(easyLocation.x, easyLocation.y) != easySelectedColor:
            fastClick(770, 430)
            myRobot.delay(500)
    else:
        print('not implemented for "' + level + '" yet')
        exit(-1)

def selectWorldPlay():
    worldLocation = Location(1135, 706)
    unselectedWorldColor = Color(229, 227, 181)
    waitForColorAndDo(worldLocation.x, worldLocation.y, unselectedWorldColor)

def selectFriendPlay():
    friendLocation = Location(942, 705)
    unselectedFriendColor = Color(229, 227, 181)
    if myRobot.getPixelColor(friendLocation.x, friendLocation.y) == unselectedFriendColor:
        waitForColorAndDo(friendLocation.x, friendLocation.y, unselectedFriendColor)

def hasFriendSelected():
    unselectSelectedFriendRegion = Region(1231,213,23,815)
    unselectSelectedIcon = "unselectSelectedIcon.png"
    return unselectSelectedFriendRegion.exists(Pattern(unselectSelectedIcon).similar(0.9), 3)


def unselectedFriends():
    unselectSelectedFriendRegion = Region(1231,213,23,815)
    unselectSelectedIcon = "unselectSelectedIcon.png"
    while unselectSelectedFriendRegion.exists(Pattern(unselectSelectedIcon).similar(0.9), 3):
        unselectSelectedFriendRegion.click(Pattern(unselectSelectedIcon).similar(0.9))
        myRobot.delay(1000)
    
    
def selectFriendToPlay(friendIcon):
    selectFriendPlay()
    myRobot.delay(1000)
    chooseFriendRegion = Region(851,148,219,64)
    chooseFriendIcon = "chooseFriendIcon.png"
    chooseFriendLocation = Location(909, 179)
    chooseFriendColor = Color(255, 254, 249)
    #while not chooseFriendRegion.exists(Pattern(chooseFriendIcon).similar(0.9)):
    while myRobot.getPixelColor(chooseFriendLocation.x, chooseFriendLocation.y) != chooseFriendColor:
        # click play
        myRobot.delay(2000)
        playLocation = Location(908, 1067)
        playColor = Color(255, 135, 45)
        if myRobot.getPixelColor(playLocation.x, playLocation.y) == playColor:
            fastClick(playLocation.x, playLocation.y)
        myRobot.delay(1000)
    myRobot.delay(1500)

    # entered friend list
    playLocation = Location(908, 1067)
    playColor = Color(255, 135, 45)
    #myRobot.delay(1000)
    if myRobot.getPixelColor(playLocation.x, playLocation.y) == playColor:
        unselectedFriends()
        myRobot.delay(1000)
 

    friendRegion = Region(667,212,267,808)
    count = 0
    while not friendRegion.exists(Pattern(friendIcon).similar(0.9)):
        myRobot.delay(1000)
        count += 1
        if count == 2:
            return False

    friendRegion.click(Pattern(friendIcon).similar(0.9))
    myRobot.delay(1000)
    return hasFriendSelected()

def goBackToHomePage():
    homePageLocation = Location(961, 1024)
    homePageColor = Color(152, 169, 4)
    while myRobot.getPixelColor(homePageLocation.x, homePageLocation.y) != homePageColor:
        type(Key.ESC)
        myRobot.delay(3000)
    myRobot.delay(1000)

def leaveStageDetailPage():
    stageTitleBarLocation = Location(950, 180)
    stageTitleBarColor = Color(42, 155, 175)
    stageLeavingAarowLocation = Location(706, 1063)
    stageLeavingAarowColor = Color(247, 255, 223)
    if myRobot.getPixelColor(stageTitleBarLocation.x, stageTitleBarLocation.y) == stageTitleBarColor and \
            myRobot.getPixelColor(stageLeavingAarowLocation.x, stageLeavingAarowLocation.y) == stageLeavingAarowColor:
        waitForColorAndDo(
                stageTitleBarLocation.x, stageTitleBarLocation.y, stageTitleBarColor,
                func_after_wait=fastClick, arg_after_wait=[stageLeavingAarowLocation.x, stageLeavingAarowLocation.y],
                wait_time_period=1000)


def clickBackupIfAvailable():
    backupLocation = Location(1005, 856)
    backupColor = myRobot.getPixelColor(backupLocation.x, backupLocation.y) # Color(255, 135, 48)
    hasBackup = backupColor.getRed() > 250 and backupColor.getGreen() > 130 and backupColor.getBlue() > 40
    if hasBackup:
        # first choose the plan
        bestPlaneLocation = Location(775, 633)
        util.fastClick(bestPlaneLocation.x, bestPlaneLocation.y)
        myRobot.delay(700)
        waitForColorAndDo(backupLocation.x, backupLocation.y, backupColor)


def handleOpeningNoise():
    log('util.txt', 'launch', 'enter handleOpeningNoise')
    noiseRegions = [
        Region(841,715,235,79),
        Region(1129,98,143,177),
        Region(956,614,244,105),
        Region(1170,97,71,72)
    ]
    noiseIcons = [
         "continueIcon.png",
         "announcementCloseIcon.png",
         "1539211321242.png",
         "1540132313595.png"
    ]
    for i in range(0, len(noiseIcons)):
        if noiseRegions[i].exists(Pattern(noiseIcons[i]).similar(0.9)):
            noiseRegions[i].click(Pattern(noiseIcons[i]).similar(0.9))
            myRobot.delay(3000)
    log('util.txt', 'launch', 'finish handleOpeningNoise')


def closeHawk():
    HawkRegion = Region(7,101,1796,378)
    HawkIcon = "HawkIcon.png"
    log('util.txt', 'close', 'trying to close Hawk')
    while not HawkRegion.exists(HawkIcon):
        log('util.txt', 'close', 'click close x')
        hawkCloseXLocation = Location(517, 10)
        fastClick(hawkCloseXLocation.x, hawkCloseXLocation.y)
        myRobot.delay(10000)
    log('util.txt', 'close', 'Hawk closed')    



def launchHawk():
    gameIconRegion = Region(7,101,1796,378)
    gmaeIcon = "gmaeIcon.png"
    while not gameIconRegion.exists(Pattern(gmaeIcon).similar(0.9)):
        log('util.txt', 'launch', 'waiting for hawk icon')
        myRobot.delay(5000)
    
    while gameIconRegion.exists(Pattern(gmaeIcon).similar(0.9)):
        log('util.txt', 'launch', 'click hawk icon')
        gameIconRegion.click(Pattern(gmaeIcon).similar(0.9))
        myRobot.delay(5000)

    # wait for hawk menu
    homePageLocation = Location(961, 1024)
    homePageColor = Color(152, 169, 4)
    while myRobot.getPixelColor(homePageLocation.x, homePageLocation.y) != homePageColor:
        log('util.txt', 'launch', 'wait for reaching home page')
        handleOpeningNoise()
        myRobot.delay(5000)
    log('util.txt', 'launch', 'arrived home page')


if __name__ == "__main__":
    clickBackupIfAvailable()
    exit(0)
    targetLocation = Location(1005, 856)

    hover(targetLocation)
    print(targetLocation)
    print(myRobot.getPixelColor(targetLocation.x, targetLocation.y))
    myRobot.delay(3000)
