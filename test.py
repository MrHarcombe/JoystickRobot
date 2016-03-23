import time
import robot


while True:
    die = input("")
    if die == "w":
        robot.forward(3)
    elif die == "s":
        robot.reverse(3)
    elif die == "a":
        robot.left(0.37)
    elif die == "d":
        robot.right(0.37)

