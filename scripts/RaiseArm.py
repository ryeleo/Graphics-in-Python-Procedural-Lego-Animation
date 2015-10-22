#!/bin/python
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


def raise_arm(animation_time=32):
    lego_body = get_lego_man_from_current_selection()
    if lego_body is '':
        return """Was unable to find a "lego body" in the current selection!"""
    right_arm = lego_body+"|arm_R"
    # Animation Variables
    arm_up_rotation = -140
    start_time = mc.currentTime(query=True)

    # Set initial Keyframe
    current_time = start_time
    mc.setKeyframe(right_arm, at="rotateX", v=0, t=current_time)

    # Set keyframe for rotating arm up
    current_time = start_time + (0.2*animation_time)
    mc.setKeyframe(right_arm, at="rotateX", v=arm_up_rotation, t=current_time)

    # Set keyframe for holding arm up
    current_time = start_time + (0.5*animation_time)
    mc.setKeyframe(right_arm, at="rotateX", v=arm_up_rotation, t=current_time)

    # Set end keyframe
    current_time = start_time + animation_time
    mc.setKeyframe(right_arm, at="rotateX", v=0, t=current_time)

raise_arm()
