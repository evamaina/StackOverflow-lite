import os

from app.app import create_app

app = create_app(config=os.getenv("CONFIG"))

if __name__ == '__main__':
	app.run()

    