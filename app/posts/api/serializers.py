from flask_restful import fields
CategorySerilizer = {
    'id': fields.Integer,
    'title': fields.String,
}


postserilizer = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'image': fields.String,
}
