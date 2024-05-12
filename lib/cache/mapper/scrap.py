from lib.cache.mapper.base import BaseMapper

class ScrapMapper(BaseMapper):
    def save_scrap(self, service, network, station, left_time, right_time, scrapped_data):
        self.create(service+'-'+network+'-'+station+'-' + left_time + '|' + right_time,
                    scrapped_data, expiration=1200000)
    
    def get_scrap(self, service, network, station, left_time, right_time):
        return self.get(service+'-'+network+'-'+station+'-' + left_time + '|' + right_time)