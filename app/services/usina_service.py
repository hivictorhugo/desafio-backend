from flask import request, jsonify
from app import db
from app.models.usina import Usina
from app.schemas.usina_schema import UsinaSchema

usina_schema = UsinaSchema()
usinas_schema = UsinaSchema(many=True)


def criar_usina_service():
    data = request.get_json()
    errors = usina_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    nova = Usina(**data)
    db.session.add(nova)
    db.session.commit()
    return usina_schema.dump(nova), 201


def listar_usinas_service():
    usinas = Usina.query.all()
    return jsonify(usinas_schema.dump(usinas)), 200


def obter_usina_service(usina_id):
    usina = Usina.query.get_or_404(usina_id)
    return usina_schema.dump(usina), 200


def atualizar_usina_service(usina_id):
    usina = Usina.query.get_or_404(usina_id)
    data = request.get_json()
    errors = usina_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    usina.nome = data.get('nome', usina.nome)
    usina.localizacao = data.get('localizacao', usina.localizacao)
    db.session.commit()
    return usina_schema.dump(usina), 200


def deletar_usina_service(usina_id):
    usina = Usina.query.get_or_404(usina_id)
    db.session.delete(usina)
    db.session.commit()
    return '', 204
