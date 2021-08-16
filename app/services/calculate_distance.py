import haversine as hs


def calculate_distance(coordinates):
    """ Will calculate the distance from Saint Basil's Cathedral and the address provided by client usind Haversine python lib. Saint Basil's Cathedral is used as an approximation to define whether the provided address is located inside the MKAD Moscow Ring Road (MKAD) or not. It's location is the center point to a 18 km radius circle. Will return a null string indicating the address is inside MKAD or a string with the distance expressed in kilometers if the address falls outside the MKAD. """

    loc1 = (55.75859164153293, 37.623173678442136)

    loc2 = (coordinates['lat'], coordinates['lon'])
    distance = round(hs.haversine(loc1, loc2), 2)

    if distance <= 18:
        return 'null'

    return f'{distance} km'
