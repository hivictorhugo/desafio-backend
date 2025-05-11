from app import db

class Inversor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usina_id = db.Column(db.Integer, db.ForeignKey('usina.id'), nullable=False)
    potencia_maxima = db.Column(db.Float, nullable=False)
    temperatura = db.Column(db.Float)

