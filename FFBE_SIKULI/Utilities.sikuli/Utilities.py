import java.awt.Robot as JRobot
import java.awt.Color as Color

UNIT_CENTER_LOCATIONS = [
        Location(823, 739),
        Location(818, 845),
        Location(818, 950),
        Location(1105, 741),
        Location(1101, 846),
        Location(1104, 950)]
MAGIC_MENU_REGION = Region(683,686,548,290)
def isAttacking():
    myRobot = JRobot()
    currentColor = myRobot.getPixelColor(1080, 1052)
    notAttackingColor = Color(0x00,0x41,0x6F)
    # if not attacking: java.awt.Color[r=0,g=65,b=111]
    # if attacking: java.awt.Color[r=0,g=25,b=44]
    if  myRobot.getPixelColor(1080, 1052).getRGB() == notAttackingColor.getRGB():
        print "ohohohohoh not attacking"
        return False
    else:
        print "seems attacking"
        return True

def isBloodLowerThanHalf(unitNum): #unitNum is 1 based
    HP_Half_Locations = [Location(788, 775), Location(786, 879), Location(786, 983),
            Location(1072, 776), Location(1073, 879), Location(1074, 983)]
    targetUnit = HP_Half_Locations[unitNum - 1]
    myRobot = JRobot()
    if myRobot.getPixelColor(targetUnit.x, targetUnit.y).getGreen() < 10:
        #print "unit ", unitNum, " needs help"
        return True
    else:
        #print "unit ", unitNum, " is fine"
        return False

def defense(unitNum): #unitNum is 1 based
    mouseMove(UNIT_CENTER_LOCATIONS[unitNum - 1])
    mouseDown(Button.LEFT)
    mouseMove(0, 100)
    mouseUp(Button.LEFT)

def openMagicMenu(unitNum): #unitNum is 1 based
    mouseMove(UNIT_CENTER_LOCATIONS[unitNum - 1])
    mouseDown(Button.LEFT)
    mouseMove(100, 0)
    mouseUp(Button.LEFT)

def scrollMenuDown():
    mouseMove(Location(893, 957))
    mouseDown(Button.LEFT)
    mouseMove(0, -270)
    mouseUp(Button.LEFT)

def findTheMagic(targetMagic):
    # start looking
    scrollCount = 0
    MAX_SCROLL_COUNT = 5
    while not MAGIC_MENU_REGION.exists(targetMagic):
        scrollCount = scrollCount + 1
        if scrollCount > MAX_SCROLL_COUNT:
            # not found
            return
        scrollMenuDown()
    findResult = MAGIC_MENU_REGION.find(targetMagic)
    if findResult != None: 
        return findResult.getTarget()
    else:    
        return None

def findMagicMiddleCure(unitNum):
    openMagicMenu(3)

    targetMagic = "1477172791051.png"
    result = findTheMagic(targetMagic)
    if result == None:
        # can't find, return to main menu
        click(Location(1180, 1030))
    return result

def isAnyoneHPLow():
    if isBloodLowerThanHalf(1):
        return True
    if isBloodLowerThanHalf(2):
        return True
    if isBloodLowerThanHalf(3):
        return True
    if isBloodLowerThanHalf(4):
        return True
    if isBloodLowerThanHalf(5):
        return True
    if isBloodLowerThanHalf(6):
        return True

if isAnyoneHPLow():
    print "need magic"
else:
    print "everyone okay"
    