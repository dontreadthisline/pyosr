from .types import  GeoPoint, Graph
from .repository import OSMRepository
from .publisher import Dispatcher,OSMPublisher
from .builders import FilterOutOfBox, RepoNodeBuilder, RepoWayBuilder
from .config import OsrConfig
import osmium
from rtree import index

def load_osm_repo(conf:OsrConfig)->OSMRepository:
    repo = OSMRepository()
    dispatcher = Dispatcher()
    publisher = OSMPublisher(dispatcher)
    #some ugly code
    ld = GeoPoint(0,conf.input.bound_lon_lat[0],conf.input.bound_lon_lat[1])
    ru = GeoPoint(0,conf.input.bound_lon_lat[2],conf.input.bound_lon_lat[3])
    node_filter = FilterOutOfBox(ld,ru)
    node_builder = RepoNodeBuilder(repo,[node_filter,])
    way_builder = RepoWayBuilder(repo)
    dispatcher.register("node",node_builder)
    dispatcher.register("way",way_builder)
    osmium.apply(conf.input.osm_file,publisher)
    repo.graph = build_graph(repo)
    repo.looker = build_rtree(repo)
    return repo

def build_graph(repo:OSMRepository)->Graph:
    graph:Graph = {}
    for way_id,node_ids in repo.way_to_node.items():
        to_ways = set()
        for node_id in node_ids:
            if node_id in repo.node_to_way:
                to_ways |= repo.node_to_way[node_id]
        if to_ways:
           graph[way_id] = list(to_ways - {way_id})
    return graph

def build_rtree(repo:OSMRepository)->index.Index:
    looker = index.Index()
    for way_id,way in repo.ways.items():
        bl = way.mbr.bottom_left
        tr = way.mbr.top_right
        looker.insert(way_id,(bl.lat,bl.lon,tr.lat,tr.lon))
    return looker
