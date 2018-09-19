import java.awt.Color as Color
import Utilities as util
from Utilities import myRobot
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
        # in the daily reward menu, need to go back
        goBackToHomePage()
        return False
    else:
        return True
    

def collectDailyRewardIfAny():
    util.log('WatchAds.txt', 'DailyReward', 'collecting daily reward')
    rewardRegion = Region(1105,257,105,691)
    rewardIcon = "rewardIcon.png"
    while rewardRegion.exists(Pattern(rewardIcon).similar(0.9), 5):
        rewardRegion.click(Pattern(rewardIcon).similar(0.9))
        myRobot.delay(5000)


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
    closeAds()


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

def closeAds():
    util.log('WatchAds.txt', 'CloseAds', 'trying to close ads')
    while True:
        topRightCloseLocation = Location(1246, 79)
        util.fastClick(topRightCloseLocation.x, topRightCloseLocation.y)
        myRobot.delay(3000)
        if adsClosed():
            break
        topRightCloseLocation2 = Location(1185, 293)
        util.fastClick(topRightCloseLocation2.x, topRightCloseLocation2.y)
        myRobot.delay(3000)
        if adsClosed():
            break
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


def goBackToHomePage():
    util.log('WatchAds.txt', 'Go Home', 'trying to get home')
    homePageLocation = Location(961, 1024)
    homePageColor = Color(152, 169, 4)
    while myRobot.getPixelColor(homePageLocation.x, homePageLocation.y) != homePageColor:
        type(Key.ESC)
        myRobot.delay(3000)
    myRobot.delay(1000)
    

def monitorAds():
    while True:
        util.log('WatchAds.txt', 'Monitor', 'Checking for Ads')
        if hasMegaAds():
            watchMegaAds()
            util.log('WatchAds.txt', 'MegaReward', 'finished watching mega ads')
            myRobot.delay(10000)
        if hasSmallAds():
            watchSmallAdsAndReturnHome()
            util.log('WatchAds.txt', 'DailyReward', 'finished watching daily ads')
            myRobot.delay(10000)
        for i in range(0, 10):  # check every 10 min
            myRobot.delay(60*1000)  # 1 min
        
            

if __name__ == "__main__":
    #openChest()
    #print(hasMegaAds())
    #goBackToHomePage()
    monitorAds()
