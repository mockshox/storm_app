from celery import Celery
from flask import Flask, render_template

from app.utils import config, storm_info

app = Flask(__name__)
celery = Celery()
app.is_storm = None


@celery.task
def update_storm_info(app, app_config):
    app.is_storm = storm_info.is_storm_in_location(app, app_config)


@app.route('/')
def storm_app ():
    app_config = config.get_config()

    update_storm_info(app, app_config)
    return render_template('app.html.j2', is_storm_in_location=app.is_storm)