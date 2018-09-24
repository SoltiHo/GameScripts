import java.awt.Color as Color
import Utilities as util
from Utilities import myRobot
from sikuli import *
reload(util)

def hasMegaAds():
    megaAdsLocation = Location(1237, 272)
    megaAdsColor = Color(255, 102, 20)
    return myRobot.getPixelColor(megaAdsLocation.x, megaAdsLocation.y) == megaAdsColor


def hasSmallAds():
    hasDailyRewardLocation = Location(1117, 1030)
    hasDailyRewardColor1 = Color(255, 102, 20)
    hasDailyRewardColor2 = Color(178, 102, 231)

    theColorSeen = None
    if myRobot.getPixelColor(hasDailyRewardLocation.x, hasDailyRewardLocation.y) == hasDailyRewardColor1:
        theColorSeen = hasDailyRewardColor1
    elif myRobot.getPixelColor(hasDailyRewardLocation.x, hasDailyRewardLocation.y) == hasDailyRewardColor2:
        theColorSeen = hasDailyRewardColor2
    else:
        return False

    # enter daily reward list
    util.waitForColorAndDo(hasDailyRewardLocation.x, hasDailyRewardLocation.y, theColorSeen)
    # find "watch"
    watchRegion = Region(1093,219,122,790)
    watchIcon = "watchIcon.png"

    if not watchRegion.exists(Pattern(watchIcon).similar(0.9), 5):
        collectDailyRewardIfAny()
        # in the daily reward menu, need to go back
        goBackToHomePage()
        return False
    else:
        return True
    

def collectDailyRewardIfAny():
    util.log('WatchAds.txt', 'DailyReward', 'collecting daily reward')
    rewardRegion = Region(1105,257,105,691)
    rewardIcon = "rewardIcon.png"

    notFoundCount = 0
    while True:
        if rewardRegion.exists(Pattern(rewardIcon).similar(0.9), 5):
            rewardRegion.click(Pattern(rewardIcon).similar(0.9))
            notFoundCount = 0
            myRobot.delay(5000)
        else:
            notFoundCount += 1
            # check if it is daily login reward
            loginRewardLocation = Location(902, 1033)
            loginRewardColor = Color(255, 134, 46)
            if myRobot.getPixelColor(loginRewardLocation.x, loginRewardLocation.y) == loginRewardColor:
                util.fastClick(loginRewardLocation.x, loginRewardLocation.y)
                myRobot.delay(3000)
                confirmRewardLocation = Location(1089, 483)
                util.fastClick(confirmRewardLocation.x, confirmRewardLocation.y)
                myRobot.delay(3000)

                # make sure closing completed
                closeLoginRewardMenuLocation = Location(1209, 135)
                rewardListLocation = Location(739, 171)
                rewardListColor = Color(0, 156, 177)
                while myRobot.getPixelColor(rewardListLocation.x, rewardListLocation.y) != rewardListColor:
                    util.fastClick(closeLoginRewardMenuLocation.x, closeLoginRewardMenuLocation.y)
                    myRobot.delay(2000)
                myRobot.delay(2000)
                notFoundCount = 0
            if notFoundCount == 3:
                break
            myRobot.delay(2000)


def watchSmallAdsAndReturnHome():
    util.log('WatchAds.txt', 'DailyReward', 'watching daily reward ads')
    watchRegion = Region(1093,219,122,790)
    watchIcon = "watchIcon.png"
    while watchRegion.exists(Pattern(watchIcon).similar(0.9)):
        watchRegion.click(Pattern(watchIcon).similar(0.9))
        myRobot.delay(2000)
    waitForAdsToEndAndClose()

    # collect reward and go home
    collectDailyRewardIfAny()
    goBackToHomePage()
    

def waitForAdsToEndAndClose():   
    myRobot.delay(60*1000)  # 2 min ads time
    myRobot.delay(60*1000)
    closeAds_x()
    myRobot.delay(10000)

    # do not wait for Ads to end, just click it
    #clickAdsLocation = Location(957, 612)
    #myRobot.delay(5000)
    #util.fastClick(clickAdsLocation.x, clickAdsLocation.y)
    #myRobot.delay(5000)
    #closeAds_clickThrough()


def watchMegaAds():
    util.log('WatchAds.txt', 'MegaReward', 'watching mega ads')
    megaAdsLocation = Location(1237, 272)
    megaAdsColor = Color(255, 102, 20)
    util.waitForColorAndDo(megaAdsLocation.x, megaAdsLocation.y, megaAdsColor)

    watchLocation = Location(1099, 729)
    watchColor = Color(150, 100, 195)
    util.waitForColorAndDo(watchLocation.x, watchLocation.y, watchColor)

    waitForAdsToEndAndClose()
    openChest()
    goBackToHomePage()


def adsClosed():
    crystalLocation = Location(1085, 87)
    crystalColor = Color(27, 224, 210)
    if myRobot.getPixelColor(crystalLocation.x, crystalLocation.y) == crystalColor:
        return True
    else:
        return False

def closeAds_clickThrough():
    # click through
    util.log('WatchAds.txt', 'CloseAds', 'click through close ads')
    tabClosedLocation = Location(563, 25)
    tabClosedColor = Color(88, 90, 108)
    closeTabLocation = Location(719, 10)
    while myRobot.getPixelColor(tabClosedLocation.x, tabClosedLocation.y) != tabClosedColor:
        util.fastClick(closeTabLocation.x, closeTabLocation.y)
        myRobot.delay(5000)

def closeAds_x():
    util.log('WatchAds.txt', 'CloseAds', 'trying to close ads')
    attempCount = 0
    while True:
        attempCount += 1
        possibleCloseAdsLocations = [
            Location(1246, 79),
            Location(1185, 293),
            Location(1824, 129),
        ]
        for loc in possibleCloseAdsLocations:
            util.fastClick(loc.x, loc.y)
            myRobot.delay(3000)
            if adsClosed():
                break  # break the for loop
        # to break the while loop
        if adsClosed():
            break
        if attempCount == 20:
            closeAds_clickThrough()
            attempCount = 0
    myRobot.delay(5000)



def openChest():
    util.log('WatchAds.txt', 'MegaReward', 'opening chest')
    openLocation = Location(1099, 729)
    openColor = Color(255, 134, 45)
    util.waitForColorAndDo(openLocation.x, openLocation.y, openColor)
    myRobot.delay(3000)
    util.fastClick(1139, 361)
    myRobot.delay(500)
    util.fastClick(1139, 361)
    myRobot.delay(2000)
    
    yourRewardLocation = Location(1100, 415)
    yourRewardColor = Color(255, 102, 20)
    util.waitForColorAndDo(yourRewardLocation.x, yourRewardLocation.y, yourRewardColor)
    myRobot.delay(1000)


def closeHawk():
    HawkRegion = Region(11,112,621,167)
    HawkIcon = "HawkIcon.png"
    util.log('WatchAds.txt', 'close', 'trying to close Hawk')
    while not HawkRegion.exists(HawkIcon):
        util.log('WatchAds.txt', 'close', 'click close x')
        hawkCloseXLocation = Location(517, 10)
        util.fastClick(hawkCloseXLocation.x, hawkCloseXLocation.y)
        myRobot.delay(10000)
    util.log('WatchAds.txt', 'close', 'Hawk closed')

def launchHawk():
    HawkRegion = Region(11,112,621,167)
    HawkIcon = "HawkIcon.png"
    while not HawkRegion.exists(HawkIcon):
        util.log('WatchAds.txt', 'launch', 'waiting for HawkIcon')
        myRobot.delay(5000)
    HawkRegion.click(HawkIcon)
    myRobot.delay(10000)
    goBackToHomePage()
    util.log('WatchAds.txt', 'launch', 'launch completed')
    

def goBackToHomePage():
    util.log('WatchAds.txt', 'Go Home', 'trying to get home')
    homePageLocation = Location(961, 1024)
    homePageColor = Color(152, 169, 4)
    while myRobot.getPixelColor(homePageLocation.x, homePageLocation.y) != homePageColor:
        type(Key.ESC)
        myRobot.delay(3000)
    myRobot.delay(1000)
    

def checkAdsOneRound():
    # start checking ads
    util.log('WatchAds.txt', 'Monitor', 'Checking for Ads')
    if hasMegaAds():
        watchMegaAds()
        util.log('WatchAds.txt', 'MegaReward', 'finished watching mega ads')
        myRobot.delay(10000)
    if hasSmallAds():
        watchSmallAdsAndReturnHome()
        util.log('WatchAds.txt', 'DailyReward', 'finished watching daily ads')
        myRobot.delay(10000)


def monitorAds():
    while True:
        # launch the game
        launchHawk()
        checkAdsOneRound() 
        # close hawk
        closeHawk()

        for i in range(0, 10):  # check every 10 min
            myRobot.delay(60*1000)  # 1 min
        
        
            

if __name__ == "__main__":
    hasSmallAds()
    exit(1)
    #collectDailyRewardIfAny()
    #openChest()
    #print(hasMegaAds())
    #goBackToHomePage()
    monitorAds()
