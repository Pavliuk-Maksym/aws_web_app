from flask import Flask
from .s3 import s3_bp
from .home import home_bp


def register_blueprints(app: Flask):
    app.register_blueprint(s3_bp)
    app.register_blueprint(home_bp)
