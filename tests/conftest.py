from pathlib import Path

import pytest

from navigator.models import Action, City, Direction, Landmark, Position, Route
from navigator.types import DirectionSide, Turn


@pytest.fixture(scope="session")
def data_path():
    return Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def city():
    landmarks = {
        "Madame Tussauds Wax Museum": Landmark("Madame Tussauds Wax Museum", Position(200, 200)),
        "Hyde Park": Landmark("Hyde Park", Position(5, 25)),
    }

    return City("London", landmarks)


@pytest.fixture(scope="session")
def routes(city):
    return [
        Route(
            city=city,
            start=Position(130, 100),
            name='To work',
            actions=[
                Action(
                    description='Go North 5 blocks',
                    distance=5,
                    direction=Direction(DirectionSide.NORTH),
                    target=None,
                    turn=None,
                ),
                Action(
                    description='Turn right',
                    distance=None,
                    direction=None,
                    target=None,
                    turn=Turn.RIGHT,
                ),
                Action(
                    description='Go to landmark "Madame Tussauds Wax Museum"',
                    distance=None,
                    direction=None,
                    target=Landmark(
                        name='Madame Tussauds Wax Museum',
                        position=Position(200, 200)
                    ),
                    turn=None
                ),
                Action(
                    description='Go West 25 blocks',
                    distance=25,
                    direction=Direction(DirectionSide.WEST),
                    target=None,
                    turn=None
                ),
                Action(
                    description='Turn left',
                    distance=None,
                    direction=None,
                    target=None,
                    turn=Turn.LEFT,
                ),
                Action(
                    description='Go 3 blocks',
                    distance=3,
                    direction=None,
                    target=None,
                    turn=None
                ),
            ],
        ),
        Route(
            city=city,
            name="To home",
            start=Position(10, 10),
            actions=[
                Action(
                    description='Go North 25 blocks',
                    distance=25,
                    direction=Direction(DirectionSide.NORTH),
                    target=None,
                    turn=None
                ),
                Action(
                    description='Turn right',
                    distance=None,
                    direction=None,
                    target=None,
                    turn=Turn.RIGHT,
                ),
                Action(
                    description='Go 5 blocks',
                    distance=5,
                    direction=None,
                    target=None,
                    turn=None
                ),
                Action(
                    description='Turn left',
                    distance=None,
                    direction=None,
                    target=None,
                    turn=Turn.LEFT,
                ),
            ],
        ),
    ]
