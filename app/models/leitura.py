from app.extensions import db

class Leitura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inversor_id = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    potencia_ativa_watt = db.Column(db.Float, nullable=False)
    temperatura_celsius = db.Column(db.Float, nullable=False)
