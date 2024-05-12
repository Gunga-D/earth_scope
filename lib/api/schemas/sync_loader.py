from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class ScrapedSyncLoader(Schema):
    file = fields.String()
    waveform_data = fields.String()
    waveform_format = fields.String()

class ScrapSyncLoaderRequestSchema(Schema):
    service_name = fields.String()
    network = fields.String()
    station = fields.String()
    left_time = fields.String()
    right_time = fields.String()

class ScrapSyncLoaderResponseSchema(SuccessResponseSchema):
    data = fields.Nested(ScrapedSyncLoader)