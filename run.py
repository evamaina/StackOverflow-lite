import os

from app.app import create_app

try:
    config = os.environ['APP_SETTINGS'] # config_name = "development"
    app = create_app(config)
except KeyError:
    app = create_app('development')

if __name__ == '__main__':
	app.run()

    