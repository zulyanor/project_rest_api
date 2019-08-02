from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from . import * 
from .model import Datareqs
from flask_jwt_extended import jwt_required
from blueprints import db, app, internal_required


bp_datareq = Blueprint('datareq', __name__) 
api = Api(bp_datareq)

class DatareqResource(Resource):


    def __init__(self): # Hanya untuk menunjukkan bahwa ini class
        pass
    @jwt_required
    def get(self, id):
        qry = Datareqs.query.get(id)
        if qry is not None:
            return marshal(qry, Datareqs.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', location='json', required=True) # required means that system will return error message if it doesn'_internalt found this parameter
        parser.add_argument('per_page', location='json', required=True)
        parser.add_argument('keywords', location='json', required=True) # required bisa ada bisa juga ngga. Jika ada maka jika tidak diisi akan error
        args = parser.parse_args()

        client = Datareqs(args['page'], args['per_page'], args['keywords'])
        
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client)

        return marshal(client, Datareqs.response_fields), 200, {'Content-Type': 'application/json'}
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('page', location='json', required=True) # required means that system will return error message if it doesn't found this parameter
        parser.add_argument('per_page', location='json', required=True)
        parser.add_argument('keywords', location='json', required=True) # required bisa ada bisa juga ngga. Jika ada maka jika tidak diisi akan error
        args = parser.parse_args()

        qry = Datareqs.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        qry.page = args['page']
        qry.per_page = args['per_page']
        qry.keywords = args['keywords']
        db.session.commit()

        return marshal(qry, Datareqs.response_fields), 200
    @jwt_required
    @internal_required
    def delete(self, id):
        qry = Datareqs.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        db.session.delete(qry)
        db.session.commit()

        return {'status': 'DELETED'}, 200

    def patch(self):
        return 'Not yet implemented', 501 

class DatareqList(Resource):

    def __init__(self):
        pass
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('keywords', location='args', help='invalid status')
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Datareqs.query

        if args['keywords'] is not None:
            qry = qry.filter(Datareqs.client_id.contains(args['keywords']))

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Datareqs.response_fields))
        
        return rows, 200

api.add_resource(DatareqList, '', '/list')
api.add_resource(DatareqResource, '', '/<id>') 