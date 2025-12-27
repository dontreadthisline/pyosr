
from .types import Road,GeoPoint,Graph
from rtree import index
class OSMRepository:
    ways:dict[int,Road]
    nodes:dict[int,GeoPoint]
    node_to_way:dict[int,set[int]]
    way_to_node:dict[int,set[int]]
    graph:Graph
    looker:index.Index

