from rtree import index
from .types import OdPointLiker
class MapMatcher():

    rtree:index.Index
    dist_thresh:float


    def __init__(self,rtree:index.Index,dist_thresh:float=10) -> None:
        self.rtree = rtree
        self.dist_thresh = dist_thresh

    def __call__(self,point:OdPointLiker)->int|None:
        return None
