# -*- coding: utf-8 -*-
"""Main loop for the program

Created 2025.09.27
Contributors:
    Jakub
    Lucas
"""


import turtle
import time
import math
import random
from physics import Body, PhysicsBody, System, Vector2, G
import planets


SCALE = 1 / 5e6
TIMESCALE = 100_000
TPS = 100


turtles: dict = {}
planets_list = [
    obj for obj in planets.__dict__.values()
    if isinstance(obj, Body)
]

planets: dict = {}


def main():
    screen = turtle.Screen()
    screen.title("Simulation Système Planétaire")
    screen.bgcolor("black")
    screen.setup(width=1000, height=800)
    screen.tracer(0)
    
    
    sys = init_system()
    global turtles
    turtles = create_turtles_for_system(sys, SCALE)

    try:
        sun_uid = next(uid for uid, b in sys.bodies.items() if b.name.lower() == "sun")
        sun_pos = sys.bodies[sun_uid].position
    except StopIteration:
        pass
    
    dt = TIMESCALE / TPS
    try:
        while True:
            sys.update(dt)
            #update_system(sys, dt)
            update_graphics(sys, turtles, SCALE)
            screen.update()
            time.sleep(1/TPS)
    except turtle.Terminator:
        return
    except KeyboardInterrupt:
        return


def init_system() -> System:
    """Crée et retourne un System en respectant les contraintes du module Physics."""
    sys = System(bodies={})

    root_bodies = [b for b in planets_list if b.parent_body is None]
    child_bodies = [b for b in planets_list if b.parent_body is not None]

    for b in root_bodies:
        sys.add_body(b, at_origin=True)

    for b in child_bodies:
        sys.add_body(b)

    for uid, phys in sys.bodies.items():
        planets[uid] = phys

    return sys


def create_obj(shape: str = "circle", color: str = "white", shapesize: float = 1.0) -> turtle.Turtle:
    """Crée une turtle selon les spécifications des planètes."""
    t = turtle.Turtle()
    t.hideturtle()
    t.shape(shape)
    t.color(color)
    t.shapesize(shapesize)
    t.penup()
    t.showturtle()
    return t


def create_turtles_for_system(sys: System, SCALE: float) -> dict:
    """Crée une turtle par PhysicsBody, retourne dict uuid -> turtle."""
    tdict = {}
    for uid, body in sys.bodies.items():
        #color = PLANET_COLOR.get(body.name, random.choice(
        #    ["white", "lightgreen", "violet", "cyan", "pink"]))
        color = body.color
        radius_pixels = body.radius * SCALE
        shapesize = max(0.2, radius_pixels / 10.0)
        t = create_obj(shape="circle", color=color, shapesize=shapesize)
        tdict[uid] = t
    return tdict


def update_graphics(sys: System, turtles_dict: dict, SCALE: float):
    """Place toutes les tortues aux positions correspondantes."""
    for uid, body in sys.bodies.items():
        t = turtles_dict.get(uid)
        if t is None:
            continue
        x_pix = body.position.x * SCALE
        y_pix = body.position.y * SCALE
        t.goto(x_pix, y_pix)


if __name__ == "__main__":
    main()
else:
    raise ImportWarning("main.py is the main file and should not be imported")
