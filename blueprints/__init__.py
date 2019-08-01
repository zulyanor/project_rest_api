from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from datetime import timedelta
from functools import wraps

import json, logging

app = Flask(__name__)

##############
# Database
##############

app.config['APP_DEBUG'] = True
app.config['SQLAlCHEMY_DATABSE_URI'] = 'mysql+pymysql://root:@localhost:3306/rest_project'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

######
# JWT
######

app.config['JWT_SECRET_KEY'] = 'tT9)2:u3ATYNTafx'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return identity


################################
# Middlewares (log)
###############################

@app.after_request # -> decorator
def after_request(response):
    # GET dikasih if karena pake param (tidak meneirma input body) jadi tidak bisa langsung get_json dan harus pake args
    try:
        if request.method == 'GET':  
            app.logger.warning("REQUEST_LOG\t%s", 
                json.dumps({
                    'method':request.method,
                    'code':response.status,
                    'uri':request.full_path,
                    'request':request.args.to_dict(), 
                    'response':json.loads(response.data.decode('utf-8'))
                    })
            )
        else:
            app.logger.warning("REQUEST_LOG\t%s", 
                json.dumps({
                    'uri':request.full_path,
                    'request':request.get_json(), 
                    'response':json.loads(response.data.decode('utf-8'))
                    })
            )
    except Exception as e:
        app.logger.error("REQUEST_LOG\t%s",
            json.dumps({
                'uri':request.full_path,
                'request':{}, 
                'response':json.loads(response.data.decode('utf-8'))
                })
        )
    return response

#####################
# Import Blueprints
#####################

from blueprints.auth import bp_auth


app.register_blueprint(bp_auth, url_prefix='/login')