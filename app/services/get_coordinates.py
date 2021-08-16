import requests
from environs import Env
from app.exc import KeyError, ValidationError, TypeError, AddressError


env = Env()
env.read_env()


API_KEY = env("API_KEY")


def verify_input_keys(data: dict):
    required_keys = ["address"]
    keys = data.keys()

    return [key for key in required_keys if key not in keys]


def verify_error(data: dict):
    verifying_keys = ["error"]
    keys = data.keys()

    return [key for key in verifying_keys if key in keys]


def get_coordinates(data: dict):

    if verify_input_keys(data):
        raise KeyError

    address = data['address']
    if not type(address) == str:
        raise TypeError

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
