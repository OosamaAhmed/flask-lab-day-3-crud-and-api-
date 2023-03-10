

from flask import render_template
from app.models import Category
from app.category import category_blueprint


@category_blueprint.route('/')
def category_index():
    categories = Category.query.all()
    return render_template('catshow.html', categories=categories)

