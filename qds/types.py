from dataclasses import dataclass


@dataclass
class Size:
    width: float
    height: float


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Rect:
    origin: Point
    size: Size
