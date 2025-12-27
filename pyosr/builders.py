from typing import Protocol
from osmium import osm
from .types import GeoPoint,OSM_T,Road
from .repository import OSMRepository

class Filter(Protocol[OSM_T]):
    def __call__(self,ref:OSM_T)->bool:
        ...

class FilterOutOfBox(Filter[osm.Node]):
    ld:GeoPoint
    ru:GeoPoint
    def __init__(self,ld:GeoPoint,ru:GeoPoint):
        self.ld = ld
        self.ru = ru
    def __call__(self,node:osm.Node)->bool:
        inbox = self.ld.lat <= node.lat <= self.ru.lat and self.ld.lon <= node.lon <= self.ru.lon
        return not inbox


class Builder(Protocol[OSM_T]):
    def __call__(self,ref:OSM_T)->None:
        ...


class RepoNodeBuilder(Builder[osm.Node]):
    def __init__(self,repo:OSMRepository,filters:list[Filter]):
        self.repo = repo
        self.filters = filters

    def node(self,node_ref:osm.Node):
        need_keep = all(not filter(node_ref) for filter in self.filters)
        if need_keep:
            point = GeoPoint(node_ref.id,node_ref.lon,node_ref.lat)
            self.repo.nodes[node_ref.id] = point

class RepoWayBuilder(Builder[osm.Node]):
    def __init__(self,repo:OSMRepository,filters:list[Filter]):
        self.repo = repo
        self.filters = filters

    def way(self,way_ref:osm.Way):
        need_keep = all(not filter(way_ref) for filter in self.filters)
        if not need_keep:
            return
        road_name = way_ref.tags.get("name",default="无名路") or "无名路"
        points = []
        poi_ids = set()
        link_id = way_ref.id
        for node in way_ref.nodes:
            if node.ref not in self.repo.nodes:
                continue
            gp = self.repo.nodes[node.ref]
            points.append(gp)
            poi_ids.add(node.ref)
            way_ids = set()
            if node.ref in self.repo.node_to_way:
                way_ids = self.repo.node_to_way[node.ref]
            way_ids.add(link_id)
            self.repo.node_to_way[node.ref] = way_ids

        if len(poi_ids) > 0:
            road = Road(link_id,points,0.0,road_name,osm.Box(0,0,0,0))
            self.repo.ways[link_id] = road
            self.repo.way_to_node[link_id] = poi_ids

