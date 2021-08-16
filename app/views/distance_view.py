from flask import request, jsonify, Blueprint
from app.services.get_coordinates import get_coordinates
from app.services.calculate_distance import calculate_distance
from app.services.log_services import create_id, read_logs, create_log
from app.exc import KeyError, ValidationError, TypeError, AddressError
from http import HTTPStatus


bp = Blueprint("distances", __name__, url_prefix="/api")


@bp.route("/distances/", methods=["POST"])
def post():
    """ This route will receive the the json provided in the request body, verify the coordinates of the provided address using Positionstack API, calculate the distance from one specific point of origin to the provided address and create a csv log file with the results. """

    data = request.get_json()

    try:
        location = get_coordinates(data)
        distance = calculate_distance(location)

        new_log = dict()
        new_log['id'] = create_id()
        new_log['address'] = location['label']
        new_log['distance'] = distance

        read_logs()
        create_log(new_log)

        return jsonify(new_log), HTTPStatus.CREATED

    except KeyError as e:
        return e.args[0],  HTTPStatus.BAD_REQUEST

    except ValidationError as e:
        return e.message,  HTTPStatus.UNPROCESSABLE_ENTITY

    except TypeError as e:
        return e.message,  HTTPStatus.UNPROCESSABLE_ENTITY

    except AddressError as e:
        return e.message,  HTTPStatus.NOT_FOUND
