from typing import Protocol
from .types import OdPair,Route
from .repository import OSMRepository
from .config import OsrConfig
class Router(Protocol):
    def __call__(self,OdPair)->Route:
        ...


class DfsRouter(Router):
    repo:OSMRepository

    def __init__(self,repo:OSMRepository,conf:OsrConfig):
        self.repo = repo

    def __call__(self,od:OdPair)->Route:
        return Route()

