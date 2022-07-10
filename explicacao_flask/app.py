import views
from flask import Flask

def create_app():
    """Factory Principal"""
    """Resolve problema de circular import"""
    app = Flask(__name__)
    views.init_app(app)
    return app