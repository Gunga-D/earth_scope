from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class LoadedResult(Schema):
    file = fields.String()
    waveform_data = fields.String()
    waveform_format = fields.String()

class AsyncLaunchedLoader(Schema):
    task_id = fields.String()
    status = fields.String()
    result = fields.Nested(LoadedResult)

class LaunchAsyncLoaderRequestSchema(Schema):
    service_name = fields.String()
    network = fields.String()
    station = fields.String()
    interval_sec = fields.Integer()

class LaunchAsyncLoaderResponseSchema(SuccessResponseSchema):
    data = fields.Nested(AsyncLaunchedLoader)