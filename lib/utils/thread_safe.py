from typing import Callable, Dict
import threading

class Safe:
    def __init__(self):
        self.lock = threading.Lock()

    def on(self, f: Callable, **kwargs: Dict[str, any]):
        while self.lock.locked():
            continue
        self.lock.acquire()
        f(kwargs=kwargs)
        self.lock.release()