from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class WaveTravelTime(Schema):
    wave = fields.String()
    time_sec = fields.Float()

class CalcWaveTravelTimeRequestSchema(Schema):
    depth_km = fields.Float()
    distance_degree = fields.Float()

class CalcWaveTravelTimeResponseSchema(SuccessResponseSchema):
    data = fields.List(fields.Nested(WaveTravelTime))