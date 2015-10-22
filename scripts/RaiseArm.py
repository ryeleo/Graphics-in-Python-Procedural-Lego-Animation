#!/bin/python
import maya.cmds as mc


def raise_arm(maya_object, animation_time=48):
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

raise_arm(mc.ls(selection=True))
