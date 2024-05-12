from lib.cache.mapper.base import BaseMapper

class StreamMapper(BaseMapper):
    def create_streams(self, service, streams):
        self.create(service, streams, expiration=100)
    
    def get_streams(self, service):
        return self.get(service)