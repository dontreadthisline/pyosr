from pyosr.types import Route
from pyosr.loader import load_osm_repo
from pyosr.router import DfsRouter
from pyosr.config import OsrConfig,load_config

def extract_and_route(config_path:str)->Route:
    osr_conf = load_config("../config.toml")
    repo = load_osm_repo(osr_conf)
    router = DfsRouter(repo,osr_conf)
    origin = "天通苑"
    distination = "西二旗"
    route  = router((origin,distination))
    return route

def main():
    extract_and_route("")
if __name__ == "__main__":
    main()
