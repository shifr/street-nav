import pytest

from navigator.models import Action, Direction, Position, Robot
from navigator.types import DirectionSide, Turn


class TestAction:
    @pytest.mark.parametrize(
        "dist,direction,target,turn,exc",
        [
            (5, None, None, None, False),
            (5, Direction(DirectionSide.NORTH), None, None, False),
            (None, Direction(DirectionSide.NORTH), None, None, True),
            (None, Direction(DirectionSide.NORTH), None, Turn.LEFT, False),
            (None, None, None, Turn.LEFT, False),
            (None, None, None, None, True),
        ]
    )
    def test_validate(self, dist, direction, target, turn, exc):
        if exc:
            with pytest.raises(ValueError):
                Action("action", dist, direction, target, turn)
        else:
            assert Action("action", dist, direction, target, turn)


class TestDirection:
    def test_turns(self):
        turns = {
            DirectionSide.NORTH: (DirectionSide.WEST, DirectionSide.EAST),
            DirectionSide.SOUTH: (DirectionSide.EAST, DirectionSide.WEST),
            DirectionSide.EAST: (DirectionSide.NORTH, DirectionSide.SOUTH),
            DirectionSide.WEST: (DirectionSide.SOUTH, DirectionSide.NORTH),
        }

        for side, side_turns in turns.items():
            direction = Direction(side)
            left, right = side_turns

            assert direction.left == Direction(left)
            assert direction.right == Direction(right)


class TestRobot:
    def test_go_to_position(self):
        position = Position(10, 10)
        robot = Robot()

        assert robot.position != position

        robot.go_to_position(position)

        assert robot.position == position
        assert robot.direction == Direction(DirectionSide.NORTH)

    @pytest.mark.parametrize(
        "distance,direction,position",
        [
            (5, None, Position(0, 5)),
            (10, Direction(DirectionSide.WEST), Position(0, 0)),
            (10, Direction(DirectionSide.EAST), Position(10, 0)),
            (10, Direction(DirectionSide.SOUTH), Position(0, 0)),
        ]

    )
    def test_go(self, distance, direction, position):
        robot = Robot()

        robot.go(distance, direction=direction)

        assert robot.position == position

        if direction:
            assert robot.direction == direction

    def test_navigate(self, routes):
        robot = Robot()

        route1, route2 = routes
        robot.navigate(route1)

        assert robot.position == Position(175, 197)
        assert robot.direction == Direction(DirectionSide.SOUTH)

        robot.navigate(route2)

        assert robot.position == Position(15, 35)
        assert robot.direction == Direction(DirectionSide.NORTH)
