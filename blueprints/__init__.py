from flask import Flask, request
import json
## Import yang dibutuhkan untuk database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from datetime import timedelta
from functools import wraps

app = Flask(__name__)

###################################
# JWT
###################################

app.config['JWT_SECRET_KEY'] = 'AuliaBukuCommerceSecret' # Bisa bebas
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

# jwt custom decorator
# @jwt.user_claims_loader # Terima kasih atas perjuangan anda
# def add_claims_to_access_token(identity):
#     return {
#         'claims': identity,
#         'identifier': 'ATA-Batch3'
#     }

## Buat Decorator untuk internal only
def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['status']: # If berjalan jika statement True, jadi 'not False' = True
            return {'status': 'FORBIDDEN', 'message': 'Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

## Buat Decorator untuk non-internal
def non_internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['status']: # If berjalan jika statement True, jadi 'not False' = True
            return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


## Setting Database
app.config['APP_DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/bukucommerce' # localhost aka 127.0.0.1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# log error (middlewares)
@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()

    app.logger.warning("REQUEST_LOG\t%s", 
        json.dumps({
            'method': request.method,
            'code': response.status,
            'uri':request.full_path, 
            'request': requestData, 
            'response': json.loads(response.data.decode('utf-8'))
            }))
    
    # we could use code above or code below, but the code above is more efficient

    # try:
    #     if request.method == 'GET':
    #         app.logger.warning("REQUEST_LOG\t%s", json.dumps({'uri':request.full_path, 'request': request.args.to_dict(), 'response': json.loads(response.data.decode('utf-8'))}))
            
    #     else:
    #             app.logger.warning("REQUEST_LOG\t%s", json.dumps({'uri':request.full_path, 'request': request.get_json(), 'response': json.loads(response.data.decode('utf-8'))}))
    # except Exception as e:
    #     app.logger.error("REQUEST_LOG\t%s", json.dumps({'uri':request.full_path, 'request': {}, 'response': json.loads(response.data.decode('utf-8'))}))

    return response


# import blueprints

from blueprints.auth import bp_auth
from blueprints.datareq.resources import bp_datareq
from blueprints.client.resources import bp_client
from blueprints.apiluar.resources import bp_apiluar 

app.register_blueprint(bp_auth, url_prefix='/login')
app.register_blueprint(bp_client, url_prefix='/client')
app.register_blueprint(bp_datareq, url_prefix='/datareq')
app.register_blueprint(bp_apiluar, url_prefix='/apiluar')
db.create_all()

