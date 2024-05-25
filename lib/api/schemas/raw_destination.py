from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class RawDestination(Schema):
    kilometers = fields.Float()
    degrees = fields.Float()
    on_map = fields.String()

class CalcRawDestinationRequestSchema(Schema):
    input_latitude = fields.Float()
    input_longitude = fields.Float()
    source_latitude = fields.Float()
    source_longitude = fields.Float()

class CalcRawDestinationResponseSchema(SuccessResponseSchema):
    data = fields.Nested(RawDestination)