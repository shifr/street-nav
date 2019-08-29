import logging

from dataclasses import dataclass, field
from functools import partial


from ..types import DirectionSide, Turn
from .common import Position
from .route import Action, Direction, Route, DIRECTIONS


log = logging.getLogger(__name__)


START_POSITION = (0, 0)
TURN_VALUES = [x.value for x in Turn]


@dataclass
class Robot:
    position: Position = field(default_factory=partial(Position, *START_POSITION))
    _direction: Direction = field(default=DIRECTIONS[DirectionSide.NORTH])

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value: Direction):
        if self._direction != value:
            log.info("Changing direction to %s", value)
            self._direction = value

    def navigate(self, route: Route):
        """
        Start the robot and navigate along the routes
        """
        self.position = Position(route.start.x, route.start.y)
        self.direction = Direction(DirectionSide.NORTH)
        log.info("Navigating '%s' from the %s...", route.name, self.position)

        for action in route.actions:
            self.act(action)

        log.info("Navigation '%s' finished!", route.name)

    def act(self, action: Action):
        """
        Understand which action to evaluate
        """
        log.info(action.description)

        if action.target is not None:
            return self.go_to_position(action.target.position)

        if action.turn is not None:
            return self.turn(action.turn)

        self.go(action.distance, direction=action.direction)

    def go_to_position(self, position: Position):
        """
        Navigate to the actual position, changing the directions
        """
        log.info("Heading for %s...", position)
        x_distance = position.x - self.position.x
        y_distance = position.y - self.position.y

        if x_distance < 0:
            self.direction = DIRECTIONS[DirectionSide.WEST]
        elif x_distance > 0:
            self.direction = DIRECTIONS[DirectionSide.EAST]

        self.go(x_distance)

        if y_distance < 0:
            self.direction = DIRECTIONS[DirectionSide.SOUTH]
        elif y_distance > 0:
            self.direction = DIRECTIONS[DirectionSide.NORTH]

        self.go(y_distance)

        log.info("We're in place!")

    def go(self, distance: int, *, direction: Direction = None):
        """
        Go explisitly defined distance in the direction
        """
        if direction and direction != self.direction:
            self.direction = direction

        if self.direction.side == DirectionSide.WEST:
            new_x = self.position.x - distance
            self.position.x = new_x if new_x > 0 else 0
        elif self.direction.side == DirectionSide.EAST:
            new_x = self.position.x + distance
            self.position.x = new_x if new_x > 0 else 0
        elif self.direction.side == DirectionSide.NORTH:
            new_y = self.position.y + distance
            self.position.y = new_y if new_y > 0 else 0
        elif self.direction.side == DirectionSide.SOUTH:
            new_y = self.position.y - distance
            self.position.y = new_y if new_y > 0 else 0

    def turn(self, turn: Turn):
        new_direction = getattr(self.direction, turn.value, None)

        if new_direction:
            self.direction = new_direction
        else:
            log.warning("Can't turn %s, please choose from %s", turn.value, TURN_VALUES)
