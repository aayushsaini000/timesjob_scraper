import os
from flask import Flask,jsonify,make_response
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from app import db
mongo = db.init_db()


#----------Import schedulers functions from files----------

from app.chainguardians_scheduler import Timesjobs


#----------created app functionality----------

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()
    CORS(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify(error='Not found'), 400)

    @app.errorhandler(500)
    def error_500(error):
        return make_response({}, 500)

    db.get_db(mongo=mongo, app=app)

    from app.api import fetch

    app.register_blueprint(fetch.bp)


#-----------Date time Settings of chainguardians schedulers--------------

    Timesjobs_scheduler = BackgroundScheduler()
    Timesjobs_scheduler.add_job(Timesjobs, trigger='cron', day_of_week='mon-sun', hour=00,minute=54)
    #Timesjobs_scheduler.add_job(Timesjobs, trigger='interval', minutes =3000)#30
    Timesjobs_scheduler.start()

    try:
        return app
    except:   
        Timesjobs_scheduler.shutdown()
