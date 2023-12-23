from flask import render_template
import datetime
from view.view import view
from app import app

@view.route("/index", methods=['GET'])
def index():
    app.logger.info('Rendering Index page...!')
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())