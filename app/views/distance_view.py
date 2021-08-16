from flask import request, jsonify, Blueprint
from app.services.get_coordinates import get_coordinates
from app.services.calculate_distance import calculate_distance
from app.services.log_services import create_id, read_logs, create_log
from app.exc import KeyError, ValidationError, TypeError, AddressError
from http import HTTPStatus


bp = Blueprint("distances", __name__, url_prefix="/api")


@bp.route("/distances/", methods=["POST"])
def post():
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
        return e.message,  HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return e.message,  HTTPStatus.BAD_REQUEST

    except AddressError as e:
        return e.message,  HTTPStatus.BAD_REQUEST
