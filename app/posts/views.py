
from flask import jsonify, redirect, render_template, request, url_for

from app.models import Category, Posts 
from app.models import db
from app.posts import posts_blueprint
from app.posts.forms import Posts_Form, Category_Form


# def posts_index():
#     posts = Posts.get_all_posts()
#     return render_template('posts.html',  posts=posts)


# def show(id):
#     post = Posts.query.get_or_404(id)
#     return render_template('show.html', post=post)


# def delete(id):
#     post = Posts.query.get_or_404(id)
#     res = post.delete_object()
#     if res :
#         return redirect(url_for("posts_index"))


def notFound(error):
    return render_template("pagenotfound.html")



# =================================================================


@posts_blueprint.route('')
def posts_index():
    posts = Posts.get_all_posts()
    return render_template('posts.html', posts=posts)


@posts_blueprint.route('/<int:id>')
def show(id):
    posts = Posts.query.get_or_404(id)
    return render_template('show.html', posts=posts)


@posts_blueprint.route('/<int:id>/delete')#
def delete(id):
    posts = Posts.query.get_or_404(id)
    res =posts.delete_object()
    if res :
        return redirect(url_for("posts_index"))
# =====================================


@posts_blueprint.route('/addpost', methods=['POST', 'GET'], endpoint="addpost")
def addNewPost():
    form = Posts_Form()
    if request.method == 'GET':
        return render_template("addPost.html", form=form, category=Category.query.all())
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.form['image']
        category = request.form['category']
        data = Posts(title=title,
              body=body,
              image=image,
              category=category
              )
        db.session.add(data)
        db.session.commit()
        return redirect('/')

# ====================


@posts_blueprint.route('/update/<int:id>/', methods=('GET', 'POST'), endpoint="updatepost")
def update(id):
    form = Posts.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('update.html', form=form, category=Category.query.all())
    if request.method == 'POST':
        title = request.form['title']
        # title = request.form.get('title')
        if title is None:
            return jsonify({'error': 'Title is missing'}), 400
        
        body = request.form['body']
        image = request.form['image']
        category = request.form['category']
        form.title = title
        form.body = body
        form.image = image
        form.category = category
        db.session.add(form)
        db.session.commit()
        return redirect('/')
