import Utilities
reload(Utilities)
count = 0
while True:
    count = count + 1
    if Utilities.isAttacking():
        print "attacking -------"
    else:
        print "not attacking ------"
    wait(0.5)
    if count > 10:
        break;
    
exit


testRegion = Region(1276,448,82,62)
Settings.OcrTextRead = True #to switch on the Region.text() function
print testRegion.text()
exit

MyColor = getPixelColor(Location(785, 776))
print MyColor
exit

UnitHP_01 = Region(776,768,22,14)
UnitHP_02 = Region(786,872,27,16)
UnitHP_03 = Region(772,977,25,13)
UnitHP_04 = Region(1061,768,25,15)
UnitHP_05 = Region(1059,874,26,14)

EmptyBlood = "EmptyBlood.png"
shouldCure = False
if UnitHP_01.exists(EmptyBlood):
    print "User 1 need cure"
    shouldCure = True
if UnitHP_02.exists(EmptyBlood):
    print "User 2 need cure"
    shouldCure = True
if UnitHP_03.exists(EmptyBlood):
    print "User 3 need cure"
    shouldCure = True
if UnitHP_04.exists(EmptyBlood):
    print "User 4 need cure"
    shouldCure = True
if UnitHP_05.exists(EmptyBlood):
    print "User 5 need cure"
    shouldCure = True

if not shouldCure:
    print "-------------------------"
else:
    print "should cure"
        


MagicRegion = Region(668,682,577,303)
MagicMiddleCure = "MagicMiddleCure.png"
MagicRegion.mouseMove(Location(958, 786))
while True:
    MagicRegion.mouseDown(Button.LEFT)
    MagicRegion.mouseMove(0, -50)
    MagicRegion.mouseUp(Button.LEFT)
    if MagicRegion.exists(MagicMiddleCure):
        click(getLastMatch())
        wait(0.5)
        click(Location(805, 738))
        break
