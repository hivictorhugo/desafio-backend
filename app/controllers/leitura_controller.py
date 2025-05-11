import json
from flask import Blueprint, jsonify
from datetime import datetime
from app.models.leitura import Leitura
from app import db

leitura_bp = Blueprint('leitura', __name__)

# Rota para carregar os dados de metrics.json
@leitura_bp.route('/inserir-metrics', methods=['POST'])
def inserir_metrics():
    try:
        # Carregar o conteúdo do arquivo JSON
        with open('metrics.json', 'r') as file:
            data = json.load(file)
        
        # Processar cada item e adicionar ao banco de dados
        for item in data:
            # Convertendo o campo 'datetime' para o formato de data
            datetime_str = item['datetime']['$date']
            data_datetime = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            
            # Criar o objeto Leitura e adicionar no banco
            leitura = Leitura(
                inversor_id=item['inversor_id'],
                data=data_datetime,
                potencia_ativa_watt=item['potencia_ativa_watt'],
                temperatura_celsius=item['temperatura_celsius']
            )
            db.session.add(leitura)
        
        # Commitar as alterações no banco de dados
        db.session.commit()
        return jsonify({"message": "Dados inseridos com sucesso!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
