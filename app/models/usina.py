from app import db

class Usina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    localizacao = db.Column(db.String(200))

    inversores = db.relationship('Inversor', backref='usina', lazy=True)
