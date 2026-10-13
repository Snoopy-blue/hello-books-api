from flask import Flask
from .db import db, migrate 
from .routes.book_routes import books_bp
from .models import book


def create_app():
    app = Flask(__name__)

    #先配置
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    #再连接
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app 

