from marshmallow import Schema, fields

class UsinaSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    localizacao = fields.Str()
