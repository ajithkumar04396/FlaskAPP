from flask import render_template, make_response, request, session, url_for
import datetime
from view.view import view
from app import app
import os

@view.route("/index", methods=['GET'])
def index():
    app.logger.info('Rendering Index page...!')
    renderImage = url_for('view.static', filename = 'media/img/code.jpeg')
    render = make_response(render_template('index.html', utc_dt=datetime.datetime.utcnow().strftime("%B %d %Y"), img_res = renderImage))
    render.set_cookie("Ajith-cookies", value="I am ajiths cookie..!")
    session['Ajith-session'] = "ajith-my-session"
    return render