

from flask import Blueprint

posts_blueprint = Blueprint('', __name__, url_prefix='/')

from app.posts import views
