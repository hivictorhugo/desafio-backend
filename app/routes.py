from . import app
from app.controllers.usina_controller import usina_bp
from app.controllers.inversor_controller import inversor_bp

# Registrando os blueprints
app.register_blueprint(usina_bp)
app.register_blueprint(inversor_bp)
