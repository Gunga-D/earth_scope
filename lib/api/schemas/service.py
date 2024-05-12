from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class ServiceSchema(Schema):
    name = fields.String()
    has_supported_scrap = fields.Bool()

class GetServicesResponseSchema(SuccessResponseSchema):
    data = fields.List(fields.Nested(ServiceSchema))