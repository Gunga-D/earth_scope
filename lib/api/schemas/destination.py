from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class Destination(Schema):
    kilometers = fields.Float()
    degrees = fields.Float()
    on_map = fields.String()

class CalcDestinationRequestSchema(Schema):
    service_name = fields.String()
    network = fields.String()
    station = fields.String()
    source_latitude = fields.Float()
    source_longitude = fields.Float()

class CalcDestinationResponseSchema(SuccessResponseSchema):
    data = fields.Nested(Destination)