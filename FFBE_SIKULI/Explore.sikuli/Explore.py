moveCount = 0
SUMMON_NUM = 0
to_summon = False
direeciton = 'UpDown'

import java.awt.Robot as JRobot
import java.awt.Color as Color
import java.awt.event.InputEvent as InputEvent
import Utilities
reload(Utilities)

myRobot = JRobot()

    
def Battle():
    if not Utilities.isInBattle():
        return
    # In Battle
    myRobot.delay(500)
    if to_summon and Utilities.lookAbleToSummon():
        Utilities.summonIfAvailable(SUMMON_NUM)
    myRobot.delay(1500)
    Utilities.doMiddleCureIfNeeded()

    myRobot.delay(500)
    doSteal()
    myRobot.delay(1000)
    
    Utilities.fastClick(783, 518)
    Utilities.fastClick(908, 462)
    Utilities.fastClick(750, 387)    

    autoColor = Color(0, 38, 89) # 734, 1034
    Utilities.waitForColorAndDo(734, 1034, autoColor)
    
    # Battle Ends
    gilColor = Color(222,168,24) # (887, 412)
    Utilities.waitForColorAndDo(887, 412, gilColor)

def main():
    while True:
        Utilities.moveAround(direeciton)
        Battle()
        print "one round finished"
        if moveCount > 1000:
            break
    print "end"

if __name__ == "__main__":
    #print(Utilities.lookAbleToSummon())
    main()
    #Battle()