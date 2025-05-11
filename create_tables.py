from app import create_app, db
from app.models.usina import Usina  
from app.models.inversor import Inversor  

app = create_app()

with app.app_context():
    db.create_all()
