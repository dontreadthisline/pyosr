from typing import Iterable
from osmium import osm
from .types import GeoPoint
#todo fix the bug, could not handle corss zero lon and zero lat case
def find_mbr(points:Iterable[GeoPoint])->osm.Box:
    min_x = -181.0
    min_y = -91
    max_x = 181
    max_y = 91
    for geo in points:
        if geo.lat < min_x:
            min_x = geo.lat
        if geo.lat > max_x:
            max_x = geo.lat
        if geo.lon < min_y:
            min_y = geo.lon
        if geo.lon > max_y:
            max_y = geo.lon
    return osm.Box(min_x,min_y,max_x,max_y)

