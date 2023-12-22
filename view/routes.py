from app import app
from flask import render_template
import datetime

@app.route("/view/index", methods=['GET'])
def index():
    app.logger.info('Rendering Index page...!')
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())