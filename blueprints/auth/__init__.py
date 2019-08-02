from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.client.model import Client
bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', type=str, location='args', required=True)
        parser.add_argument('client_secret', type=str, location='args', required= True)
        args = parser.parse_args()

        qry = Client.query

        qry = qry.filter_by(client_key=args['client_key'])
        qry = qry.filter_by(client_secret=args['client_secret']).first()
        
        if qry is not None:
            client_data= marshal(qry, Client.response_fields)
            client_data.pop("client_secret")
            token = create_access_token(identity=args['client_key'], user_claims=client_data)
        else:
            return {'status': 'UNATHORIZED', 'message': 'invalid key or secret'}, 401
        return {'token': token}, 200

class RefreshTokenResource(Resource):

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        token = create_access_token(identity=current_user)
        return {'token':token, 'identity':current_user}, 200


api.add_resource(CreateTokenResource, '')
api.add_resource(RefreshTokenResource, '/refresh')
        