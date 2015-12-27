from flask import Flask, render_template
from flask_wtf import CsrfProtect

from config import config

crsf = CsrfProtect()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	crsf.init_app(app)

	#let flask know which instance of the app 'app' is
	# with app.app_context():
		#db.drop_all()


	return app