from flask import Blueprint
from flask_restful import Resource, reqparse, Api
import requests, json
from flask_jwt_extended import jwt_required
from blueprints.datareq.model import Datareqs

bp_weather = Blueprint('weather', __name__)
api = Api(bp_weather)

class BestPersonalizedRecommendation(Resource):
    wio_host = 'https://api.weatherbit.io/v2.0'
    wio_apikey = '001de4440e814c16bc45197fd601ef9d'
    bl_host = 'https://api.bukalapak.com/v2/products.json'

    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', location='args', default=None)
        parser.add_argument('gaya', location='args', required=True)
        parser.add_argument('your_weekend', location='args', required=True)
        args = parser.parse_args()

        rq = requests.get(self.wio_host + '/ip', params={'ip': args['ip'], 'key': self.wio_apikey})
        geo = rq.json()
        lat = geo['latitude']
        lon = geo['longitude']
        rq = requests.get(self.wio_host + '/current', params={'lat': lat, 'lon': lon, 'key': self.wio_apikey})
        current = rq.json()

        code_weather = current['data'][0]['weather']['code']
        
        
        qry = {}        

        if code_weather <= 799 or code_weather == 900  :
            if args['gaya'] == 'hype':
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(1)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(2)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(3)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(4)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(5)
            elif args['gaya'] == 'kampung' :
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(6)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(7)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(8)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(9)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(10)
            elif args['gaya'] == 'biasa':
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(11)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(12)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(13)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(14)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(15)
        else:
            if args['gaya'] == 'hype':
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(16)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(17)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(18)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(19)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(20)
            elif args['gaya'] == 'kampung' :
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(21)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(22)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(23)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(24)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(25)
            elif args['gaya'] == 'biasa':
                if args['your_weekend'] == 'olahraga':
                    qry = Datareqs.query.get(26)
                elif args['your_weekend'] == 'nongkrong':
                    qry = Datareqs.query.get(27)
                elif args['your_weekend'] == 'baca':
                    qry = Datareqs.query.get(28)
                elif args['your_weekend'] == 'family':
                    qry = Datareqs.query.get(29)
                elif args['your_weekend'] == 'outdoor':
                    qry = Datareqs.query.get(30)
        
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        rq = requests.get(self.bl_host + '', params={'page': qry.page, 'per_page': qry.per_page, 'keywords': qry.keywords})
        current = rq.json()

        return {"products": current["products"]}
    
        
        

api.add_resource(BestPersonalizedRecommendation, '')


