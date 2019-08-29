from ..models import Position


def get_position(text: str):
    return Position(*map(int, text.strip("()").split(",")))
