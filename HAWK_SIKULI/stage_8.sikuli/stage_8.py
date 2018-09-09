import Utilities as util
reload(util)


if __name__ == "__main__":
    util.myRobot.delay(2000)
    while True:
        util.moveRight(interval=500, num_steps=15)
        util.myRobot.delay(100)
        util.moveLeft(interval=500, num_steps=15)
        util.myRobot.delay(100)