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
