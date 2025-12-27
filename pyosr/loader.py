from typing import Iterable,Any
from .types import GeoPoint, Graph
from .repository import OSMRepository
from .publisher import Dispatcher,OSMPublisher
import osmium
from osmium import osm
from rtree import index

def load_osm_repo(osm_file:str,conf:Any)->OSMRepository:
    repo = OSMRepository()
    dispatcher = Dispatcher()
    publisher = OSMPublisher(dispatcher)
    osmium.apply(osm_file,publisher)
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
        looker.insert(way_id,way.bound)
    return looker
