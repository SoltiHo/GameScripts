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



