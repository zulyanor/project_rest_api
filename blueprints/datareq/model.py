from blueprints import db
from flask_restful import fields
from blueprints import client

class Datareqs(db.Model):
    __tablename__ = "datareqs"

    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.Integer, nullable=False)
    per_page = db.Column(db.Integer, nullable=False)
    keywords = db.Column(db.String(50), nullable=False)

    response_fields = {
        'id': fields.Integer,
        'page': fields.Integer,
        'per_page': fields.Integer,
        'keywords': fields.String       
    }

    def __init__(self, page, per_page, keywords):
        self.page = page 
        self.per_page = per_page
        self.keywords = keywords 
    def __repr__(self):
        return '<Datareq %r>' % self.id