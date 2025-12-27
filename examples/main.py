from pyosr.types import GeoPoint,Route
from pyosr.loader import load_osm_repo
from pyosr.router import DfsRouter

def extract_and_route(osm_file:str,config_path:str)->Route:
    ld = GeoPoint(0,116.26913,40.03741)
    ru = GeoPoint(0,116.27908,40.05083)
    repo = load_osm_repo(osm_file,None)
    router = DfsRouter(repo)
    route  = router(("zhang",ru))
    return route

def main():
    osm_file = "./road_data/bj251220.osm"
    conf_file = "./conf/conf.json"
    extract_and_route(osm_file,conf_file)

if __name__ == "__main__":
    main()
