from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=False, allow_none=True)
    completed = fields.Boolean(required=False)
