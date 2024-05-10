class CoreBaseExceptionError(Exception):
    message="Internal Server Error"

class CoreDataError(CoreBaseExceptionError):
    message = 'DATA_ERROR'

class CoreAlreadyExistsError(CoreBaseExceptionError):
    message = 'ALREADY_EXISTS'

class CoreNotFoundError(CoreBaseExceptionError):
    message = 'NOT_FOUND'