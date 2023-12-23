from flask import Blueprint
view = Blueprint('view',__name__,url_prefix="/view",template_folder="templates",static_folder="static")
from .routes import routes