import re
import typing as t

from ..models import Action, City, Route, DIRECTIONS
from ..types import Actions, DirectionSide, Turn
from .helpers import get_position


NAME_MARKER = "#"
LANDMARK = "landmark"
TURNS = {
    Turn.LEFT.value: Turn.LEFT,
    Turn.RIGHT.value: Turn.RIGHT,
}
SIDES = {
    DirectionSide.NORTH.value: DirectionSide.NORTH,
    DirectionSide.SOUTH.value: DirectionSide.SOUTH,
    DirectionSide.EAST.value: DirectionSide.EAST,
    DirectionSide.WEST.value: DirectionSide.WEST,
}


def parse_action_line(line: str) -> tuple:
    line = line.strip()

    if LANDMARK in line:
        return None, None, line.split(LANDMARK)[-1].strip().strip('"')

    go = re.search(r'Go ([0-9]+) blocks', line)
    go_direction = re.search(r'Go ([A-Za-z]+) ([0-9]+) blocks', line)

    if go:
        return int(go.group(1)), None, None

    if go_direction:
        return int(go_direction.group(2)), go_direction.group(1), None

    return None, None, None


class RoutesParser:
    @classmethod
    def from_plain_text(csl, city: City, file_path: str) -> t.List[Route]:
        """
        Parse routes and actions from the plaintext file
        """
        routes = []
        with open(file_path, "r") as f:
            line = f.readline()
            last_route_name = None
            last_route = None

            while line:
                action = None
                # logic below could be split into multiple small action parsers
                if line.startswith(NAME_MARKER):
                    last_route_name = line[1:].strip()
                elif line.startswith("Start"):
                    *_, pos = line.split()
                    start = get_position(pos)

                    last_route = Route(city, start=start, name=last_route_name)
                    routes.append(last_route)

                    last_route_name = None
                elif line.startswith(Actions.GO.value):
                    distance, side, target = parse_action_line(line)

                    if target and target in last_route.city.landmarks:
                        target = last_route.city.landmarks[target]
                    else:
                        target = None

                    direction = DIRECTIONS.get(SIDES.get(side))

                    action = Action(
                        description=line.strip(),
                        distance=distance,
                        direction=direction,
                        target=target,
                    )
                elif line.startswith(Actions.TURN.value):
                    description = line.strip()
                    turn = description.split(Actions.TURN.value)[-1].strip()
                    action = Action(
                        description=description,
                        turn=TURNS.get(turn),
                    )

                if action is not None:
                    last_route.actions.append(action)

                line = f.readline()

            return routes
