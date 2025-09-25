# -*- coding: utf-8 -*-
"""All the code for handling physics

Created 2025.09.22
Contributors:
    Jakub
"""


from __future__ import annotations
import turtle as t
import numpy as np
from dataclasses import dataclass
from beartype import beartype
from uuid import uuid4, UUID


G = 6.6743e-11 # m^3 / (kg * s^2)


def main():
    ...


class Vector2(object):
    # name-mangling to prevent the values from being changed
    __x: float
    __y: float
    
    
    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)
        
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    
    @property
    def x(self) -> float:
        return self.__x
    
    @property
    def y(self) -> float:
        return self.__y
    
    
    def length(self) -> float:
        """Calculate the magnitude of the vector."""
        return (self.x**2 + self.y**2)**0.5
    
    
    def dot(self, other: Vector2) -> float:
        """Calculate the dot product of two vectors."""
        return self.x * other.x + self.y * other.y
    
    
    def rotated(self, angle: float) -> Vector2:
        """Create a new vector rotated by some angle [radians]."""
        # special cases
        if angle == 0.0:
            return self
        elif angle == np.pi:
            return -self
        
        # rotation matrix
        return Vector2(self.x*np.cos(angle) - self.y*np.sin(angle),
                       self.x*np.sin(angle) + self.y*np.cos(angle))
    
    
    def normalized(self) -> Vector2:
        """Return a unit vector with the same dirction."""
        length = self.length()
        return Vector2(self.x / length, self.y / length)
    
    
    def distance_to(self, other: Vector2) -> float:
        """Calculate the Euclidean distance between two vectors.
        
        The distance is always positive or zero.
        """
        displacement = other - self
        return displacement.length()
    
    
    def distance_squared_to(self, other: Vector2) -> float:
        """Calculate the square of the Euclidean distance between two vectors.
        
        Useful for some calculations.
        """
        return (other.x - self.x)**2 + (other.y - self.y)**2
    
    
    def direction_to(self, other: Vector2) -> Vector2:
        """Calculate the normalized direction vector between the endpoints of two
        vectors.
        """
        displacement = other - self
        return displacement.normalized()
    
    
    def __neg__(self) -> Vector2:
        return Vector2(-self.x, -self.y)
    
    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other: Vector2) -> Vector2:
        return self + other
    
    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __rsub__(self, other: Vector2) -> Vector2:
        return Vector2(other.x - self.x, other.y - self.y)
    
    def __mul__(self, scalar: int | float) -> Vector2:
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: int | float) -> Vector2:
        return self * scalar
    
    def __truediv__(self, scalar: int | float) -> Vector2:
        return Vector2(self.x / scalar, self.y / scalar)
    

@dataclass(frozen=True)
class Body():
    """Stores static data of an astronomical object.
    
    Can create a PhysicsBody instance to be used for simulation
    """
    name: str
    mass: float         # kg
    radius: float       # m
    
    parent_body: Body | None = None
    initial_distance: float  = 0.0
    initial_angle:    float  = 0.0
    initial_velocity: float  = 0.0


@dataclass()
class PhysicsBody():
    uuid: UUID
    name: str
    mass: float         # kg
    radius: float       # m
    
    position: Vector2   # m
    velocity: Vector2   # m / s
        
    
    def distance_to(self, other: Body) -> float:
        """Calculate the Euclidean distance between two Bodies.
        
        The distance is always positive or zero.
        """
        displacement = other.position - self.position
        return displacement.length()
    
    
    def distance_squared_to(self, other: Body) -> float:
        """Calculate the square of the Euclidean distance between two vectors.
        
        Useful for some calculations.
        """
        return (other.position.x - self.position.x)**2 + (other.position.y - self.position.y)**2
    
    
    def direction_to(self, other: Body) -> Vector2:
        """Calculate the normalized direction vector between the endpoints of two
        vectors.
        """
        displacement = other.position - self.position
        return displacement.normalized()
    



if __name__ == "__main__":
    main()
