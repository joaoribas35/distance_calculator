import haversine as hs


def calculate_distance(coordinates):
    """ Will calculate the distance from Saint Basil's Cathedral and the address provided by client usind Haversine python lib. Saint Basil's Cathedral is used as an approximation to define whether the provided address is located inside the MKAD Moscow Ring Road (MKAD) or not. It's location is the center point to a 18 km radius circle. Will return a null string indicating the address is inside MKAD or a string with the distance from MKAD border, expressed in kilometers, if the address falls outside the MKAD. """

    CENTER_POINT = (55.75859164153293, 37.623173678442136)
    CIRCLE_RADIUS = 18

    input_address = (coordinates['lat'], coordinates['lon'])
    distance = hs.haversine(CENTER_POINT, input_address)

    if distance <= CIRCLE_RADIUS:
        return 'null'

    distance_from_border = round(distance - CIRCLE_RADIUS, 2)

    return f'{distance_from_border} km'
