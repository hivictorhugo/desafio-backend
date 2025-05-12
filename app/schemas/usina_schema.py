from marshmallow import Schema, fields
from app.schemas.inversor_schema import InversorSchema

class UsinaSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    localizacao = fields.Str()

    inversores = fields.Nested(InversorSchema, many=True, dump_only=True)

    

  
