import os
from flask_migrate import Migrate
from app import create_app, db
# from app.models import User, Products, Categories


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, products=Products, categories=Categories)
