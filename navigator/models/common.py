import logging

from dataclasses import dataclass, field


log = logging.getLogger(__name__)


@dataclass
class Position:
    _x: int = field(repr=False)
    _y: int = field(repr=False)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        if self._x == value:
            return

        self._x = value

        log.info("Going %s block(s) forward...", abs(self._x - value))

    @y.setter
    def y(self, value):
        if self._y == value:
            return

        self._y = value

        log.info("Going %s block(s) forward...", abs(self._y - value))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Position({self.x}, {self.y})"
