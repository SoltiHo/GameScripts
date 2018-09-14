import java.awt.Color as Color
import Utilities as util
from Utilities import myRobot
reload(util)

def hasMegaAds():
    megaAdsLocation = Location(1238, 274)
    megaAdsColor = Color(255, 102, 20)
    return myRobot.getPixelColor(megaAdsLocation.x, megaAdsLocation.y) == megaAdsColor


def hasSmallAds():
    hasDailyRewardLocation = Location(1115, 1029)
    hasDailyRewardColor = Color(255, 102, 20)
    if myRobot.getPixelColor(hasDailyRewardLocation.x, hasDailyRewardLocation.y) != hasDailyRewardColor:
        return False

    # enter daily reward list
    util.waitForColorAndDo(hasDailyRewardLocation.x, hasDailyRewardLocation.y, hasDailyRewardColor)
    # find "watch"
    watchRegion = Region(1093,219,122,790)
    watchIcon = "watchIcon.png"

    if not watchRegion.exists(Pattern(watchIcon).similar(0.9), 5):
        return False
    else:
        return True
    

def collectDailyRewardIfAny():
    rewardRegion = Region(1105,257,105,691)
    rewardIcon = "rewardIcon.png"
    while rewardRegion.exists(Pattern(rewardIcon).similar(0.9), 5):
        rewardRegion.click(Pattern(rewardIcon).similar(0.9))
        myRobot.delay(3000)


def watchSmallAdsAndReturnHome():
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
    megaAdsLocation = Location(1238, 274)
    megaAdsColor = Color(255, 102, 20)
    util.waitForColorAndDo(megaAdsLocation.x, megaAdsLocation.y, megaAdsColor)

    watchLocation = Location(1094, 731)
    watchColor = Color(150, 100, 195)
    util.waitForColorAndDo(watchLocation.x, watchLocation.y, watchColor)

    waitForAdsToEndAndClose()
    openChest()
    goBackToHomePage()


def closeAds():
    closeIconRegion = Region(693,48,547,258)
    closeIcon = "closeIcon.png"
    closeIconRegion.click(Pattern(closeIcon).similar(0.9))


def openChest():
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
    homePageLocation = Location(961, 1024)
    homePageColor = Color(152, 169, 4)
    util.waitForColorAndDo(homePageLocation.x, homePageLocation.y, homePageColor)
    myRobot.delay(1000)
    

def monitorAds():
    while True:
        if hasMegaAds():
            watchMegaAds()
            myRobot.delay(3000)
        if hasSmallAds():
            watchSmallAdsAndReturnHome()
        
            

if __name__ == "__main__":
    collectDailyRewardIfAny()
    #monitorAds()
