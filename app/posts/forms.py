from flask_wtf import FlaskForm
from wtforms import StringField
from app.models import Posts
from wtforms import BooleanField


class Posts_Form(FlaskForm):
    title = StringField('title')
    body = StringField('body')
    image = StringField('image')



class Category_Form(FlaskForm):
    title = StringField('Cat Name label')
    desc = StringField('description label')
