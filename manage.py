import os

from app import create_app
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
Migrate(app=app)

if __name__ == '__main__':
    app.run()
