# To run this script, AUTO LB can be ON.
TARGET_LB_TYPE = 1  # 1 is attack, 2 is others\
import Utilities
reload(Utilities)



def doOffensiveLB():
    openMagicMenu(5)
    wait(2)
    if Utilities.isLBAvailable(True):
        return True
    else:
        print "offensive LB isn't available"
        return False

def doDefensiveLB():
    openMagicMenu(5)
    wait(2)
    if Utilities.isLBAvailable(True):
        Utilities.defense(1)
        Utilities.defense(2)
        Utilities.defense(3)
        Utilities.defense(4)
        return True
    else:
        print "defensive LB isn't available"
        return False

def doLBaccordingToType():
    LB_EXECUTED = False
    if TARGET_LB_TYPE != 1:
        LB_EXECUTED = doDefensiveLB()
    else:
        LB_DEXECUTED = doOffensiveLB()
    wait(0.5)
    Utilities.manuallyKickOff()
    return LB_EXECUTED

LastTransferredUnitIdx = 3

openMagicMenu(5)
wait(0.5)
if Utilities.isLBAvailable(True):
    if not doLBaccordingToType():
        print "Error, LB should be ready but not"
        exit(1)
else:
    # Target LB is not available, see if anyone can transfer
    Utilities.closeMagicMenu()
    checkCount = 0
    ToCheckUnitIdx = (LastTransferredUnitIdx + 1) % 4    
    while checkCount < 4:
        checkCount = checkCount + 1
        Utilities.openMagicMenu(ToCheckUnitIdx + 1)
        print "Checking unit num ", ToCheckUnitIdx + 1
        wait(0.5)
        if Utilities.isLBAvailable(False):
            # LB available, find transfer magic
            magicTransfer = "MagicTransfer.png"
            result = findTheMagic(magicTransfer)
            if result != None:
                click(result)
                wait(0.5)
                click(Location(1044, 835))
                wait(0.5)
                click(Utilities.UNIT_CENTER_LOCATIONS[ToCheckUnitIdx])
                wait(0.5)
                LastTransferredUnitIdx = ToCheckUnitIdx
                break
        ToCheckUnitIdx = (ToCheckUnitIdx + 1) % 4
        Utilities.closeMagicMenu()
    if checkCount < 4:
        # transferred
        if not doLBaccordingToType():
            print "Error, LB should be ready but not"
            exit(1)
    else:
        # no one can transfer
        # just do normal kickoff
        Utilities.manuallyKickOff()