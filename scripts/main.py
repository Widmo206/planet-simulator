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
#import random
from physics import Body, PhysicsBody, System, BodyNotFoundError
import planets
from get_input import get_input


PLANET_SCALE = 0.1
SCALE = 2e9
TIMESCALE = 5e6
TPS = 120

turtles: dict = {}
planets_list = [
    obj for obj in planets.__dict__.values()
    if isinstance(obj, Body)
]

planets_dict: dict = {}


def main():
    # why do I need to do this?
    global PLANET_SCALE
    global SCALE
    global TIMESCALE
    show_moons = False
    
    print("Bienvenue dans le simulateur du système solaire.")
    print()
    print("================================================")
    print()
    print("Veulliez choisir les paramètres (ou appuiyez sur retour pour accepter les valeurs par defaut).\n")
    
    print(f"Afficher les lunes ({'oui' if show_moons else 'non'})")
    new_value = input("> ")
    if new_value != "":
        show_moons = new_value.lower().startswith('o')
    
    sys = init_system(show_moons)
    FOCUSED_BODY = sys.get_body_by_name("sun")
    
    print(f"Centre d'écran ({FOCUSED_BODY.name}) :")
    while True:
        new_name = input("> ")
        if new_name == "":
            break
        else:
            try:
                new_value = sys.get_body_by_name(new_name)
            except BodyNotFoundError:
                continue
            else:
                FOCUSED_BODY = new_value
                break
    
    print(f"Échelle de distances ({SCALE}) :")
    new_value = get_input(float, True, (0, None), True)
    if new_value is not None:
        SCALE = new_value
        
    print(f"Échelle des planètes ({PLANET_SCALE}) :")
    new_value = get_input(float, True, (0, None), True)
    if new_value is not None:
        PLANET_SCALE = new_value
        
    print(f"Échelle du temps ({TIMESCALE}) :")
    new_value = get_input(float, True, (0, None), True)
    if new_value is not None:
        TIMESCALE = new_value
    
    
    
    
    
    screen = turtle.Screen()
    screen.title("Simulation Système Planétaire")
    screen.bgcolor("black")
    screen.setup(width=1000, height=800)
    screen.tracer(0)
    

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
            update_graphics(sys, turtles, SCALE, FOCUSED_BODY)
            screen.update()
            time.sleep(1/TPS)
    except turtle.Terminator:
        return
    except KeyboardInterrupt:
        return


def init_system(show_moons: bool) -> System:
    """Crée et retourne un System en respectant les contraintes du module Physics."""
    sys = System(bodies={})

    root_bodies = [b for b in planets_list if b.parent_body is None]
    child_bodies = [b for b in planets_list if b.parent_body is not None]

    for b in root_bodies:
        sys.add_body(b, at_origin=True)

    for b in child_bodies:
        # only add moons if they're enabled
        if b.parent_body in root_bodies or show_moons:
            sys.add_body(b)

    for uid, phys in sys.bodies.items():
        planets_dict[uid] = phys

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


def create_turtles_for_system(sys: System, scale: float) -> dict:
    """Crée une turtle par PhysicsBody, retourne dict uuid -> turtle."""
    tdict = {}
    for uid, body in sys.bodies.items():
        
        color = body.color
        radius_pixels = math.sqrt(body.radius / planets.Earth.radius) * PLANET_SCALE
        shapesize = max(0.15, radius_pixels)
        
        
        t = create_obj(shape="circle", color=color, shapesize=shapesize)
        tdict[uid] = t
    return tdict


def update_graphics(sys: System, turtles_dict: dict, scale: float, focused_body: PhysicsBody):
    """Place toutes les tortues aux positions correspondantes."""
    for uid, body in sys.bodies.items():
        t = turtles_dict.get(uid)
        if t is None:
            continue
        x_pix = (body.position.x - focused_body.position.x) / scale
        y_pix = (body.position.y - focused_body.position.y) / scale
        t.goto(x_pix, y_pix)


if __name__ == "__main__":
    main()
else:
    raise ImportWarning("main.py is the main file and should not be imported")
