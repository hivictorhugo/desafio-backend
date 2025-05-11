from flask import Flask
from app.extensions import db, migrate  # usa os objetos criados
from app.controllers.leitura_controller import leitura_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usinas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.usina_controller import usina_bp
    from app.controllers.inversor_controller import inversor_bp
    from app.controllers.leitura_controller import leitura_bp

    app.register_blueprint(usina_bp)
    app.register_blueprint(inversor_bp)
    app.register_blueprint(leitura_bp)

    return app

app = create_app()

from app.models.usina import Usina
from app.models.inversor import Inversor
from app.models.leitura import Leitura
