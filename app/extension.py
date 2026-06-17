from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




# 1. extension.py
# Responsabilidad:
# Crear las extensiones UNA SOLA VEZ.

db = SQLAlchemy()
migrate = Migrate()

