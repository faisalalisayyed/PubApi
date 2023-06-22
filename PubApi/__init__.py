from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config.py')
cache = Cache(app,config={'CACHE_TYPE': 'SimpleCache'})
db = SQLAlchemy(app)

from PubApi import views