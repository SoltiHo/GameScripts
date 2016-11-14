import Utilities
reload(Utilities)

count = 0
while True:
    start = time.time()
    count = count + 1
    DeepestRegion = Region(818,527,111,55)
    while not DeepestRegion.exists("1478848873869.png"):
        print "iteration ", count, ": waiting deepest"
        wait(1)
    click(DeepestRegion)
    wait(3)
    click(Location(961, 940)) # the challenge description
    wait(3)
    # choose follower
    FollowerRegion = Region(769,237,144,71)
    while not FollowerRegion.exists("1478839919960.png"):
        print "iteration ", count, ": waiting follower"
        click(DeepestRegion)
        wait(3)
        click(Location(961, 940)) # the challenge description
        wait(3)

    # select the first
    click(Location(810, 404))

    LaunchRegion = Region(916,899,88,53)
    while not LaunchRegion.exists("1478839845298.png"):
        print "iteration ", count, ": waiting launch"
        click(Location(810, 404))
        wait(1)
    click(LaunchRegion)
    wait(3)


    # entering battle
    AutoRegion = Region(672,1007,142,70)
    while not AutoRegion.exists("1476140591375.png"):
        print "iteration ", count, ": waiting auto"
        #click(LaunchRegion) 
        click(Location(962, 646))
        wait(1)

    click(Location(778, 455))
    Utilities.manuallyKickOff()
    #click(AutoRegion)

    # end of 1st battle
    EndOfBattleRegion = Region(962,128,101,53)
    while not EndOfBattleRegion.exists("1476051896541.png"):
        Utilities.manuallyKickOff()
        wait(0.1)
    #click(AutoRegion)
    wait(3)
    click(Location(778, 455))
    Utilities.manuallyKickOff()
    #click(AutoRegion)
    # end of 2nd battle
    EndOfBattleRegion = Region(962,128,101,53)
    while not EndOfBattleRegion.exists("1476051896541.png"):
        Utilities.manuallyKickOff()
        wait(0.1)
    wait(3)
    click(AutoRegion)
    wait(3)


    #1st next step
    NextStepRegion = Region(889,865,143,78)
    while not NextStepRegion.exists("1476141063965.png"):
        print "iteration ", count, ": waiting 1st next step"
        click(Location(962, 646))
        wait(1)
    click(NextStepRegion)
    wait(1)
 
    # 2nd next step 
    while not NextStepRegion.exists("1478846502248.png"):
        print "iteration ", count, ": waiting 2nd next step"
        click(Location(726, 899))        
        wait(0.5)
    click(NextStepRegion)
    wait(1)
    
    # Friends
    FriendApplyRegion = Region(757,771,127,68)
    wait(1)
    while FriendApplyRegion.exists("1478846364756.png"):
        click(FriendApplyRegion)
        wait(0.5)

    # Close Mission
    CloseMissionRegion = Region(733,637,363,338)
    while CloseMissionRegion.exists("1475571605121.png"):
        click("1475571605121.png")
        wait(1)

    remaining = 300 - (time.time() - start)
    #if remaining > 0: wait(remaining)

