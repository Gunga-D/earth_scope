from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class StreamSchema(Schema):
    network = fields.String()
    station = fields.String()
    channels = fields.List(fields.String())

class GetStreamsRequestSchema(Schema):
    service_name = fields.String()

class GetStreamsResponseSchema(SuccessResponseSchema):
    data = fields.List(fields.Nested(StreamSchema))