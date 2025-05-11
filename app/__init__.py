from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.controllers.leitura_controller import leitura_bp

# Criando o objeto db
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usinas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True

    # Inicializa o banco de dados
    db.init_app(app)
    migrate.init_app(app, db)

    # Aqui você registra o blueprint
    from app.controllers.usina_controller import usina_bp
    from app.controllers.inversor_controller import inversor_bp
    
   
    app.register_blueprint(usina_bp)
    app.register_blueprint(inversor_bp)
    app.register_blueprint(leitura_bp)

    return app

app = create_app()

from app.models.usina import Usina
from app.models.inversor import Inversor
