from flask import Flask

from .distance_view import bp as bp_distances


def init_app(app: Flask):
    app.register_blueprint(bp_distances)
