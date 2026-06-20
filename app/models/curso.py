from app.extension import db


class Curso(db.Model):

    __tablename__ = "curso"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    imagen = db.Column(db.String(255), nullable=True, default='default.jpg')
