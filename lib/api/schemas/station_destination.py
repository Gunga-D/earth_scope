from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class StationDestination(Schema):
    kilometers = fields.Float()
    degrees = fields.Float()
    on_map = fields.String()

class CalcStationDestinationRequestSchema(Schema):
    service_name = fields.String()
    network = fields.String()
    station = fields.String()
    source_latitude = fields.Float()
    source_longitude = fields.Float()

class CalcStationDestinationResponseSchema(SuccessResponseSchema):
    data = fields.Nested(StationDestination)