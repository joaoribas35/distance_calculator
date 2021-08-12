import haversine as hs


def calculate_distance(coordinates):

    # coordinates from Saint Basil's Cathedral, located in the center of Moscow Ring Road
    loc1 = (55.75859164153293, 37.623173678442136)

    # coordinates from the address provided by client and distance
    loc2 = (coordinates['lat'], coordinates['lon'])
    distance = round(hs.haversine(loc1, loc2), 2)

    if distance <= 18:
        return 'null'

    return f'{distance} km'
