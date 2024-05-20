from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class ConnectionSchema(Schema):
    host = fields.String()
    port = fields.String()

class ServiceSchema(Schema):
    name = fields.String()
    connection = fields.Nested(ConnectionSchema)
    has_supported_scrap = fields.Bool()
    has_supported_dist = fields.Bool()

class GetServicesResponseSchema(SuccessResponseSchema):
    data = fields.List(fields.Nested(ServiceSchema))