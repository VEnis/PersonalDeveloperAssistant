"""
Module that contains implementation of the configuration class
"""
from collections import UserDict

class Config(UserDict):
    """
    Implementation of the configuration class
    """

    def __init__(self, dict=None, **kwargs):
        UserDict.__init__(self, dict, **kwargs)
