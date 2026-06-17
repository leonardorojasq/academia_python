from app.extension import db

class Clase(db.Model):

    __tablename__ = "clase"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(150), nullable=True)
    video = db.Column(db.String(150), nullable=True)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), nullable=False)