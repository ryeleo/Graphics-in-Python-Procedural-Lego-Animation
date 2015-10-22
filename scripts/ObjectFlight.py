#!/bin/python
import maya.cmds as mc
import random
import re


def get_lego_man_from_current_selection():
    selection = mc.ls(selection=True)
    lego_body = ''
    for item in selection:
        match = re.search("(body.*)\|*?", item)
        if match:
            lego_body = match.group(1)
    return lego_body


def object_flight(maya_object, height=30):
    lego_body = get_lego_man_from_current_selection()
    if lego_body is '':
        return """Was unable to find a "lego body" in the current selection!"""
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

object_flight(mc.ls(selection=True), 45)
