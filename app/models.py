#  relation related to database such as flask alchemy

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# create the object from sqlalchemy
db=SQLAlchemy()

class Category(db.Model):
     

    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    posts = db.relationship('Posts', backref='mycategory', lazy=True)

    def __str__(self):
        return f"{self.title}"
    
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(100))
    image = db.Column(db.String(100))
    category = db.Column(db.Integer, db.ForeignKey('categorys.id'),nullable=True)
    # created_at = db.Column(db.DateTime,nullable=False , default=datetime.utcnow)
    # updated_at = db.Column(db.Date)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True


# 
    def update_post(self, updated_data):
        self.title = updated_data["title"]
        self.body = updated_data["body"]
        self.image = updated_data["image"]
        db.session.add(self)
        db.session.commit()
        return True


