from app import create_app, db
from app.models.usina import Usina  # Importando o modelo Usina
from app.models.inversor import Inversor  # Importando o modelo Inversor

app = create_app()

with app.app_context():
    db.create_all()
