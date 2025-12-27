from typing import Protocol

from .lookup import MapMatcher
from .types import Graph, OdPair, Path,Route,GeoPoint
from .repository import OSMRepository
from .config import OsrConfig
from .rgeo import rgeo
class Router(Protocol):
    def __call__(self,OdPair)->Route:
        ...


class DfsRouter(Router):
    repo:OSMRepository

    def __init__(self,repo:OSMRepository,conf:OsrConfig):
        self.repo = repo
        self.mm = MapMatcher(repo.looker)

    def __call__(self,od:OdPair)->Route:
        link_pair = self._mapmatch(od)
        if not link_pair:
            return Route()
        o_link,d_link = link_pair
        links = self._dfs(self.repo.graph,o_link,d_link,{})
        route = Route()

        for link_id in reversed(links):
            way = self.repo.ways[link_id]
            path = Path(link_id,way.points,way.road_len,0,way.road_name)
            route.paths.append(path)

        return route

    def _dfs(self,graph:Graph,o_link:int,d_link:int,visited:dict[int,bool])->list[int]:
        if o_link == d_link:
            return [o_link]
        return []
    def _mapmatch(self,od:OdPair)->tuple[int,int]|None:
        o,d = od
        match (o,d):
            case (GeoPoint() as o_pt,GeoPoint() as d_pt):
                o_link,d_link = self.mm(o_pt),self.mm(d_pt)
                if o_link and d_link:
                    return (o_link,d_link)

            case (int() as o_link,int() as d_link):
                return (o_link,d_link)

            case (str() as o_name,str() as d_name):
                o_point,d_point = rgeo(o_name),rgeo(d_name)
                if not o_point or not d_point:
                    return None
                else:
                    o_link,d_link = self.mm(o_point),self.mm(d_point)
                    if o_link and d_link:
                        return (o_link,d_link)
            case _:
                return None
        return None
