from flask import Flask
from config import Config
from app.extension import db, migrate
import app.models

# ============
# Blueprints
# ============
from .routes.cursos import curso_bp
from .routes.admin import admin_bp
from .routes.clase import clase_bp




def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(curso_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(clase_bp)

    return app