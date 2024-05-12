import json
from typing import Optional

class BaseMapper(object):
    def redis(self, redis):
        self._redis = redis
        return self

    def create(self, key, value, expiration = Optional[int]):
        value_json = json.dumps(value)
        if not self._redis is None:
            self._redis.set(key, value_json, ex=expiration)
    
    def get(self, key):
        if not self._redis is None:
            res = self._redis.get(key)
        if res is None:
            return None
        raw = res.decode('utf-8')
        return json.loads(raw)