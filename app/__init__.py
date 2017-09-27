# -*- coding: utf-8 -*-

__version__ = '1.0.0'

from flask import Flask


app = Flask(__name__)


from app.views import main_views
