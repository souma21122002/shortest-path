import math

RADIUS_EARTH_KM = 6371

def to_radians(degree):
    return degree * (math.pi / 180)

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1 = to_radians(lat1)
    lon1 = to_radians(lon1)
    lat2 = to_radians(lat2)
    lon2 = to_radians(lon2)

    dlong = lon2 - lon1
    dlat = lat2 - lat1

    ans = math.pow(math.sin(dlat / 2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(dlong / 2), 2)
    ans = 2 * math.asin(math.sqrt(ans))

    return ans * RADIUS_EARTH_KM