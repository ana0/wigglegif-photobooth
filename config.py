
class Config:
	SECRET_KEY = 'catsareveryadorableandilovethem'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

config = {
	'default': DevelopmentConfig,
}