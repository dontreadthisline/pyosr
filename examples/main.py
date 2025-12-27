from pyosr.types import Route
from pyosr.loader import load_osm_repo
from pyosr.router import DfsRouter
from pyosr.config import load_config
from pprint import pprint
def extract_and_route(config_path:str)->Route:
    osr_conf = load_config(config_path)
    repo = load_osm_repo(osr_conf)
    pprint(repo.graph)
    print(len(repo.graph))
    print(len(repo.ways))
    print(len(repo.nodes))
    router = DfsRouter(repo,osr_conf)
    origin = "天通苑"
    distination = "西二旗"
    route  = router((origin,distination))
    print(len(repo.looker))
    return route

def main():
    conf_path = "./config.toml"
    extract_and_route(conf_path)
if __name__ == "__main__":
    main()
