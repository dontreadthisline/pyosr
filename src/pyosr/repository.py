
from .types import Road,GeoPoint,Graph
from rtree import index
class OSMRepository:
    ways:dict[int,Road]
    nodes:dict[int,GeoPoint]
    node_to_way:dict[int,set[int]]
    way_to_node:dict[int,set[int]]
    graph:Graph
    looker:index.Index
    def __init__(self):
        self.ways = {}
        self.nodes = {}
        self.node_to_way = {}
        self.way_to_node = {}
        self.graph = {}
        self.looker = index.Index()

