import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)
myRobot = JRobot()

def isStillRunning():
    FFBEColor = Color(239, 172, 194) # (1169, 200)
    if myRobot.getPixelColor(1169, 200) == FFBEColor:
        return False
    return True

def recover():
    Utilities.log('LBDroidXLog.txt', 'recover', 'recover')
    print "recover"
    #myRobot.delay(10000)
    # first, go back to FFBE
    Utilities.fastClick(1169, 200)
    myRobot.delay(5000)
    # wait for combat screen
    combatBackgroundColor = Color(166, 63, 50) # (1126, 161)
    while myRobot.getPixelColor(1126, 161) != combatBackgroundColor:
        Utilities.fastClick(983, 827)
        print "waiting for combat background"
        myRobot.delay(3000)

    # pause speedup
    myRobot.delay(1000)
    Utilities.fastClick(1247, 163)
    myRobot.delay(1000)
    Utilities.fastClick(1247, 163)
    myRobot.delay(1000)

    # restart speedup
    Utilities.fastClick(1247, 163)
    myRobot.delay(1500)
    Utilities.fastClick(996, 82)
    myRobot.delay(2000)

    # click Auto
    Utilities.fastClick(768, 996)
    Utilities.log('LBDroidXLog.txt', 'recover', 'recover completed')
    

def main():
    while True:
        if not isStillRunning():
            recover()
        myRobot.delay(60000)

if __name__ == "__main__":
    main()
    #recover()
    