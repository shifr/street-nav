import typing as t

from dataclasses import dataclass, field

from ..types import DirectionSide, Turn
from .city import City, Landmark
from .common import Position


UNKNOWN_ROUTE = "Unknown"


@dataclass
class Direction:
    side: DirectionSide

    _turns = {
        DirectionSide.NORTH: (DirectionSide.WEST, DirectionSide.EAST),
        DirectionSide.SOUTH: (DirectionSide.EAST, DirectionSide.WEST),
        DirectionSide.EAST: (DirectionSide.NORTH, DirectionSide.SOUTH),
        DirectionSide.WEST: (DirectionSide.SOUTH, DirectionSide.NORTH),
    }
    _left = None
    _right = None

    @property
    def left(self):
        if not self._left:
            left, _ = self._turns[self.side]
            self._left = Direction(left)

        return self._left

    @property
    def right(self):
        if not self._right:
            _, right = self._turns[self.side]
            self._right = Direction(right)

        return self._right

    def __repr__(self):
        return self.side.value


DIRECTIONS = dict((side, Direction(side)) for side in DirectionSide)


@dataclass
class Action:
    description: str
    distance: int = None
    direction: Direction = None
    target: Landmark = None
    turn: Turn = None

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.distance:
            return

        if self.target:
            return

        if self.turn:
            return

        raise ValueError("Either distance or target shoud exists!")


@dataclass
class Route:
    city: City
    start: Position
    name: str = field(default=UNKNOWN_ROUTE)
    actions: t.List[Action] = field(default_factory=list)
