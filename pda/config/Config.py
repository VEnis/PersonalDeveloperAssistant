"""
Module that contains implementation of the configuration class
"""

from UserDict import IterableUserDict


class Config(IterableUserDict):
    """
    Implementation of the configuration class
    """

    def __init__(self, dict=None, **kwargs):
        IterableUserDict.__init__(self, dict, **kwargs)

    def save(self):
        """
        Saves container data. Actual saving will be implemented in child classes
        """
        pass

    def load(self):
        """
        Loads container data. Actual loading will be implemented in child classes
        """
        pass
