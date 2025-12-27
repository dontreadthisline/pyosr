from opencage.geocoder import OpenCageGeocode
from .types import GeoPoint

KEY = "fe07c90b6b7647da9ec8ee44a5a7a15e"
geocoder = OpenCageGeocode(KEY)

def rgeo(loc_name: str) -> GeoPoint | None:
    results = geocoder.geocode(loc_name)
    if not results:
        return None
    result = results[0]  # type: ignore
    geometry = result.get("geometry", {}) # pyright: ignore
    lat = geometry.get("lat") # pyright: ignore
    lng = geometry.get("lng") # pyright: ignore
    if not lat or not lng:
        return None
    return GeoPoint(0,float(lng), float(lat))
