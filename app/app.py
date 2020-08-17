from flask import Flask, render_template
from flask_apscheduler import APScheduler

from app.utils import config, storm_info

app = Flask(__name__)
scheduler = APScheduler()

app.storm_config = config.get_config()
app.is_storm = None

scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

@scheduler.task('interval', id='update', seconds=60, misfire_grace_time=900)
@app.before_first_request
def update_storm_info():
    app.is_storm = storm_info.is_storm_in_location(app)


@app.route('/')
def storm_app():
    return render_template('app.html.j2', is_storm_in_location=app.is_storm)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
