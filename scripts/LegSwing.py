#!/bin/python
import maya.cmds as mc


def kick(maya_object, animation_time=24):
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

kick(mc.select())
