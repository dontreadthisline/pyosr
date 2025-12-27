from typing import NamedTuple,TypeVar
from osmium import osm

OSM_T = TypeVar("OSM_T",osm.Node,osm.Way,osm.Relation)

class GeoPoint(NamedTuple):
    poi_id:int
    lon:float
    lat:float
    def to_location(self)->osm.Location:
        return osm.Location(lon=self.lon,lat=self.lat)

class Road(NamedTuple):
    link_id:int
    points:list[GeoPoint]
    road_len:float
    road_name:str
    bound:osm.Box

class Path:
    way_id:int
    points:list[GeoPoint]
    dist:float
    cost:float

class Route:
    cost:float
    dist:float
    paths:list[Path]

    def __init__(self):
        self.paths = []
        self.cost = -1
        self.dist = -1

    def __len__(self)->int:
        return len(self.paths)

type Graph = dict[int,list[int]]

type OdPair = tuple[OdPointLiker,OdPointLiker]

type OdPointLiker = int|str|GeoPoint
