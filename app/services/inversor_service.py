from flask import request, jsonify
from app import db
from app.models.inversor import Inversor
from app.schemas.inversor_schema import InversorSchema

inversor_schema = InversorSchema()
inversores_schema = InversorSchema(many=True)


def criar_inversor_service():
    data = request.get_json()
    errors = inversor_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    novo = Inversor(**data)
    db.session.add(novo)
    db.session.commit()
    return inversor_schema.dump(novo), 201


def listar_inversores_service():
    inversores = Inversor.query.all()
    return jsonify(inversores_schema.dump(inversores)), 200


def obter_inversor_service(inv_id):
    inversor = Inversor.query.get_or_404(inv_id)
    return inversor_schema.dump(inversor), 200


def atualizar_inversor_service(inv_id):
    inversor = Inversor.query.get_or_404(inv_id)
    data = request.get_json()
    errors = inversor_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    inversor.nome = data.get('nome', inversor.nome)
    inversor.usina_id = data.get('usina_id', inversor.usina_id)
    db.session.commit()
    return inversor_schema.dump(inversor), 200


def deletar_inversor_service(inv_id):
    inversor = Inversor.query.get_or_404(inv_id)
    db.session.delete(inversor)
    db.session.commit()
    return '', 204
