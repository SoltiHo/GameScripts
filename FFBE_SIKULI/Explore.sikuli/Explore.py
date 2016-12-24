moveCount = 0
SUMMON_NUM = 5
direeciton = 'LeftRight'

import Utilities
reload(Utilities)



def Battle():
    if not Utilities.isInBattle():
        return
    # In Battle
    if Utilities.lookAbleToSummon():
        Utilities.summonIfAvailable(SUMMON_NUM)
    Utilities.doMiddleCureIfNeeded()

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
    main()
    #Battle()