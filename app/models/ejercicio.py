from app.extension import db



class Ejercicio(db.Model):

    __tablename__ = "ejercicio"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    solucion = db.Column(db.Text)
    clase_id = db.Column(db.Integer, db.ForeignKey("clase.id"), nullable=False)
