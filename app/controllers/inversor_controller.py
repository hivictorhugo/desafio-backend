from flask import Blueprint, request, jsonify
from app import db
from app.models.inversor import Inversor
from app.schemas.inversor_schema import InversorSchema

inversor_bp = Blueprint('inversor', __name__)
inversor_schema = InversorSchema()
inversores_schema = InversorSchema(many=True)

@inversor_bp.route('/inversores', methods=['POST'])
def criar_inversor():
    data = request.get_json()
    errors = inversor_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    novo_inversor = Inversor(**data)
    db.session.add(novo_inversor)
    db.session.commit()
    return inversor_schema.dump(novo_inversor), 201

@inversor_bp.route('/inversores', methods=['GET'])
def listar_inversores():
    inversores = Inversor.query.all()
    return jsonify(inversores_schema.dump(inversores))

@inversor_bp.route('/inversores/<int:id>', methods=['GET'])
def obter_inversor(id):
    inversor = Inversor.query.get_or_404(id)
    return inversor_schema.dump(inversor)

@inversor_bp.route('/inversores/<int:id>', methods=['PUT'])
def atualizar_inversor(id):
    inversor = Inversor.query.get_or_404(id)
    data = request.get_json()
    errors = inversor_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    inversor.nome = data['nome']
    inversor.usina_id = data['usina_id']
    db.session.commit()
    return inversor_schema.dump(inversor)

@inversor_bp.route('/inversores/<int:id>', methods=['DELETE'])
def deletar_inversor(id):
    inversor = Inversor.query.get_or_404(id)
    db.session.delete(inversor)
    db.session.commit()
    return '', 204
