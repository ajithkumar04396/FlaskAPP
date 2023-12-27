from flask import Blueprint
restApi = Blueprint('restApi',__name__,url_prefix="/rest-api/v1.0")
from .api import api