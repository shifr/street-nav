import typing as t

from dataclasses import dataclass, field

from .common import Position


@dataclass
class Landmark:
    name: str
    position: Position


@dataclass
class City:
    name: str
    landmarks: t.Dict[str, Landmark] = field(default_factory=dict, repr=False)
