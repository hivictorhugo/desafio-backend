from flask import Blueprint
from app.services.leitura_service import (
    processar_metrics,
    listar_leituras_service,
    potencia_maxima_service,
    temperatura_media_service,
    geracao_usina_service,
    geracao_inversor_service
)

leitura_bp = Blueprint('leitura', __name__)

@leitura_bp.route('/inserir-metrics', methods=['POST'])
def inserir_metrics():
    return processar_metrics()

@leitura_bp.route('/leituras', methods=['GET'])
def listar_leituras():
    return listar_leituras_service()

@leitura_bp.route('/potencia-maxima', methods=['GET'])
def potencia_maxima_por_dia():
    return potencia_maxima_service()

@leitura_bp.route('/temperatura-media', methods=['GET'])
def temperatura_media_por_dia():
    return temperatura_media_service()

@leitura_bp.route('/geracao-usina', methods=['GET'])
def geracao_usina():
    return geracao_usina_service()

@leitura_bp.route('/geracao-inversor', methods=['GET'])
def geracao_inversor():
    return geracao_inversor_service()
