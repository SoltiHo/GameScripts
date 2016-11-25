import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
from sikuli import *

myRobot = JRobot()
UNIT_CENTER_LOCATIONS = [
        Location(823, 739),
        Location(818, 845),
        Location(818, 950),
        Location(1105, 741),
        Location(1101, 846),
        Location(1104, 950)]

UNIT_LB_TOP_LOCATIONS = [
        Location(942, 724),
        Location(938, 833),
        Location(940, 941),
        Location(1241, 724),
        Location(1238, 834)]
UNIT_SWORD_REGIONS = [
        Region(657,640,52,56),
        Region(657,752,48,54),
        Region(657,861,49,50),
        Region(957,645,47,47),
        Region(959,753,44,48),
        Region(958,860,45,49)]

MAGIC_MENU_REGION = Region(683,686,548,290)

MAGIC_MENU_REGION_BS = Region(670,662,576,299)


def isAttacking():
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

def isAttacking_BS():
    NotAttackingColor = Color(0x00,0x77,0x93)
    if myRobot.getPixelColor(1052, 1022) == NotAttackingColor:
        print "ohohohohoh not attacking"
        return False
    else:
        print "seems attacking"
        return True



def isBloodLowerThanHalf(unitNum): #unitNum is 1 based
    HP_Half_Locations = [Location(777, 759), Location(778, 868), Location(774, 978),
            Location(1076, 759), Location(1076, 868), Location(1076, 977)]
    targetUnit = HP_Half_Locations[unitNum - 1]
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
    moveRegion = Region(917,671,44,292)
    myRobot.mouseMove(893,957)
    moveRegion.mouseDown(Button.LEFT)
    moveRegion.mouseMove(0, -270)
    moveRegion.mouseUp(Button.LEFT)

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

def findTheMagic_BS(targetMagic):
    # start looking
    scrollCount = 0
    MAX_SCROLL_COUNT = 5
    start = time.time()
    while not MAGIC_MENU_REGION_BS.exists(targetMagic):
        print "search took ", time.time() - start
        scrollCount = scrollCount + 1
        if scrollCount > MAX_SCROLL_COUNT:
            # not found
            return
        scrollMenuDown()
        start = time.time()
    findResult = MAGIC_MENU_REGION_BS.find(targetMagic)
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
    summonRegion = Region(968,675,79,87)
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

def isLBAvailable_BS(toClick):
    if  myRobot.getPixelColor(833, 687).getRed() >= 100:
        print "LB available"
        if toClick == True:
            click(Location(833, 687))
        return True
    else:
        print "LB not ready"
        return False

def moveAround():
    MoveRegion = Region(859,451,231,183)
    #dragDrop(MoveRegion, MoveRegion.offset(100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(-100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(0,100))
    #dragDrop(MoveRegion, MoveRegion.offset(0,-100))
    myRobot.mouseMove(961, 494)
    MoveRegion.mouseDown(Button.LEFT)
    MoveRegion.mouseMove(0, -270)
    myRobot.delay(500)
    MoveRegion.mouseMove(0, 540)
    myRobot.delay(500)
    MoveRegion.mouseUp(Button.LEFT)
    
def moveUp():
    myRobot.mouseMove(960, 449)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveDown():
    myRobot.mouseMove(963, 554)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveLeft():
    myRobot.mouseMove(912, 519)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveRight():
    myRobot.mouseMove(1007, 516)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def isInBattle():
    # (BS) Not in battle color = java.awt.Color[r=255,g=255,b=255]
    if myRobot.getPixelColor(1231, 998).getRed() > 230:
        return False
    else:
        return True

def lookHavingLB(unitNum):
    if myRobot.getPixelColor( \
            UNIT_LB_TOP_LOCATIONS[unitNum - 1].getX(), \
            UNIT_LB_TOP_LOCATIONS[unitNum - 1].getY()).getRed() > 150:
        print "unit ", unitNum, " looks having LB"
        return True
    else:
        print "unit ", unitNum, " no LB"   
        return False



print myRobot.getPixelColor(1135, 1030)