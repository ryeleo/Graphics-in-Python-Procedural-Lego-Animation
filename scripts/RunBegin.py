#!/bin/python
# I make the assumption that I can arbitrarily select "body", "leg_L" and "leg_R" in this script. Need to go through
# and make it so that I select from a subset of the current selection only.
# TODO: Pass the currently selected object as a parameter and select Body, and Legs as a subset of that
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


def run_begin(right_leg_lead, drama=1.0):
    lego_body = get_lego_man_from_current_selection()
    if lego_body is '':
        return """Was unable to find a "lego body" in the current selection!"""
    # Animation details
    animation_time = 6
    current_body_move = mc.getAttr(lego_body + ".translateZ")
    body_move = 0.8 * drama + current_body_move
    body_bounce = 0.15 * drama
    body_sway = 8 * drama
    leg_swing_rotation = 35 * drama
    if right_leg_lead:
        leg_swing_rotation = -leg_swing_rotation
    start_time = mc.currentTime(query=True)
    end_time = mc.currentTime(query=True) + animation_time
    left_arm = lego_body+"|arm_L"
    right_arm = lego_body+"|arm_R"
    right_leg = lego_body+"|hips|leg_R"
    left_leg = lego_body+"|hips|leg_L"

    # Set initial keyframe
    mc.setKeyframe(lego_body, right_leg, left_leg, left_arm, right_arm, at="rotateX", time=start_time, ott="spline")
    mc.setKeyframe(lego_body, at="translateZ", time=start_time, ott="spline")
    mc.setKeyframe(lego_body, at="translateY", time=start_time, ott="spline")

    # Set ending keyframe
    mc.setKeyframe(lego_body, v=body_bounce, at="translateY", time=end_time, ott="spline")
    mc.setKeyframe(lego_body, v=body_move, at="translateZ", time=end_time, itt="linear", ott="linear")
    mc.setKeyframe(lego_body, v=body_sway, at="rotateX", time=end_time, itt="linear", ott="linear")
    mc.setKeyframe(right_leg, left_arm, v=leg_swing_rotation, at="rotateX", time=end_time, itt="linear", ott="linear")
    mc.setKeyframe(left_leg, right_arm, v=-leg_swing_rotation, at="rotateX", time=end_time, itt="linear", ott="linear")
    mc.currentTime(end_time)

run_begin(True)
