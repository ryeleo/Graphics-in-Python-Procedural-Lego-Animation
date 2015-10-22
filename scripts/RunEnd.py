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


def run_end(drama=1.0):
    lego_body = get_lego_man_from_current_selection()
    if lego_body is '':
        return """Was unable to find a "lego body" in the current selection!"""
    animation_time = 6
    end_time = mc.currentTime(query=True) + animation_time
    current_body_move = mc.getAttr(lego_body + ".translateZ")
    body_move = 1.2 * drama + current_body_move
    left_arm = lego_body+"|arm_L"
    right_arm = lego_body+"|arm_R"
    right_leg = lego_body+"|hips|leg_R"
    left_leg = lego_body+"|hips|leg_L"

    mc.setKeyframe(lego_body, right_leg, left_leg, left_arm, right_arm, v=0, at="rotateX", time=end_time, ott="spline")
    mc.setKeyframe(lego_body, v=0, at="translateZ", time=end_time, ott="spline")
    mc.setKeyframe(lego_body, v=0, at="translateY", time=end_time, ott="spline")
    mc.setKeyframe(lego_body, v=body_move, at="translateZ", time=end_time, itt="spline")

run_end()
