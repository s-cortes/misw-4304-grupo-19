from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.dialects.postgresql import UUID

from utils.database import db

ma: Marshmallow = Marshmallow()


class Email(db.Model):
    email = db.Column(db.String(), nullable=False, unique=True)
    app_uuid = db.Column(UUID(as_uuid=True), primary_key=True)
    blocked_reason = db.Column(db.String(), nullable=False)


class EmailSerializerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        load_instance = True

    email = fields.Email()
    app_uuid = fields.String()
    blocked_reason = fields.String()


email_schema = EmailSerializerSchema()
