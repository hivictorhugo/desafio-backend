# API de Monitoramento de Usinas Fotovoltaicas

Este projeto é um protótipo de API REST para monitoramento de usinas fotovoltaicas, desenvolvido como parte do processo seletivo da TECSCI.

## Tecnologias Utilizadas

* Python 3
* Flask
* Flask SQLAlchemy
* Flask Migrate
* SQLite (como banco de dados)

## Estrutura do Projeto

```
desafio-backend/
|├── app/
|   |├── __init__.py
|   |├── controllers/
|   |├── models/
|   |├── schemas/
|   └── ...
|└── migrations/ (após rodar os comandos do Flask-Migrate)
```

## Como Executar o Projeto

### 1. Crie o ambiente virtual e ative

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a variável de ambiente e rode o servidor

```bash
set FLASK_APP=app  # Windows
# ou
export FLASK_APP=app  # Linux/macOS

flask run
```

### 4. (Opcional) Executar migrações

```bash
flask db init       # apenas na primeira vez
flask db migrate -m "Mensagem da migração"
flask db upgrade
```

## Endpoints Obrigatórios (conforme desafio)

* CRUD de Usinas: `GET`, `POST`, `PUT`, `DELETE` em `/usinas`
* CRUD de Inversores: `GET`, `POST`, `PUT`, `DELETE` em `/inversores`
* Potência máxima por dia: `/potencia-maxima`
* Média da temperatura por dia: `/media-temperatura`
* Geração da usina: `/geracao-usina`
* Geração do inversor: `/geracao-inversor`

## Exemplos de Consumo via PowerShell

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/inversores -Method Post -ContentType "application/json" -Body (@{
    usina_id = 1
    potencia_maxima = 1000
    temperatura = 45
} | ConvertTo-Json)
```
## Testes com filtros (exemplos)

- `/geracao-usina?usina_id=1&data_inicio=2023-01-01&data_fim=2023-12-31`
- `/potencia-maxima?inversor_id=2&data_inicio=2023-05-01&data_fim=2023-05-07`


## Observações

* O projeto está em formato de protótipo, com foco em clareza de arquitetura e boas práticas.
* Estrutura modular separando controladores, modelos e inicialização da aplicação.

---

Para dúvidas ou sugestões, entre em contato com o desenvolvedor deste desafio.
