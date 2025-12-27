from typing import Iterable
from osmium import osm
from .types import GeoPoint

def find_box(points:Iterable[GeoPoint])->osm.Box:
    return osm.Box(0,0,0,0)
