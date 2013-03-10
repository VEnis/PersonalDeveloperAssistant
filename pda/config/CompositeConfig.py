"""
Module that contains implementation of the composite configuration class
"""
from collections import Iterable

from pda.config.Config import Config


class CompositeConfig(Config):
    """
    Implementation of the composite configuration class
    """

    def __init__(self, dict=None, configs=None, **kwargs):
        Config.__init__(self, dict, **kwargs)

        self.configs = []
        if configs is not None:
            if not isinstance(configs, Iterable):
                raise TypeError("Passed configs value is not List")
            else:
                if not all(isinstance(c, Config) for c in configs):
                    raise TypeError("Some items in the configs list does not inherited from pda.config.Config")
                else:
                    self.configs = configs

    def get(self, key, failobj=None):
        if key not in self:
            return failobj
        return self[key]

    def __getitem__(self, key):
        data = self._get_data_from_all_configs()
        if key in data:
            return data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)

    def __len__(self):
        return len(self._get_data_from_all_configs())

    def __iter__(self):
        return self._get_data_from_all_configs().__iter__()

    def values(self):
        return self._get_data_from_all_configs().values()

    def items(self):
        return self._get_data_from_all_configs().items()

    def keys(self):
        return self._get_data_from_all_configs().keys()

    def __contains__(self, key):
        return key in self._get_data_from_all_configs()

    def __repr__(self):
        return repr(self._get_data_from_all_configs())

    def _get_data_from_all_configs(self):
        result = {}
        for config in reversed(self.configs):
            result.update(config.data)

        result.update(self.data)
        return result
