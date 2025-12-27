from typing import Iterable
from osmium import osm
from .types import GeoPoint
#todo fix the bug, could not handle corss zero lon and zero lat case
def find_mbr(points:Iterable[GeoPoint])->osm.Box:
    min_lat = 91.0
    min_lon = 181
    max_lat = -91
    max_lon = -181
    for geo in points:
        if geo.lat < min_lat:
            min_lat = geo.lat
        if geo.lat > max_lat:
            max_lat = geo.lat
        if geo.lon < min_lon:
            min_lon = geo.lon
        if geo.lon > max_lon:
            max_lon = geo.lon
    return osm.Box(osm.Location(min_lon,min_lat),
                   osm.Location(max_lon,max_lat))

