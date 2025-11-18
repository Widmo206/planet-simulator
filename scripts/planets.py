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

color: str = "white"

parent_body:      Body   = None
initial_distance: float  = 0.0  # m
initial_angle:    float  = 0.0  # rad
initial_velocity: float  = 0.0  # m / s
"""

PLANET_COLOR = {
    "Sun": "yellow",
    "Mercury": "gray",
    "Venus": "orange",
    "Earth": "blue",
    "Moon": "lightgray",
    "Mars": "red",
    "Jupiter": "saddle brown",
    "Saturn": "khaki",
    "Uranus": "light blue",
    "Neptune": "navy"
}


Sun = Body(
    name="Sun",
    mass=1.9885e30,
    radius=695_700e3,
    color="yellow"
    )


Mercury = Body(
    name="Mercury",
    mass=3.3011e23,
    radius=2439.7e3,
    color="gray",
    parent_body=Sun,
    initial_distance=69.82e9,
    initial_angle=math.radians(203.92),
    initial_velocity=38.86e3,
    )


Venus = Body(
    name="Venus",
    mass=4.8675e24,
    radius=6051.8e3,
    color="orange",
    parent_body=Sun,
    initial_distance=108.21e9,
    initial_angle=math.radians(104.999),
    initial_velocity=35.02e3,
    )


Earth = Body(
    name="Earth",
    mass=5.972e24,
    radius=6_371_008.771,
    color="blue",
    parent_body=Sun,
    initial_distance=147.10e9,
    initial_angle=math.radians(288.1),
    initial_velocity=30.29e3,
    )


# Moon = Body(
#     name="Moon",
#     mass=7.346e22,
#     radius=1737.4e3,
#     color="lightgray",
#     parent_body=Earth,
#     initial_distance=384784e3,
#     initial_angle=math.radians(134),
#     initial_velocity=1.022e3,
#     )


Mars = Body(
    name="Mars",
    mass=6.4171e23,
    radius=3396.2e3,
    color="red",
    parent_body=Sun,
    initial_distance=206650000e3,
    initial_angle=math.radians(305.912),
    initial_velocity=26.5e3,
    )











