from collections import defaultdict
from .builders import OSM_T, Builder
import osmium
from osmium import osm

class Dispatcher():
    def __init__(self) -> None:
        self.listeners = defaultdict[str,list[Builder]](list)

    def register(self,event_type:str,listener:Builder):
        self.listeners[event_type].append(listener)

    def emit(self,event_type:str,entity:OSM_T):
        for lisenter in self.listeners[event_type]:
            lisenter(entity)

class OSMPublisher(osmium.SimpleHandler):
    def __init__(self,dispatcher:Dispatcher):
        super().__init__()
        self.dispatcher = dispatcher

    def node(self,node:osm.Node):
        self.dispatcher.emit("node",node)

    def way(self,way:osm.Way):
        self.dispatcher.emit("way",way)

    def relation(self,relation:osm.Relation):
        self.dispatcher.emit("relation",relation)

