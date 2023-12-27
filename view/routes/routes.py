from flask import render_template, make_response, request, session
import datetime
from view.view import view
from app import app

@view.route("/index", methods=['GET'])
def index():
    app.logger.info('Rendering Index page...!')
    render = make_response(render_template('index.html', utc_dt=datetime.datetime.utcnow()))
    render.set_cookie("Ajith-cookies", value="I am ajiths cookie..!")
    session['Ajith-session'] = "ajith-my-session"
    return render