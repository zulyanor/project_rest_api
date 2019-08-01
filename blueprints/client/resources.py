from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from flask_jwt_extended import jwt_required
from sqlalchemy import desc
from .model import Client
import json

from blueprints import db, app

bp_client = Blueprint('client', __name__)
api_client = Api(bp_client)

class ClientResource(Resource):

    def get(self, client_id):
        qry = Client.query.get(client_id)
        if qry is not None:
            return marshal(qry, Client.response_fields), 200
        return {'status':'NOT_FOUND'}, 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', location='json', type=bool, required=True)
        data = parser.parse_args()

        client = Client(data['client_key'], data['client_secret'], data['status'])
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG: %s', client)

        return marshal(client, Client.response_fields), 200, {'Content-Type':'application/json'}
    
    def put(self, client_id):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', location='json', type=bool, required=True)
        args = parser.parse_args()

        qry = Client.query.get(client_id)
        if qry is None:
            return {'status':'NOT_FOUND'}, 404
        
        qry.client_key = args['client_key']
        qry.client_secret = args['client_secret']
        qry.status = args['status']

        return marshal(qry, Client.response_fields), 200
    
    def delete(self, client_id):
        qry = Client.query.get(client_id)
        if qry is None:
            return {'status':'NOT_FOUND'}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'status':'DELETED'}, 200

class ClientList(Resource):

    def __init__(self):
        pass
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Client.query

        row = []
        for baris in qry.limit(args['rp']).offset(offset).all():
            row.append(marshal(baris, Client.response_fields))
        
        return row, 200

api_client.add_resource(ClientList, '', '/list')
api_client.add_resource(ClientResource, '', '/<client_id>')

