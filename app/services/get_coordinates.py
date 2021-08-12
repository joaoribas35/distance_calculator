import requests
from environs import Env

env = Env()
env.read_env()


API_KEY = env("API_KEY")


def get_coordinates(address):
    input = address.replace(' ', '%20')

    url = f'http://api.positionstack.com/v1/forward?access_key={API_KEY}&query={input}'

    coordinates = requests.get(url).json()
    lat = (coordinates['data'][0]['latitude'])
    lon = (coordinates['data'][0]['longitude'])

    return {'lat': lat, 'lon': lon}
