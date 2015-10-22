import maya.cmds as mc
import random

__author__ = 'Ryan'


def swing_arm(maya_object, animation_time=48):
    mc.select(maya_object)
    # Get the starting time and declare any "parameters" inline for now
    starting_time = mc.currentTime(query=True)
    arm_up_time = 0.2 * animation_time + starting_time
    arm_hover_time = 0.5 * animation_time + arm_up_time
    ending_time = animation_time + starting_time

    # Set initial Keyframe
    mc.setKeyframe(at="rotateX", time=starting_time)

    # Set keyframe for rotating arm up
    mc.rotate(-140, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=arm_up_time)

    # Set keyframe for holding arm up
    # mc.rotate(0, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=arm_hover_time)

    # Set keyframe for rotating arm back down
    mc.rotate(140, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=ending_time)


def swing_leg(maya_object, animation_time=24):
    mc.select(maya_object)
    # Get the starting time and declare any "parameters" inline for now
    starting_time = mc.currentTime(query=True)
    swing_back_time = 0.2 * animation_time + starting_time
    swing_kick_time = 0.15 * animation_time + swing_back_time
    ending_time = animation_time + starting_time

    # Set initial Keyframe
    mc.setKeyframe(at="rotateX", time=starting_time)

    # Set keyframe swinging leg back
    mc.rotate(30, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=swing_back_time)

    # Set keyframe swing leg forward
    mc.rotate(-110, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=swing_kick_time)

    # Set keyframe leg coming to rest
    mc.rotate(80, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=ending_time)


def tumble_object_flight(maya_object, height=30):
    mc.select(maya_object)
    # Set initial key frame
    current_time = mc.currentTime(query=True)
    mc.setKeyframe(time=current_time)

    # Set all remaining key frames using while loop
    bounce_height = height
    bounce_time = bounce_height
    bounce_count = 0
    ball_distance_traveled = 0
    while bounce_height > 1:

        # peak of flight
        current_time += bounce_time/2
        mc.move(0, bounce_height, bounce_height, r=True)
        mc.setKeyframe(at="translate", time=current_time, itt="spline", ott="spline")

        # touch down to earth
        current_time += bounce_time/2
        mc.move(0, -bounce_height, bounce_height, r=True)
        mc.setKeyframe(at="translate", time=current_time, itt="linear", ott="linear")

        ball_distance_traveled += bounce_height
        bounce_count += 1
        bounce_time *= 0.25
        bounce_height *= 0.25

    # Set final key frame
    current_time += 6
    mc.move(0, 0, 3, r=True)
    mc.rotate(360*random.randint(1, 3*bounce_count),
              360*random.randint(1, 3*bounce_count),
              360*random.randint(1, 3*bounce_count),
              r=True)
    mc.setKeyframe(at="translate", time=current_time)
    mc.setKeyframe(at="rotate", time=current_time)
