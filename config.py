import os
from dotenv import load_dotenv

load_dotenv()


# # 2. config.py
# # Responsabilidad:
# # Guardar configuraciones.

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False