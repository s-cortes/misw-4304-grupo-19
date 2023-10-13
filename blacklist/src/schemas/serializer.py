from marshmallow import Schema, fields, validate


class GetEmailResponseSchema(Schema):
    exists = fields.Boolean(required=True)
    reason = fields.String(required=False)
