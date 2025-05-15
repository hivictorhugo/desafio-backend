import json
from flask import request, jsonify
from datetime import datetime
from sqlalchemy import func, cast, Date
from app import db
from app.models.leitura import Leitura
from app.models.inversor import Inversor
from app.utils import calc_inverters_generation, TimeSeriesValue

def processar_metrics():
    try:
        with open('metrics.json', 'r') as file:
            data = json.load(file)

        for item in data:
            if not all(k in item and item[k] is not None for k in ('inversor_id', 'potencia_ativa_watt', 'temperatura_celsius')):
                continue

            datetime_str = item['datetime']['$date']
            data_datetime = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            leitura = Leitura(
                inversor_id=item['inversor_id'],
                data=data_datetime,
                potencia_ativa_watt=item['potencia_ativa_watt'],
                temperatura_celsius=item['temperatura_celsius']
            )
            db.session.add(leitura)

        db.session.commit()
        return jsonify({"message": "Dados inseridos com sucesso!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def listar_leituras_service():
    try:
        inversor_id = request.args.get('inversor_id', type=int)
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')

        query = Leitura.query

        if inversor_id:
            query = query.filter_by(inversor_id=inversor_id)

        if data_inicio:
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
            query = query.filter(Leitura.data >= data_inicio)

        if data_fim:
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d")
            query = query.filter(Leitura.data <= data_fim)

        leituras = query.all()
        resultado = [
            {
                'id': l.id,
                'inversor_id': l.inversor_id,
                'data': l.data.isoformat(),
                'potencia_ativa_watt': l.potencia_ativa_watt,
                'temperatura_celsius': l.temperatura_celsius
            } for l in leituras
        ]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def potencia_maxima_service():
    try:
        inversor_id = request.args.get('inversor_id', type=int)
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')

        if not inversor_id:
            return jsonify({"error": "inversor_id é obrigatório"}), 400

        query = db.session.query(
            cast(Leitura.data, Date).label('data'),
            func.max(Leitura.potencia_ativa_watt).label('potencia_maxima')
        ).filter(Leitura.inversor_id == inversor_id)

        if data_inicio:
            query = query.filter(Leitura.data >= datetime.strptime(data_inicio, "%Y-%m-%d"))
        if data_fim:
            query = query.filter(Leitura.data <= datetime.strptime(data_fim, "%Y-%m-%d"))

        query = query.group_by(cast(Leitura.data, Date)).order_by('data')

        resultados = [
            {
                "data": str(row.data),
                "potencia_maxima": row.potencia_maxima
            } for row in query.all()
        ]

        return jsonify(resultados), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def temperatura_media_service():
    try:
        inversor_id = request.args.get('inversor_id', type=int)
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')

        if not inversor_id:
            return jsonify({"error": "inversor_id é obrigatório"}), 400

        query = db.session.query(
            cast(Leitura.data, Date).label('data'),
            func.avg(Leitura.temperatura_celsius).label('temperatura_media')
        ).filter(Leitura.inversor_id == inversor_id)

        if data_inicio:
            query = query.filter(Leitura.data >= datetime.strptime(data_inicio, "%Y-%m-%d"))
        if data_fim:
            query = query.filter(Leitura.data <= datetime.strptime(data_fim, "%Y-%m-%d"))

        query = query.group_by(cast(Leitura.data, Date)).order_by('data')

        resultados = [
            {
                "data": str(row.data),
                "temperatura_media": round(row.temperatura_media, 2)
            } for row in query.all()
        ]

        return jsonify(resultados), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def geracao_usina_service():
    try:
        usina_id = request.args.get('usina_id', type=int)
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')

        if not usina_id:
            return jsonify({"error": "usina_id é obrigatório"}), 400

        inversores = Inversor.query.filter_by(usina_id=usina_id).all()
        entidades = []

        for inversor in inversores:
            query = Leitura.query.filter_by(inversor_id=inversor.id)
            if data_inicio:
                query = query.filter(Leitura.data >= datetime.strptime(data_inicio, "%Y-%m-%d"))
            if data_fim:
                query = query.filter(Leitura.data <= datetime.strptime(data_fim, "%Y-%m-%d"))

            leituras = query.order_by(Leitura.data).all()
            entidade = type('Entidade', (), {})()
            entidade.power = [TimeSeriesValue(value=l.potencia_ativa_watt, date=l.data) for l in leituras]
            entidades.append(entidade)

        total = calc_inverters_generation(entidades)
        return jsonify({"usina_id": usina_id, "geracao_total_kwh": round(total, 2)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def geracao_inversor_service():
    try:
        inversor_id = request.args.get('inversor_id', type=int)
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')

        if not inversor_id:
            return jsonify({"error": "inversor_id é obrigatório"}), 400

        query = Leitura.query.filter_by(inversor_id=inversor_id)
        if data_inicio:
            query = query.filter(Leitura.data >= datetime.strptime(data_inicio, "%Y-%m-%d"))
        if data_fim:
            query = query.filter(Leitura.data <= datetime.strptime(data_fim, "%Y-%m-%d"))

        leituras = query.order_by(Leitura.data).all()
        entidade = type('Entidade', (), {})()
        entidade.power = [TimeSeriesValue(value=l.potencia_ativa_watt, date=l.data) for l in leituras]

        total = calc_inverters_generation([entidade])
        return jsonify({"inversor_id": inversor_id, "geracao_total_kwh": round(total, 2)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
