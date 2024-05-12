class FDSNClientException(Exception):
    pass

class FDSNClientNoDataException(FDSNClientException):
    pass

class FDSNClientInvalidParamsException(FDSNClientException):
    pass