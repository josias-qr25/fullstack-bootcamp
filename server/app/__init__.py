from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    # ✅ Enable CORS for API routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # ✅ Register Blueprints
    from app.routes.health import health_bp
    from app.routes.todo_routes import todo_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(todo_bp)

    from app.models import todo

    return app
