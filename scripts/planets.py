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


Moon = Body(
    name="Moon",
    mass=7.346e22,
    radius=1737.4e3,
    color="lightgray",
    parent_body=Earth,
    initial_distance=384784e3,
    initial_angle=math.radians(134),
    initial_velocity=1.022e3,
    )


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


Ceres = Body(
    name="Ceres",
    mass=9.3839e20,
    radius=469.7e3,
    color="lightgray",
    parent_body=Sun,
    initial_distance=381e9,
    initial_angle=math.radians(5.0),
    initial_velocity=17.9e3,
    )


Jupiter = Body(
    name="Jupiter",
    mass=1.8982e27,
    radius=71492e3,
    color="saddle brown",
    parent_body=Sun,
    initial_distance=778e9,
    initial_angle=math.radians(293.887),
    initial_velocity=13.06e3,
    )


Io = Body(
    name="Io",
    mass=8.931e22,
    radius=1821.6e3,
    color="yellow",
    parent_body=Jupiter,
    initial_distance=421700e3,
    initial_angle=math.radians(0),
    initial_velocity=17.334e3,
    )


Europa = Body(
    name="Europa",
    mass=4.79984e22,
    radius=1560.6e3,
    color="tan",
    parent_body=Jupiter,
    initial_distance=670900e3,
    initial_angle=math.radians(90),
    initial_velocity=13743.36,
    )


Ganymede = Body(
    name="Ganymede",
    mass=1.4819e23,
    radius=2634.1e3,
    color="light gray",
    parent_body=Jupiter,
    initial_distance=1070400e3,
    initial_angle=math.radians(180),
    initial_velocity=10.880e3,
    )


Callisto = Body(
    name="Callisto",
    mass=1.075938e23,
    radius=2410.3e3,
    color="gray",
    parent_body=Jupiter,
    initial_distance=1882700e3,
    initial_angle=math.radians(270),
    initial_velocity=8.204e3,
    )


Saturn = Body(
    name="Saturn",
    mass=5.6834e26,
    radius=60268e3,
    color="khaki",
    parent_body=Sun,
    initial_distance=1514e9,
    initial_angle=math.radians(296.412),
    initial_velocity=9.09e3,
    )


Titan = Body(
    name="Titan",
    mass=1.345e23,
    radius=2574.73e3,
    color="gray",
    parent_body=Saturn,
    initial_distance=1221870e3,
    initial_angle=math.radians(270),
    initial_velocity=5.57e3,
    )


Uranus = Body(
    name="Uranus",
    mass=86.811e24,
    radius=25559e3,
    color="light blue",
    parent_body=Sun,
    initial_distance=3001.390e9,
    initial_angle=math.radians(216.245),
    initial_velocity=6.49e3,
    )


Neptune = Body(
    name="Neptune",
    mass=1.02409e26,
    radius=24622e3,
    color="navy",
    parent_body=Sun,
    initial_distance=4558.857e9,
    initial_angle=math.radians(173.070),
    initial_velocity=5.45e3,
    )









