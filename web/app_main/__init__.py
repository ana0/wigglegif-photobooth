from flask import Flask, render_template
from flask_wtf import CsrfProtect

from config import config

crsf = CsrfProtect()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	return app

app = create_app('default')

import app_main.views