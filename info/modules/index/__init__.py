from flask import Blueprint

index_blu = Blueprint("index",__name__,url_prefix="/index")

from .views import  *