#!/usr/bin/env python3

'''Cozmo attempts to dance the first two minutes of Michael Jackson's hit Thriller
'''

import time
import cozmo


def dance_cozmo(robot: cozmo.robot.Robot):

    #NOTES
        #if head/lift already max/min, cozmo won't move them
        #need to convert degrees to angle object -- same for a lot of parameters
        #use + number for speed to go up and - to go down
        #use time.sleep() to give cozmo time to complete movements
    #BOUNDS
        #MIN_HEAD_ANGLE = -25 degrees (-.44 radians)
        #MAX_HEAD_ANGLE = 44.5 degrees (.78 radians)
        #MIN_LIFT_HEIGHT_MM = 32 -- range for height is actually 0 to 1 though
        #MAX_LIFT_HEIGHT_MM = 92
    #DANCE
        #song starts at 40 seconds
        #ACT 1 -- 40-57 seconds -- 8 head flicks every ~2.5 seconds
        #ACT 2 -- 58-67 -- 6 steps forward with arms out then bring them back in 
        #ACT 3 -- 68-71 -- 1 turn to the side and look up with lift raised, then lower both
        #ACT 4 -- 72-74 -- 1 sprinkler-esque arm move next to head with a little back-and-forth
        #ACT 5 -- 75-89 -- 4 head nods with some forward-back motion
        #ACT 6 -- 90-108 -- moving side to side, lowering and raising lift at each turn with a back and forth at each end

    #GET COZMO IN PLACE
    robot.set_head_angle(cozmo.util.degrees(-25), duration = 0.0).wait_for_completed()
    robot.set_lift_height(0.0, duration = 0.0).wait_for_completed()

    #ACT 1
    for x in range(0, 9): #8
        robot.move_head(5)
        time.sleep(.3)
        robot.move_head(-5)
        time.sleep(1.6)

    #ACT 2
    robot.move_head(2)
    for y in range(0, 6): #6
        robot.move_lift(5)
        robot.drive_straight(cozmo.util.distance_mm(50.0), cozmo.util.speed_mmps(200.0), should_play_anim = False, in_parallel = True)
        time.sleep(.9)
        robot.move_lift(-5)
        time.sleep(.9)

    #ACT 3
    robot.drive_wheels(-150, 150, duration = 1) #90 degree turn counter-clockwise
    robot.move_lift(5)
    robot.move_head(5)
    time.sleep(1)
    robot.move_lift(-1)
    robot.move_head(-1)
    time.sleep(2)

    #ACT 4
    for n in range (0, 4):
        robot.move_lift(2)
        time.sleep(.2)
        robot.move_lift(-.5)
        time.sleep(.3)
    robot.move_lift(2)
    time.sleep(1)

    #ACT 5
    for x in range(0, 5): #6
        robot.move_head(10)
        robot.drive_wheels(150, 150, duration = .73) 
        time.sleep(.1)
        robot.move_head(-5)
        robot.drive_wheels(-50, -50, duration = 1.5) 
        time.sleep(.5)

    #ACT 6
    robot.move_head(5)
    robot.drive_wheels(-150, 150, duration = 1) #90 degree turn counter-clockwise
    time.sleep(1)

    for i in range (0, 3):
        robot.move_lift(10)
        robot.drive_straight(cozmo.util.distance_mm(150.0), cozmo.util.speed_mmps(75.0), should_play_anim = False, in_parallel = True)
        time.sleep(2)
        #back-and-forth
        for w in range(0, 2):
            robot.move_lift(-10)
            time.sleep(.3)
            robot.move_lift(10)
            time.sleep(.3)
            robot.drive_wheels(-300, 300, duration = 1) #180 degree turn counter-clockwise
        #final turn
        robot.move_lift(-10)
        time.sleep(.3)
        robot.move_lift(10)
        time.sleep(.3)
        robot.drive_wheels(-350, 350, duration = 1) 
        time.sleep(.3)

cozmo.run_program(dance_cozmo)
