from flask import request, jsonify, Blueprint
from app.services.get_coordinates import get_coordinates
from app.services.calculate_distance import calculate_distance
from app.services.log_services import create_id, read_logs, create_log
from http import HTTPStatus


bp = Blueprint("distances", __name__, url_prefix="/api")


@bp.route("/distances/", methods=["POST"])
def post():
    data = request.get_json()

    address = data['address']
    coordinates = get_coordinates(address)
    distance = calculate_distance(coordinates)

    new_log = dict()
    new_log['id'] = create_id()
    new_log['address'] = data['address']
    new_log['distance'] = distance

    read_logs()
    create_log(new_log)

    return jsonify(new_log), HTTPStatus.CREATED
