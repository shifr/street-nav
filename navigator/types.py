from enum import Enum


class Turn(Enum):
    LEFT: str = "left"
    RIGHT: str = "right"


class Actions(Enum):
    GO: str = "Go"
    TURN: str = "Turn"


class DirectionSide(Enum):
    NORTH: str = "North"
    SOUTH: str = "South"
    EAST: str = "East"
    WEST: str = "West"
