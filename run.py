import os

from app.app import create_app
from app.manage import create_tables

app = create_app(config=os.getenv("CONFIG"))

create_tables()

if __name__ == '__main__':
	app.run(debug=True)

    