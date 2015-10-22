#!/bin/python
# Assume that if we find a "body" then it is a lego body and it will have the children we expect of it
import maya.cmds as mc
import re


def get_lego_man_from_current_selection():
    selection = mc.ls(selection=True)
    lego_body = ''
    for item in selection:
        match = re.search("(body.*)\|*?", item)
        if match:
            lego_body = match.group(1)
    return lego_body


def kick(drama=1.0, animation_t=24):
    # Figure out the paths to the objects we will be interacting with
    lego_body = get_lego_man_from_current_selection()
    if lego_body is '':
        return """Was unable to find a "lego body" in the current selection!"""
    left_arm = lego_body+"|arm_L"
    right_arm = lego_body+"|arm_R"
    right_leg = lego_body+"|hips|leg_R"
    # Animation Variables
    body_rotation = -10 * drama
    body_sway = 10 * drama
    leg_back_swing = 35 * drama
    arm_back_swing = -30 * drama
    arm_swing = 20 * drama
    leg_swing = -50 * drama
    start_time = mc.currentTime(query=True)

    # Set initial Keyframe
    current_time = start_time
    mc.setKeyframe(left_arm, right_arm, right_leg, lego_body, at="rotateX", v=0, t=current_time)
    mc.setKeyframe(lego_body, at="rotateY", v=0, t=current_time)

    # Set keyframe swinging leg back
    current_time = start_time + (0.2*animation_t)
    mc.setKeyframe(left_arm, at="rotateX", v=arm_back_swing, t=current_time)
    mc.setKeyframe(right_arm, at="rotateX", v=arm_back_swing/2, t=current_time)
    mc.setKeyframe(right_leg, at="rotateX", v=leg_back_swing, t=current_time)
    mc.setKeyframe(lego_body, at="rotateY", v=body_rotation, t=current_time)
    mc.setKeyframe(lego_body, at="rotateX", v=body_sway, t=current_time)

    # Set keyframe swing leg forward
    current_time = start_time + (0.35*animation_t)
    mc.setKeyframe(left_arm, at="rotateX", v=arm_swing, t=current_time)
    mc.setKeyframe(right_arm, at="rotateX", v=arm_swing/2, t=current_time)
    mc.setKeyframe(right_leg, at="rotateX", v=leg_swing, t=current_time)
    mc.setKeyframe(lego_body, at="rotateY", v=-body_rotation, t=current_time)
    mc.setKeyframe(lego_body, at="rotateX", v=-body_sway, t=current_time)

    # Set end Keyframe
    current_time = start_time + animation_t
    mc.setKeyframe(left_arm, right_arm, right_leg, lego_body, at="rotateX", v=0, t=current_time)
    mc.setKeyframe(lego_body, at="rotateY", v=0, t=current_time)
    mc.currentTime(current_time)

kick()
