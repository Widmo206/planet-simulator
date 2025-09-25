# -*- coding: utf-8 -*-
"""Data on all supported astronomical objects

Created 2025.09.25
Contributors:
    Jakub
"""

from physics import Body
import math


"""
name:             str
mass:             float         # kg
radius:           float         # m

parent_body:      Body   = None
initial_distance: float  = 0.0  # m
initial_angle:    float  = 0.0  # rad
initial_velocity: float  = 0.0  # m / s
"""


Earth = Body(
    name="Earth",
    mass=5.972e24,
    radius=6371008.771
    )

Moon = Body(
    name="Moon",
    mass=7.346e22,
    radius=1737.4e3,
    parent_body=Earth,
    initial_distance=384784e3,
    initial_angle=math.radians(134)
    initial_velocity=1.022e3
    )