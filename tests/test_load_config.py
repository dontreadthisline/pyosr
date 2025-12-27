import pytest
from pyosr.config import load_config
from pprint import pprint

def test_load_config():
    conf_path = "./config.toml"
    conf = load_config(conf_path)
    pprint(conf)
    assert all(conf.input.bound_name)==True
