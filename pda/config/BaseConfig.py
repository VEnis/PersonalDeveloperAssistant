from UserDict import IterableUserDict


class BaseConfig(IterableUserDict):
    def __init__(self, dict=None, **kwargs):
        IterableUserDict.__init__(self, dict, **kwargs)

    def set(self, key, value):
        self[key] = value

    def delete(self, key):
        del self.data[key]

    def save(self):
        pass

    def load(self):
        pass
