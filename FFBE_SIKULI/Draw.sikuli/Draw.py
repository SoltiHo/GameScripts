import java.awt.Color as Color
import java.awt.Robot as JRobot
import java.awt.event.InputEvent as InputEvent
import Utilities
from sikuli import *
reload(Utilities)
myRobot = JRobot()
def main():
    secondBigDrawColor = Color(182, 95, 40) # (1032, 593)
    Utilities.waitForColorAndDo(1032, 593, secondBigDrawColor, wait_time_period=3000,
        func_while_wait=Utilities.fastClick, arg_while_wait=(1127, 717))

    firstNextColor = Color(46, 80, 121) # (931, 880)
    firstNextColor2 = Color(161, 177, 204) # (983, 958)
    while True:
        if myRobot.getPixelColor(931, 880) == firstNextColor:
            Utilities.fastClick(931, 880)
            break
        elif myRobot.getPixelColor(983, 958) == firstNextColor2:
            Utilities.fastClick(983, 958)
            break
        Utilities.fastClick(1215, 169)
        myRobot.delay(1000)
    myRobot.delay(2000)
    #Utilities.waitForColorAndDo(931, 880, firstNextColor, wait_time_period=1000,
    #    func_while_wait=Utilities.fastClick, arg_while_wait=(1135, 345))

    secondNextColor = Color(58, 76, 130) # (990, 973)
    Utilities.waitForColorAndDo(990, 973, secondNextColor, wait_time_period=1000,
        func_while_wait=Utilities.fastClick, arg_while_wait=(1133, 439))

    firstBigDrawColor = Color(249, 89, 27) # (1038, 703)
    Utilities.waitForColor(1038, 703, firstBigDrawColor, "waiting for 1st big ndraw")

if __name__ == "__main__":
    while True:
        main()