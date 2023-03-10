# importing flusk
# run app
from app.posts.api.views import AllPosts, PostGetSpecificAndUpdateAndDelete
from flask_restful import Api

from flask import Flask
from app.models import db
from flask_migrate import Migrate


from app.config import projectConfig as AppConfig
from app.posts.views import  posts_index, show, delete, notFound


def create_app(config_name):

    #  production or development from config file
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config['SECRET_KEY'] = current_config.SECRET_KEY #for securety key


    app.config.from_object(current_config)
    db.init_app(app)
# add route
    # app.add_url_rule('/', view_func=posts_index)
    # app.add_url_rule('/post/<id>', view_func=show)
    # app.add_url_rule('/post/<id>/delete', view_func=delete)
    app.register_error_handler(404, notFound)

    migrate = Migrate(app, db, render_as_batch=True)
# blue prints
    from app.category import category_blueprint
    from app.posts import posts_blueprint
    app.register_blueprint(category_blueprint)
    app.register_blueprint(posts_blueprint)


#
    api = Api(app)
    api.add_resource(AllPosts, '/api/posts')
    api.add_resource(PostGetSpecificAndUpdateAndDelete, '/api/posts/<int:id>')



    return app
