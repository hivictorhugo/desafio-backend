from marshmallow import Schema, fields

class InversorSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    usina_id = fields.Int(required=True)
