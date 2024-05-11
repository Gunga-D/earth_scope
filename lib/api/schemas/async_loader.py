from marshmallow import Schema, fields

from lib.api.schemas.base import SuccessResponseSchema

class AsyncLaunchedLoader(Schema):
    task_id = fields.String()
    status = fields.String()
    files = fields.List(fields.String())

class LaunchAsyncLoaderRequestSchema(Schema):
    service_name = fields.String()
    network = fields.String()
    station = fields.String()
    interval_sec = fields.Integer()

class LaunchAsyncLoaderResponseSchema(SuccessResponseSchema):
    data = fields.Nested(AsyncLaunchedLoader)