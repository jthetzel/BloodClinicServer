"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from os.path import join
import json
from flask import (
  Flask,
  render_template,
  request,
  redirect,
  url_for,
  send_from_directory
  )
from flask_cors import CORS, cross_origin
# from dateutil.parser import parse
from iso8601 import parse_date
from prediction import get_prediction
from clinics import clinics_info


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.environ.get(
  'SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/js/<path:path>')
def send_static_js(path):
    """
    Serve static js files
    """
    return send_from_directory(join(app._static_folder, 'js'), path)


@app.route('/imgs/<path:path>')
def send_static_imgs(path):
    """
    Serve static imgs files
    """
    return send_from_directory(join(app._static_folder, 'imgs'), path)


@app.route('/css/<path:path>')
def send_static_css(path):
    """
    Serve static imgs files
    """
    return send_from_directory(join(app._static_folder, 'css'), path)


@app.route('/panel/<path:path>')
def send_static_panel(path):
    """
    Serve static imgs files
    """
    return send_from_directory(join(app._static_folder, 'panel'), path)


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
@cross_origin()
def api():
    """Render the website's about page."""
    error = False
    date = None
    payload = request.get_json(silent=True)
    if hasattr(payload, 'date'):
        date = payload['date']
    if hasattr(payload, 'clinics'):
        payload = payload['clinics']

    try:
        current_rate, daily_rates = get_prediction()
    except Exception as exception:
        error = exception

    message = {'error': error,
               'current_rate': current_rate,
               'daily_rates': daily_rates,
               'payload': payload}
    return json.dumps(message)


@app.route('/apiv2', methods=['GET', 'POST'])
@cross_origin()
def apiv2():
    error = []
    messages = ['Hello, front end!']
    date = None
    payload = request.get_json(silent=True)
    try:
        messages.append('Date in payload is {0}'.format(payload['date']))
        date = parse_date(payload['date'])
        messages.append('Date is {0}'.format(date))
    except:
        messages.append('Could not find date in payload')

    if hasattr(payload, 'clinics'):
        payload = payload['clinics']
    try:
        messages.append('Getting predictions with date {0}'.format(date))
        current_rate, daily_rates = get_prediction(date)
    except Exception as exception:
        error.append(exception)

    message = {'error': error,
               'messages': messages,
               'current_rate': current_rate,
               'daily_rates': daily_rates,
               'payload': payload,
               'date': date}
    return json.dumps(message)


###
# The functions below should be applicable to all Flask apps.
###


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
