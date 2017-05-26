import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import time
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
    center_x = UNIT_CENTER_LOCATIONS[unitNum - 1].getX()
    center_y = UNIT_CENTER_LOCATIONS[unitNum - 1].getY()
    myRobot.mouseMove(center_x, center_y)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(center_x, center_y + 100)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

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

def scrollMenuUp_fast():
    myRobot.mouseMove(935, 685)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(935, 735)
    myRobot.delay(100)
    myRobot.mouseMove(935, 785)
    myRobot.delay(100)
    myRobot.mouseMove(935, 835)
    myRobot.delay(100)
    myRobot.mouseMove(935, 885)
    #myRobot.delay(150)
    myRobot.mouseMove(935, 935)
    myRobot.delay(100)
    myRobot.mouseMove(935, 1003)
    myRobot.delay(200)
    myRobot.mouseMove(935, 1002)
    myRobot.delay(350)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def scrollMenuDown_fast():
    myRobot.mouseMove(935, 955)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(935, 905)
    myRobot.delay(100)
    myRobot.mouseMove(935, 855)
    myRobot.delay(100)
    myRobot.mouseMove(935, 805)
    myRobot.delay(100)
    myRobot.mouseMove(935, 755)
    #myRobot.delay(150)
    myRobot.mouseMove(935, 705)
    myRobot.delay(100)
    myRobot.mouseMove(935, 655)
    myRobot.delay(200)
    myRobot.mouseMove(935, 656)
    myRobot.delay(350)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

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

def isUnitAliveFast(unitNum):
    # Marker
    UNIT_SWORD_COLOR = [
            Color(201,197,194), # 683, 669
            Color(141,133,118), # 681, 779
            Color(141,134,120), # 681, 888
            Color(103, 90, 72), # 980, 669
            Color(243,243,243)  # 982, 777 
            ]
    UNIT_SWORD_X = [
            683, 
            681, 
            681, 
            980, 
            982, 
            ]
    UNIT_SWORD_Y = [
            669,
            779,
            888,
            669,
            777
            ]
    if myRobot.getPixelColor(
            UNIT_SWORD_X[unitNum - 1],
            UNIT_SWORD_Y[unitNum - 1]) == UNIT_SWORD_COLOR[unitNum - 1]:
        return True
    else:
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
    return False

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
    if not lookAbleToSummon():
        return False
    if not isUnitAlive(unitNum):
        return False
    summonRegion = Region(968,675,79,87)
    openMagicMenu(unitNum)
    wait(0.5)
    summoned = False
    summonNotAvailableColor = Color(206,111,111) # (998, 720)
    if myRobot.getPixelColor(998, 720) == summonNotAvailableColor:
        click(Location(1181, 1028)) # go back
    else:
        summoned = True
        click(Location(1086, 734))
    myRobot.delay(1000)
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

def moveAround(direction):
    MoveRegion = Region(859,451,231,183)
    #dragDrop(MoveRegion, MoveRegion.offset(100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(-100,0))
    #dragDrop(MoveRegion, MoveRegion.offset(0,100))
    #dragDrop(MoveRegion, MoveRegion.offset(0,-100))
    myRobot.mouseMove(961, 494)
    MoveRegion.mouseDown(Button.LEFT)
    if direction == 'UpDown':
        MoveRegion.mouseMove(0, -270)
    else:
        MoveRegion.mouseMove(-270, 0)        
    myRobot.delay(500)
    if direction == 'UpDown':
        MoveRegion.mouseMove(0, 540)
    else:
        MoveRegion.mouseMove(540, 0)
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

def MoveUpAndCheckBattle(battleFunc, battleFuncArg=[], isBoundary=False, detectBattle=True):
    print isBoundary
    move_func = moveUp
    if isBoundary:
        move_func = boundaryGoUp
    move_func()
    myRobot.delay(200)
    if detectBattle and isInBattle():
        myRobot.delay(1000)
        battleFunc(*battleFuncArg)
        myRobot.delay(1000)
        move_func()
        return 1
    return 0

def MoveDownAndCheckBattle(battleFunc, battleFuncArg=[], isBoundary=False, detectBattle=True):
    print isBoundary
    move_func = moveDown
    if isBoundary:
        move_func = boundaryGoDown
    move_func()
    myRobot.delay(200)
    if detectBattle and isInBattle():
        myRobot.delay(1000)
        battleFunc(*battleFuncArg)
        myRobot.delay(1000)
        move_func()
        return 1
    return 0

def MoveLeftAndCheckBattle(battleFunc, battleFuncArg=[], isBoundary=False, detectBattle=True):
    print isBoundary
    move_func = moveLeft
    if isBoundary:
        move_func = boundaryGoLeft
    move_func()
    myRobot.delay(200)
    if detectBattle and isInBattle():
        myRobot.delay(1000)
        battleFunc(*battleFuncArg)
        myRobot.delay(1000)
        move_func()
        return 1
    return 0

def MoveRightAndCheckBattle(battleFunc, battleFuncArg=[], isBoundary=False, detectBattle=True):
    print isBoundary
    move_func = moveRight
    if isBoundary:
        move_func = boundaryGoRight
    move_func()
    myRobot.delay(200)
    if detectBattle and isInBattle():
        myRobot.delay(1000)
        battleFunc(*battleFuncArg)
        myRobot.delay(1000)
        move_func()
        return 1
    return 0

def isInBattle():
    # (BS) Not in battle color = java.awt.Color[r=255,g=255,b=255]
    inBattleColor = Color(255, 255, 255)
    if myRobot.getPixelColor(1231, 998) == inBattleColor:
        return False
    else:
        myRobot.delay(500)
        if myRobot.getPixelColor(1231, 998) == inBattleColor:
            return False
        return True

def isInBattle_DuOS():
    mapColor = Color(3, 81, 176) # (1099,1031)
    if myRobot.getPixelColor(1099, 1031) == mapColor:
        return False
    else:
        return True

def lookAbleToSummon():
    noSummonColor = Color(7,21,27) # (1252, 645)
    return myRobot.getPixelColor(1252,645) != noSummonColor

def lookAbleToSummon_DuOS():
    noSummonColor = Color(5,20,25) # (1237, 667)
    return myRobot.getPixelColor(1237,667) != noSummonColor

def lookHavingLB(unitNum):
    if myRobot.getPixelColor( \
            UNIT_LB_TOP_LOCATIONS[unitNum - 1].getX(), \
            UNIT_LB_TOP_LOCATIONS[unitNum - 1].getY()).getRed() > 150:
        print "unit ", unitNum, " looks having LB"
        return True
    else:
        print "unit ", unitNum, " no LB"   
        return False

def selectFollowerAndLaunch(selectFollower):
    followerColor = Color(145,60,32) # (1015,223)
    if selectFollower:
        waitForColorAndDo(1015, 223, followerColor, 
                func_after_wait=fastClick, arg_after_wait=(810, 404))
    else:
        def waitAndSelectNoFollower():
            myRobot.delay(500)
            func_after_wait=selectStranger()
        #followerColor = Color(22, 41, 54) # (916, 248)
        waitForColorAndDo(1096, 223, followerColor, 
            func_after_wait=waitAndSelectNoFollower)

    launchColor = Color(0, 43, 68)  # (913,951)
    waitForColorAndDo(913, 951, launchColor)

def handleFollowerError():
    OColor = Color(239, 241, 244) # (943, 602)
    KColor = Color(251, 251, 252) # (972, 596)
    EdgeColor = Color(186, 187, 188) # (1164, 432)
    isFollowerError = myRobot.getPixelColor(943, 602) == OColor and \
            myRobot.getPixelColor(972, 596) == KColor and \
            myRobot.getPixelColor(1164, 432) == EdgeColor
    if isFollowerError:
        print "Follower Error detected, clicking OK"
        myRobot.mouseMove(943, 602)
        myRobot.mousePress(InputEvent.BUTTON1_MASK)
        myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        myRobot.delay(3000)
        selectFollowerAndLaunch(True)
    else:
        print "no follower error"  

def handleCommunicationError():
    # detect communication error
    OColor = Color(242, 245, 248)
    KColor = Color(255, 255, 255)
    EdgeColor = Color(254, 254, 254)
    isCommunicationError = myRobot.getPixelColor(943, 620) == OColor and \
            myRobot.getPixelColor(969, 621) == KColor and \
            myRobot.getPixelColor(1178, 703) == EdgeColor
    if isCommunicationError:
        print "Communication Error detected, clicking OK"
        myRobot.mouseMove(943, 620)
        myRobot.mousePress(InputEvent.BUTTON1_MASK)
        myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    else:
        print "no comm error"

def log(log_filename, event_type, event_message, toDelete=False):
    log_file = 'C:\\Users\\Solti\\Dropbox\\Misc\GameLogs\\' + log_filename
    log_msg = time.strftime('%d/%m/%Y') + ',' + time.strftime('%H:%M:%S') + ',' + event_type + ',' + event_message + '\n'
    open_mode = 'a'
    if toDelete:
        open_mode = 'w'
    with open(log_file, open_mode) as f:
        f.write(log_msg)

def handleMissionEnd(targetX=1140, targetY=332, waitTargetColor=Color(254, 237, 56)):
    # star color = java.awt.Color[r=254,g=237,b=56] (1140, 332)
    firstNextStepIsDone = False
    secondNextStepIsDone = False
    EXPisDone = False
    while myRobot.getPixelColor(targetX, targetY) != waitTargetColor:
        print "targetX =", targetX, ", targetY =", targetY, ", targetColor = ", waitTargetColor
        print "current = ", myRobot.getPixelColor(targetX, targetY)
        handleCommunicationError()
        
        # first next step
        firstNextStepColor = Color(0, 39, 113) # (958, 943)
        if (not firstNextStepIsDone) and myRobot.getPixelColor(958, 943) == firstNextStepColor:
            firstNextStepIsDone = True
            myRobot.mouseMove(958, 943)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        # EXP_X color java.awt.Color[r=189,g=204,b=230], (912, 143)
        EXP_X_color = Color(189, 204, 230)
        if (not EXPisDone) and myRobot.getPixelColor(912, 143) == EXP_X_color:
            EXPisDone = True
            myRobot.mouseMove(912, 143)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        # 2nd next step color java.awt.Color[r=254,g=254,b=254] (938,939)
        secondNextStepColor = Color(254, 254, 254)
        if (not secondNextStepIsDone) and myRobot.getPixelColor(938,939) == secondNextStepColor:
            print '2nd next step click'
            secondNextStepIsDone = True
            myRobot.mouseMove(959, 940)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        print '2nd next  = ', secondNextStepIsDone

        # Friend
        noApplyColor = Color(255, 255, 255) # (780, 784)
        if myRobot.getPixelColor(780, 784) == noApplyColor:
            myRobot.mouseMove(780, 784)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # Close Mission
        goingRewardColor = Color(77, 9, 17) #(1053, 666)
        if myRobot.getPixelColor(1053, 666) == goingRewardColor:
            myRobot.mouseMove(810, 673)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # click empty place to speed up
        myRobot.mouseMove(717, 157)
        myRobot.mousePress(InputEvent.BUTTON1_MASK)
        myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

        # pause for a while        
        myRobot.delay(500)

def selectNoFollower():
    #Location(1256, 291)Location(1256, 1063)
    myRobot.mouseMove(1256, 291)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(300)
    myRobot.mouseMove(1256, 663)
    myRobot.delay(300)
    myRobot.mouseMove(1256, 1063)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(300)
    myRobot.mouseMove(955, 1037)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)

def selectStranger():
    #Location(1256, 291)Location(1256, 1063)
    myRobot.mouseMove(1256, 291)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(300)
    myRobot.mouseMove(1256, 663)
    myRobot.delay(300)
    myRobot.mouseMove(1256, 1063)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(300)
    myRobot.mouseMove(793, 869)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
    myRobot.delay(500)


def waitForColorAndDo(x, y, color, func_while_wait=None, arg_while_wait=[], func_after_wait=None, arg_after_wait=[], wait_time_period=500, func_wait_too_long=None, arg_wait_too_long=[], wait_max_count=20):
    global UNIT_CENTER_LOCATIONS
    print 'x = ', x, ', y = ', y, ', color = ', color
    wait_count = 0
    while not myRobot.getPixelColor(x, y) == color:
        print myRobot.getPixelColor(x, y)
        if func_while_wait != None:
            func_while_wait(*arg_while_wait)
        wait_count += 1
        if wait_count == wait_max_count:
            wait_count = 0
            if func_wait_too_long != None:
                func_wait_too_long(*arg_wait_too_long)
        myRobot.delay(wait_time_period)
    while myRobot.getPixelColor(x, y) == color:
        if func_after_wait != None:
            func_after_wait(*arg_after_wait)
        else:
            myRobot.mouseMove(x, y)
            myRobot.mousePress(InputEvent.BUTTON1_MASK)
            myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        myRobot.delay(wait_time_period)

def waitForColor(x, y, color, wait_msg):
    while not myRobot.getPixelColor(x, y) == color:
        print wait_msg
        myRobot.delay(500)

def buyStrength():
    buyStrengthColor = Color(248, 249, 251) # (1135, 541)
    if myRobot.getPixelColor(1135, 541) == buyStrengthColor:
        myRobot.mouseMove(1135, 541)
        myRobot.mousePress(InputEvent.BUTTON1_MASK)
        myRobot.mouseRelease(InputEvent.BUTTON1_MASK)
        use100StoneRedColor = Color(89,0,0) # (1027, 599)
        waitForColorAndDo(1027, 599, use100StoneRedColor)
    else:
        print "no buying message"


def fastClick(x, y):
    myRobot.mouseMove(x, y)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)


def isWaitingForCommand():
    menuColor = Color(255, 255, 255) # 1139, 1034
    waitingForCommandColor1 = Color(6, 51, 120) # (850, 701)
    waitingForCommandColor2 = Color(6, 53, 124) # (828, 809)
    waitingForCommandColor3 = Color(6, 45, 120) # (821, 921)
    waitingForCommandColor4 = Color(6, 50, 117) # (1155, 700)
    waitingForCommandColor5 = Color(6, 51, 117) # (1153, 808)
    is_someone_waiting = (
        (myRobot.getPixelColor(850, 701) == waitingForCommandColor1) or
        (myRobot.getPixelColor(828, 809) == waitingForCommandColor2) or
        (myRobot.getPixelColor(821, 921) == waitingForCommandColor3) or
        (myRobot.getPixelColor(1155, 700) == waitingForCommandColor4) or
        (myRobot.getPixelColor(1153, 808) == waitingForCommandColor5))
    
    if myRobot.getPixelColor(1139, 1034) == menuColor and is_someone_waiting:
        return True
    else:
        return False

def boundaryGoUp():
    myRobot.mouseMove(756, 464)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(756, 424)
    myRobot.delay(100)
    myRobot.mouseMove(756, 394)
    myRobot.delay(100)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def boundaryGoDown():
    myRobot.mouseMove(756, 464)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(756, 504)
    myRobot.delay(100)
    myRobot.mouseMove(756, 534)
    myRobot.delay(100)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def boundaryGoLeft():
    myRobot.mouseMove(756, 464)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(716, 464)
    myRobot.delay(100)
    myRobot.mouseMove(686, 464)
    myRobot.delay(100)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def boundaryGoRight():
    myRobot.mouseMove(756, 464)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.delay(100)
    myRobot.mouseMove(796, 464)
    myRobot.delay(100)
    myRobot.mouseMove(826, 464)
    myRobot.delay(100)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def selectMission(mission_location_x, mission_location_y):
    frontPageColor = Color(243, 108, 151) # (1184,204)
    waitForColorAndDo(1184, 204, frontPageColor, 
            func_while_wait=fastClick, arg_while_wait=(929, 160),
            func_after_wait=fastClick, arg_after_wait=(mission_location_x, mission_location_y))
    print('waiting for desc next')
    # wait for mission dismiss color and buy strength if necessary
    missionDescNextStepColor = Color(0, 51, 141) # (954, 923)
    waitForColorAndDo(954, 923, missionDescNextStepColor,
            func_while_wait=buyStrength)

def selectFollowerAndLaunch(toSelct):
    followerColor = Color(40, 153, 206) # (1255, 348)    
    if toSelct:
        waitForColorAndDo(1255, 348, followerColor, 
                func_after_wait=fastClick, arg_after_wait=(810, 404))
    else:
        def waitAndSelectNoFollower():
            myRobot.delay(500)
            func_after_wait=selectStranger()
        waitForColorAndDo(1255, 348, followerColor, 
            func_after_wait=waitAndSelectNoFollower)

    launchColor = Color(0, 141, 218)  # (917, 892)
    waitForColorAndDo(917, 892, launchColor)

def moveAroundTillBattle(direction='UpDown'):
    while True:
        moveAround(direction)
        if isInBattle():                
            break
    print 'now in battle'

def closeBSFFBE():
    myRobot.mouseMove(327, 5)
    myRobot.delay(500)

    FFBETopColor = Color(226, 176, 156) # (202, 10)
    waitForColorAndDo(202, 10, FFBETopColor,
            func_after_wait=fastClick, arg_after_wait=(310, 10))
    print 'BS FFBE closed'


def switchEmulator():
    # switch emulator
    type("\t", KEY_ALT)
    myRobot.delay(1000)

def enterBSFFBE():
    BSFFBEColor = Color(230,191,216) # (330, 196)
    waitForColorAndDo(330, 196, BSFFBEColor,
            func_after_wait=fastClick, arg_after_wait=(330, 196))
    print 'entered BS FFBE'

def waitForBSFFBEDesktop():
    print 'waiting for FFBE Desktop'
    friendColor = Color(255,184,254) # (1189, 1025)
    while myRobot.getPixelColor(1189,1025) != friendColor:
        fastClick(995, 639)
        myRobot.delay(1000)
    print 'saw BS FFBE Desktop'

def waitForDuOSFFBEMissionEnd():
    nextStepColor = Color(229, 233, 239) # (937, 902)
    def clickAndHandleCommError():
        fastClick(960, 646)
        myRobot.delay(1000)
        fastClick(925, 590)
        myRobot.delay(1000)
        fastClick(495, 986)
        myRobot.delay(1000)
    waitForColorAndDo(937, 902, nextStepColor,
            func_while_wait=clickAndHandleCommError)

    secondNextStepColor = Color(255, 255, 255) # (933, 905)
    waitForColorAndDo(933, 905, secondNextStepColor,
            func_while_wait=fastClick, arg_while_wait=(925, 590))

    #thirdNextStepColor = Color(129, 150, 176) # (936, 904)
    #waitForColorAndDo(936, 904, thirdNextStepColor,
    #        func_while_wait=fastClick, arg_while_wait=(925, 590))

    frontPageColor = Color(154, 2, 10) # (1190, 270)
    while myRobot.getPixelColor(1190, 270) != frontPageColor:
        fastClick(847, 803)
        myRobot.delay(2000)
    print 'DuOS mission Completed'

def openDuOSAddCloseLine():
    myRobot.mouseMove(912, 1080)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseMove(912, 780)    
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

    myRobot.delay(500)
    myRobot.mouseMove(1027, 1070)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def waitForFloatingWindow():
    myRobot.delay(3000)
    openDuOSAddCloseLine()

def openDuOSFFBE():
    duOSFFBEColor = Color(212,191,219) # (495, 986)
    waitForColorAndDo(495, 986, duOSFFBEColor)

def closeMuOSFFBE():
    openDuOSAddCloseLine()
    
    # wait for floating window
    floatingFrontPageColor = Color(118, 55, 80) # (1261, 462)
    count = 0
    while myRobot.getPixelColor(1261, 462) != floatingFrontPageColor:
        myRobot.delay(1000)
        count += 1
        if count == 6:
            openDuOSAddCloseLine()
            count = 0
    myRobot.delay(1000)
    fastClick(1328, 191)
    myRobot.delay(3000)

    # wait for DuOS FFBE
    duOSFFBEColor = Color(212,191,219) # (495, 986)
    while myRobot.getPixelColor(495, 986) != duOSFFBEColor:
        myRobot.delay(1000)
    print 'back to DuOS Desktop'

def waitForBSFFBEDesktop2():
    friendColor = Color(255,184,254) # (1189, 1025)
    while myRobot.getPixelColor(1189,1025) != friendColor:
        fastClick(962, 940)
    print 'saw BS FFBE Desktop'

def closeBS():
    myRobot.mouseMove(897, 0)
    myRobot.delay(500)
    BSCloseColor = Color(69, 67, 82) # (1897, 11)
    waitForColorAndDo(1897, 11, BSCloseColor)
    print 'BS emulator closed'

def launchBS():
    FFBEonDesktopColor = Color(131,181,22) # (113, 932)
    #FFBEColor = Color(222,53,24)  # (121, 972)
    if myRobot.getPixelColor(113, 932) != FFBEonDesktopColor:
        print 'cannot see FFBE icon'
        exit(1)
    fastClick(113,932)
    myRobot.delay(200)
    fastClick(113,932)
    myRobot.delay(60000) # 60 sec
    # first close live stream window
    type(Key.F4, KeyModifier.ALT)
    myRobot.delay(5000)
    # find maxmize icon
    maximizeRegion = Region(1114,108,293,112)
    maximizeRegion.click("1493181119642.png")
    myRobot.delay(5000)
    # check for BS sponsor message
    tryAppColor = Color(79, 168, 201) # (1563, 766)
    while myRobot.getPixelColor(1563, 766) == tryAppColor:
        fastClick(1563, 766)
        myRobot.delay(2000)

if __name__ == "__main__":
    targetLocation = Location(706, 209)
    hover(targetLocation)
    print(targetLocation)
    print(myRobot.getPixelColor(targetLocation.x, targetLocation.y))
    myRobot.delay(3000)

    
    #wait(3)
  