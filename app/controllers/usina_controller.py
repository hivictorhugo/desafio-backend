from flask import Blueprint, request, jsonify
from app import db
from app.models.usina import Usina
from app.schemas.usina_schema import UsinaSchema

usina_bp = Blueprint('usina', __name__)
usina_schema = UsinaSchema()
usinas_schema = UsinaSchema(many=True)


@usina_bp.route('/usinas', methods=['POST'])
def criar_usina():
    data = request.get_json()
    errors = usina_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    nova_usina = Usina(**data)
    db.session.add(nova_usina)
    db.session.commit()
    return usina_schema.dump(nova_usina), 201  # Usando dump em vez de jsonify

@usina_bp.route('/usinas', methods=['GET'])
def listar_usinas():
    usinas = Usina.query.all()
    return usinas_schema.dump(usinas)  # Usando dump em vez de jsonify

@usina_bp.route('/usinas/<int:id>', methods=['GET'])
def obter_usina(id):
    usina = Usina.query.get_or_404(id)
    return usina_schema.dump(usina)  # Usando dump em vez de jsonify

@usina_bp.route('/usinas/<int:id>', methods=['PUT'])
def atualizar_usina(id):
    usina = Usina.query.get_or_404(id)
    data = request.get_json()
    errors = usina_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    usina.nome = data['nome']
    usina.localizacao = data.get('localizacao')
    db.session.commit()
    return usina_schema.dump(usina)  # Usando dump em vez de jsonify

@usina_bp.route('/usinas/<int:id>', methods=['DELETE'])
def deletar_usina(id):
    usina = Usina.query.get_or_404(id)
    db.session.delete(usina)
    db.session.commit()
    return '', 204
