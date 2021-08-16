import requests
from environs import Env
from app.exc import KeyError, ValidationError, TypeError, AddressError
from app.services.helpers import verify_input_keys, verify_error


env = Env()
env.read_env()


API_KEY = env("API_KEY")  # your API Key as set in env file.


def get_coordinates(data: dict):
    """ Will get the coordinates based on a provided address returning its latitude, longitude and full address as per Positionstack API. """

    if verify_input_keys(data):
        raise KeyError

    address = data['address']
    if not type(address) == str:
        raise TypeError

    # format string as per Positionstack API requirement removing spaces.
    input = address.replace(' ', '%20')

    url = f'http://api.positionstack.com/v1/forward?access_key={API_KEY}&query={input}'

    response = requests.get(url).json()

    if verify_error(response):
        raise ValidationError(response)

    if not response['data']:
        raise AddressError

    lat = (response['data'][0]['latitude'])
    lon = (response['data'][0]['longitude'])
    label = (response['data'][0]['label'])

    return {'lat': lat, 'lon': lon, 'label': label}
