from marshmallow import Schema, fields

class SuccessResponseSchema(Schema):
    status = fields.Constant('success')
    data = fields.Dict(default=None)

class FailedResponseSchema(Schema):
    status = fields.Constant('failed')
    message = fields.String()