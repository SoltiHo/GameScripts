import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
from sikuli import *

UNIT_CENTER_LOCATIONS = [
        Location(823, 739),
        Location(818, 845),
        Location(818, 950),
        Location(1105, 741),
        Location(1101, 846),
        Location(1104, 950)]

UNIT_SWORD_REGIONS = [
        Region(673,668,43,46),
        Region(672,769,44,48),
        Region(671,875,44,44),
        Region(958,667,42,46),
        Region(958,768,43,50),
        Region(956,890,45,49)]

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

def closeMagicMenu():
    click(Location(1175, 1012))

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
    openMagicMenu(unitNum)

    targetMagic = "1477172791051.png"
    result = findTheMagic(targetMagic)
    if result == None:
        # can't find, return to main menu
        click(Location(1180, 1030))
    return result

def doMiddleCureIfNeeded():
    if isAnyoneHPLow():
        curerNum = doMiddleCureIfAvailable();
        if curerNum == 0:
            print "Warning!!! need cure but not available. Exiting"
            exit(1)

def doMiddleCureIfAvailable():
    # return the unitNum who does the middle cure.  0 means not found
    curerNum = 0
    result = None
    while True:
        if isUnitAlive(1):
            result = findMagicMiddleCure(1)
        if result != None:
            curerNum = 1
            break
        else:
            print "uint 1 can't cure"

        if isUnitAlive(2):
            result = findMagicMiddleCure(2)
        if result != None:
            curerNum = 2
            break
        else:
            print "uint 2 can't cure"

        if isUnitAlive(3):
            result = findMagicMiddleCure(3)
        if result != None:
            curerNum = 3
            break
        else:
            print "uint 3 can't cure"

        if isUnitAlive(4):
            result = findMagicMiddleCure(4)
        if result != None:
            curerNum = 4
            break
        else:
            print "uint 4 can't cure"
        
        if isUnitAlive(5):
            result = findMagicMiddleCure(5)
        if result != None:
            curerNum = 5
            break
        else:
            print "uint 5 can't cure"
            
    if curerNum != 0:
        click(result)
        wait(0.5)
        click(UNIT_CENTER_LOCATIONS[curerNum - 1])
    return curerNum
    
def isUnitAlive(unitNum):
    swordRegion = UNIT_SWORD_REGIONS[unitNum - 1]
    if swordRegion.exists("1477850868137.png"):
        print "unit ", unitNum, " is alive"
        return True
    else:
        print "unit ", unitNum, " died"
        return False
    
def isAnyoneHPLow():
    if isBloodLowerThanHalf(1) and isUnitAlive(1):
        print "unit 1 need cure"
        return True
    if isBloodLowerThanHalf(2) and isUnitAlive(2):
        print "unit 2 need cure"
        return True
    if isBloodLowerThanHalf(3) and isUnitAlive(3):
        print "unit 3 need cure"
        return True
    if isBloodLowerThanHalf(4) and isUnitAlive(4):
        print "unit 4 need cure"
        return True
    if isBloodLowerThanHalf(5) and isUnitAlive(5):
        print "unit 5 need cure"
        return True
    if isBloodLowerThanHalf(6) and isUnitAlive(6):
        print "unit 6 need cure"
        return True

def manuallyKickOff():
    myRobot = JRobot()
    myRobot.mouseMove(823,739)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(818,845)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(818,950)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1105,741)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1101,846)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1104,950)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot = JRobot()
    myRobot.mouseMove(823,739)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(818,845)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(818,950)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1105,741)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1101,846)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(1104,950)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def summonIfAvailable(unitNum):
    if not isUnitAlive(unitNum):
        return False
    summonRegion = Region(978,712,52,39)
    openMagicMenu(unitNum)
    wait(0.5)
    summoned = False
    if summonRegion.exists("1477852401573.png"):
        click(Location(1181, 1028)) # go back
    else:
        summoned = True
        click(Location(1086, 734))
    wait(0.5)
    return summoned        

def isLBAvailable(toClick):
    myRobot = JRobot()
    # LB not available: [r=56,g=26,b=0]
    # available: [r=112,g=53,b=0]
    currentColor = myRobot.getPixelColor(906, 707)
    print currentColor
    if  myRobot.getPixelColor(906, 707).getRed() >= 100:
        print "LB available"
        if toClick == True:
            click(Location(906,707))
        return True
    else:
        print "LB not ready"
        return False

myRobot = JRobot() 
print myRobot.getPixelColor(1052, 1022)