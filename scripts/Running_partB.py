import maya.cmds as mc
__author__ = 'Ryan'

# I make the assumption that I can arbitrarily select "body", "leg_L" and "leg_R" in this script. Need to go through
# and make it so that I select from a subset of the current selection only.
# TODO: Pass the currently selected object as a parameter and select Body, and Legs as a subset of that


def begin(right_leg_lead):
    animation_time = 6
    start_animation_time = mc.currentTime(query=True)
    end_animation_time = start_animation_time + animation_time

    # Set initial keyframe
    mc.select("body")
    mc.setKeyframe(at="rotateX", time=start_animation_time)
    mc.setKeyframe(at="translateZ", time=start_animation_time)
    mc.select("leg_R")
    mc.setKeyframe(at="rotateX", time=start_animation_time)
    mc.select("leg_L")
    mc.setKeyframe(at="rotateX", time=start_animation_time)

    # Global Movements: Leaning the body forward and translating it forward
    mc.select("body")
    mc.move(0, 0, 1, r=True)
    mc.setKeyframe(at="translateZ", time=end_animation_time, ott="linear")
    mc.rotate(8, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=end_animation_time)

    # Rotate Legs AND SCALE LEGS
    # Rotate legA (x) forward 35
    # Rotate legB (x) backward -35
    leg_swing_rotation = 45
    if right_leg_lead:
        leg_swing_rotation = -leg_swing_rotation

    mc.select("leg_R")
    mc.rotate(leg_swing_rotation, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.select("leg_L")
    mc.rotate(-leg_swing_rotation, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.currentTime(end_animation_time)


def end():
    animation_time = 6
    start_animation_time = mc.currentTime(query=True)
    end_animation_time = start_animation_time + animation_time

    # Global Movements: Leaning the body forward and translating it forward
    mc.select("body")
    mc.move(0, 0, 1, r=True)
    mc.setKeyframe(at="translateZ", time=end_animation_time)
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)

    # Rotate Legs AND SCALE LEGS
    # Rotate legA (x) forward 35
    # Rotate legB (x) backward -35
    mc.select("leg_R")
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.select("leg_L")
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.currentTime(end_animation_time)


def stride(right_leg_lead):
    animation_time = 6
    start_animation_time = mc.currentTime(query=True)
    end_animation_time = start_animation_time + animation_time

    # Global Movements: translating the body forward
    mc.select("body")
    mc.move(0, 0, 4, r=True)
    mc.setKeyframe(at="translateZ", time=end_animation_time, itt="linear", ott="linear")

    # Rotate Legs AND SCALE LEGS
    # Rotate legA (x) forward 35
    # Rotate legB (x) backward -35
    leg_swing_rotation = -90
    if right_leg_lead:
        leg_swing_rotation = -leg_swing_rotation

    mc.select("leg_R")
    mc.rotate(leg_swing_rotation, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.select("leg_L")
    mc.rotate(-leg_swing_rotation, 0, 0, r=True)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.currentTime(end_animation_time)
