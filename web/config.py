class Config:
	SECRET_KEY = 'catsareveryadorableandilovethem'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

class DeployConfig(Config):
	DEBUG = False


config = {
	'default': DevelopmentConfig,
	'deploy': DeployConfig,
}