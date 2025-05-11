from app import db
from datetime import datetime

class Leitura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inversor_id = db.Column(db.Integer, db.ForeignKey('inversor.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    potencia_ativa_watt = db.Column(db.Float, nullable=False)
    temperatura_celsius = db.Column(db.Float, nullable=False)

    inversor = db.relationship('Inversor', backref='leituras', lazy=True)

    def __init__(self, inversor_id, data, potencia_ativa_watt, temperatura_celsius):
        self.inversor_id = inversor_id
        self.data = data
        self.potencia_ativa_watt = potencia_ativa_watt
        self.temperatura_celsius = temperatura_celsius
