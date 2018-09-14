import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import time
from sikuli import *
myRobot = JRobot()

leftX = 660 
rightX = 1258
def moveLeft(interval=1000, num_steps = 10):
    myRobot.mouseMove(rightX, 882)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    for i in range(0, num_steps):
        myRobot.delay(interval/num_steps)
        myRobot.mouseMove(rightX-(rightX-leftX)/num_steps*(i+1), 882)
    myRobot.mouseRelease(InputEvent.BUTTON1_MASK)

def moveRight(interval=1000, num_steps = 10):
    myRobot.mouseMove(leftX, 882)
    myRobot.mousePress(InputEvent.BUTTON1_MASK)
    for i in range(0, num_steps):
        myRobot.delay(interval/num_steps)
        myRobot.mouseMove(leftX+(rightX-leftX)/num_steps*(i+1), 882)
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

if __name__ == "__main__":
    targetLocation = Location(1115, 1029)
    hover(targetLocation)
    print(targetLocation)
    print(myRobot.getPixelColor(targetLocation.x, targetLocation.y))
    myRobot.delay(3000)
