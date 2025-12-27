from pydantic import BaseModel, Field
from typing import Literal
import toml

class OSMInputConfig(BaseModel):
    osm_file: str = Field(..., description="Path to osm.pbf file")
    load_relations: bool = True
    bound_name:tuple[str,str] = ("","")
    bound_lon_lat:tuple[float,float,float,float] = (0,0,0,0)

class BuilderConfig(BaseModel):
    enable_graph_builder: bool = True
    enable_way_builder: bool = True
    enable_node_builder: bool = True

class RouterConfig(BaseModel):
    algorithm: Literal["dijkstra", "astar"] = "astar"
    heuristic_factor: float = 1.0

class OsrConfig(BaseModel):
    input: OSMInputConfig
    builder: BuilderConfig = BuilderConfig()
    router: RouterConfig = RouterConfig()

def load_config(conf_path:str)->OsrConfig:
    raw = toml.load(conf_path)
    return OsrConfig(**raw)
