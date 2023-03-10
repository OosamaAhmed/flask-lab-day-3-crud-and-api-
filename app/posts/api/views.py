from flask_restful import Resource, Api, marshal_with, abort
from app.models import Posts
from app.posts.api.serializers import postserilizer
from app.posts.api.parser import postparser
from app.models import db


class AllPosts(Resource):
    @marshal_with(postserilizer)
    def get(self):
        posts = Posts.query.all()
        return posts

    @marshal_with(postserilizer)
    def post(self):
        posts = postparser.parse_args()
        post = Posts(**posts)
        db.session.add(post)
        db.session.commit()
        return post, 201


class PostGetSpecificAndUpdateAndDelete(Resource):
    @marshal_with(postserilizer)
    def get(self, id):
        post = Posts.query.get(id)
        if post:
            return post, 200

        return abort(404, message="post not found")

    @marshal_with(postserilizer)
    def put(self, id):
        post = Posts.query.get(id)
        if post:
            post_args = postparser.parse_args()
            post.update_post(post_args)
            return post, 200

        return abort(205, message="post not found")

    def delete(self, id):
        post = Posts.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return {"deleted": "the post Deleted"}
        return 'page not found ',404
