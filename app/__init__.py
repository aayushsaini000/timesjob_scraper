import os
from flask import Flask,jsonify,make_response
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from app import db
mongo = db.init_db()


#----------Import schedulers functions from files----------

from app.chainguardians_scheduler import Timesjobs,accountjobs,HRjobs,Salesjobs,marketingjobs,customerjobs,legaljobs,Teachingjobs,naukri_date_change


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


    naukri_date_change_scheduler = BackgroundScheduler()
    #naukri_date_change_scheduler.add_job(naukri_date_change, trigger='cron', day_of_week='mon-sat', hour=16,minute=39)
    naukri_date_change_scheduler.start()

    Timesjobs_scheduler = BackgroundScheduler()
    #Timesjobs_scheduler.add_job(Timesjobs, trigger='cron', day_of_week='mon-sat', hour=20,minute=00)
    Timesjobs_scheduler.start()

    accountjobs_scheduler = BackgroundScheduler()
    #accountjobs_scheduler.add_job(accountjobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    accountjobs_scheduler.start()

    HRjobs_scheduler = BackgroundScheduler()
    #HRjobs_scheduler.add_job(HRjobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    HRjobs_scheduler.start()

    Salesjobs_scheduler = BackgroundScheduler()
    #Salesjobs_scheduler.add_job(Salesjobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    Salesjobs_scheduler.start()

    marketingjobs_scheduler = BackgroundScheduler()
    #marketingjobs_scheduler.add_job(marketingjobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    marketingjobs_scheduler.start()

    customerjobs_scheduler = BackgroundScheduler()
    #customerjobs_scheduler.add_job(customerjobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    customerjobs_scheduler.start()

    legaljobs_scheduler = BackgroundScheduler()
    #legaljobs_scheduler.add_job(legaljobs, trigger='cron', day_of_week='mon-sun', hour=20,minute=00)
    legaljobs_scheduler.start()

    Teachingjobs_scheduler = BackgroundScheduler()
    Teachingjobs_scheduler.add_job(Teachingjobs, trigger='cron', day_of_week='mon-sun', hour=11,minute=49)
    Teachingjobs_scheduler.start()


    try:
        return app
    except:   
        Timesjobs_scheduler.shutdown()
        accountjobs_scheduler.shutdown()
        HRjobs_scheduler.shutdown()
        Salesjobs_scheduler.shutdown()
        marketingjobs_scheduler.shutdown()
        customerjobs_scheduler.shutdown()
        legaljobs_scheduler.shutdown()
        Teachingjobs_scheduler.shutdown()
        naukri_date_change_scheduler.shutdown()