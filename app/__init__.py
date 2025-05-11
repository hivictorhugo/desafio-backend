from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criando o objeto db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usinas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados
    db.init_app(app)

    # Aqui você registra o blueprint
    from app.controllers.usina_controller import usina_bp
    app.register_blueprint(usina_bp)

    return app
