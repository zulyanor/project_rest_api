from blueprints import db
from flask_restful import fields

class Client(db.Model):
    __tablename__ = "client"
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_key = db.Column(db.String, unique=True, nullable=True)
    client_secret = db.Column(db.String, unique=True, nullable=True)
    status = db.Column(sb.Boolean, nullable=False)

    response_fields = {
        'client_id':fields.Integer,
        'client_key':fields.String,
        'client_secret':fields.String,
        'status':fields.Boolean
    }

    jwt_response_field = {
        'client_id':fields.Integer,
        'status':fields.Boolean
    }

    def __init__(self, client_key, client_secret, status):
        self.client_key = client_key
        self.client_secret = client_secret
        self.status = status
    
    def __repr__(self):
        return '<Client %r>' % self.client_id