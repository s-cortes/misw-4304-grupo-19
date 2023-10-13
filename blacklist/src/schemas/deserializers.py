from marshmallow import Schema, fields, validate


class CreateEmailSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={"invalid": "invalid email"}
    )
    app_uuid = fields.String(
        required=True,
        validate=validate.Regexp(r"[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}"),
        error_messages={"invalid": "invalid app_uuid"}
    )
    blocked_reason = fields.String(
        required=True,
        validate=validate.Length(min=5),
        error_messages={"invalid": "invalid blocked_reason"}
    )


create_schema = CreateEmailSchema()
