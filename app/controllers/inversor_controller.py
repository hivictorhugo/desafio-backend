from flask import Blueprint
from app.services.inversor_service import (
    criar_inversor_service,
    listar_inversores_service,
    obter_inversor_service,
    atualizar_inversor_service,
    deletar_inversor_service
)

inversor_bp = Blueprint('inversor', __name__)

@inversor_bp.route('/inversores', methods=['POST'])
def criar_inversor():
    return criar_inversor_service()

@inversor_bp.route('/inversores', methods=['GET'])
def listar_inversores():
    return listar_inversores_service()

@inversor_bp.route('/inversores/<int:id>', methods=['GET'])
def obter_inversor(id):
    return obter_inversor_service(id)

@inversor_bp.route('/inversores/<int:id>', methods=['PUT'])
def atualizar_inversor(id):
    return atualizar_inversor_service(id)

@inversor_bp.route('/inversores/<int:id>', methods=['DELETE'])
def deletar_inversor(id):
    return deletar_inversor_service(id)
