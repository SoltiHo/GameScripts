count = 0
while True:
    start = time.time()
    count = count + 1
    #if exists("1475571605121.png",5):
    #    click(getLastMatch())
    DeepestRegion = Region(818,527,111,55)
    while not DeepestRegion.exists("1476139453189.png"):
        print "iteration ", count, ": waiting deepest"
        wait(1)
    click(DeepestRegion)
    #wait("1476051381143.png",10)
    #click("1476051381143.png")

    # choose follower
    FollowerRegion = Region(772,245,123,58)
    while not FollowerRegion.exists("1476140101421.png"):
        print "iteration ", count, ": waiting follower"
        click(DeepestRegion)
        wait(1)
    #wait("1476051731046.png",10)
    # select the first
    click(Location(810, 404))

    LaunchRegion = Region(916,899,88,53)
    while not LaunchRegion.exists("1476140355150.png"):
        print "iteration ", count, ": waiting launch"
        click(Location(810, 404))
        wait(1)
    click(LaunchRegion)
    wait(3)
    #wait("1476052182928.png") 
    #click("1476052182928.png")

    # entering battle
    AutoRegion = Region(672,1007,142,70)
    while not AutoRegion.exists("1476140591375.png"):
        print "iteration ", count, ": waiting auto"
        #click(LaunchRegion) 
        click(Location(962, 646))
        wait(1)
    
    click(Location(778, 455))
    click(AutoRegion)
    #wait("1475571086038.png", 30)
    #click(Location(778, 455))
    #click("1475571086038.png")
    #while not exists("1475571541774.png"):


    # end of 1st battle
    EndOfBattleRegion = Region(962,128,101,53)
    while not EndOfBattleRegion.exists("1476051896541.png"):
    #while not exists("1476051896541.png"):     
        wait(0.1)
    click(AutoRegion)
    #click(Location(755, 1042))
    wait(3)
    click(Location(778, 455))
    click(AutoRegion)
    #click(Location(755, 1042))
    #while not exists("1475571541774.png"):
    #while not exists("1476051896541.png"):
    #    wait(0.1)
    #click(Location(755, 1042))
    #wait(3)
    #click(Location(778, 455))
    #click(Location(755, 1042))
    
    #1st next step
    NextStepRegion = Region(889,865,143,78)
    while not NextStepRegion.exists("1476141063965.png"):
        print "iteration ", count, ": waiting 1st next step"
        click(Location(962, 646))
        wait(2)
    click(NextStepRegion)
    wait(1)
    #wait("1476086050282.png",50)
    #click(getLastMatch())
    #wait(0.5)
    #click(getLastMatch())
    #wait(0.5)
    #click(getLastMatch())
    #wait(0.5)
    #click("1476086139752.png")
 
    # 2nd next step 
    while not NextStepRegion.exists("1476148032606.png"):
        print "iteration ", count, ": waiting 2nd next step"
        click(Location(726, 899))        
        wait(0.5)
    click(NextStepRegion)
    wait(1)

    #while not exists("1476086200233.png"):
    #    click(Location(726, 899))
    #    wait(0.3)
    #click(getLastMatch())
    #wait(0.5)
    #click(getLastMatch())
    #wait(0.5)
    #click(getLastMatch())
    #wait(0.5)
    
    # Friends
    FriendApplyRegion = Region(757,771,127,68)
    wait(3)
    while FriendApplyRegion.exists("1476141815654.png"):
        click(FriendApplyRegion)
        wait(0.5)
    #while exists("1476053020690.png"):
    #    click(getLastMatch())
    #    wait(0.5)

    # Close Mission
    CloseMissionRegion = Region(733,637,363,338)
    while CloseMissionRegion.exists("1475571605121.png"):
    #while exists("1475571605121.png"):
        click("1475571605121.png")
        wait(1)
    #while exists("1476053020690.png"):
    #    click(getLastMatch())
    #    wait(0.5)    
    #
    remaining = 303 - (time.time() - start)
    if remaining > 0: wait(remaining)

