from flask import Blueprint
from app.services.usina_service import (
    criar_usina_service,
    listar_usinas_service,
    obter_usina_service,
    atualizar_usina_service,
    deletar_usina_service
)

usina_bp = Blueprint('usina', __name__)

@usina_bp.route('/usinas', methods=['POST'])
def criar_usina():
    return criar_usina_service()

@usina_bp.route('/usinas', methods=['GET'])
def listar_usinas():
    return listar_usinas_service()

@usina_bp.route('/usinas/<int:id>', methods=['GET'])
def obter_usina(id):
    return obter_usina_service(id)

@usina_bp.route('/usinas/<int:id>', methods=['PUT'])
def atualizar_usina(id):
    return atualizar_usina_service(id)

@usina_bp.route('/usinas/<int:id>', methods=['DELETE'])
def deletar_usina(id):
    return deletar_usina_service(id)