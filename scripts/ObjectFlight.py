#!/bin/python
import maya.cmds as mc
import random
import re


def get_ball_from_current_selection():
    selection = mc.ls(selection=True)
    ball = ''
    for item in selection:
        match = re.search("(ball.*)\|*?", item)
        if match:
            ball = match.group(1)
    return ball


def object_flight(height=30):
    ball = get_ball_from_current_selection()
    if ball is '':
        return """Was unable to find a "ball" in the current selection!"""
    final_slide = height/10
    ball_rotation = 360*random.randint(height/20, height/10)
    final_slide_time = height/10

    # Set initial key frame
    current_time = mc.currentTime(query=True)
    mc.setKeyframe(ball, at="translateZ", t=current_time, ott="linear")
    mc.setKeyframe(ball, at="translateY", t=current_time, ott="linear")
    mc.setKeyframe(ball, at="rotate", t=current_time)

    # Set all remaining key frames programatically in the below loop
    bounce_height = height
    bounce_time = bounce_height
    bounce_distance = 0
    while bounce_height > 1:
        # peak of flight
        current_time += bounce_time/2
        mc.setKeyframe(ball, v=bounce_height, at="translateY", t=current_time, itt="spline", ott="spline")

        # touch down to earth
        current_time += bounce_time/2
        mc.setKeyframe(ball, v=0, at="translateY", t=current_time, itt="linear", ott="linear")

        bounce_distance += bounce_height*3
        bounce_time *= 0.5
        bounce_height *= 0.5

    # Set final key frame
    current_time += final_slide_time
    mc.setKeyframe(ball, v=bounce_distance + final_slide, at="translateZ", t=current_time, itt="spline")
    mc.setKeyframe(ball, v=ball_rotation, at="rotate", t=current_time)
    mc.currentTime(current_time)

object_flight()
