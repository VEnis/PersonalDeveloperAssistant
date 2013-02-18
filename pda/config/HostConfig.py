"""
Module that contains implementation of the host-related configuration class
"""
import sys

from pda.config.PersistentConfig import PersistentConfig
import os


class HostConfig(PersistentConfig):
    """
    Implementation of the host-related configuration class
    """

    def __init__(self, dict=None, **kwargs):
        PersistentConfig.__init__(self, dict, **kwargs)

    @staticmethod
    def getPersistentPath():
        """
        Returns path where data was stored.

        Looks like: "C:/Users/[username]/pda.user.cfg"
        """
        if sys.platform == "win32":
            return os.path.join(os.getenv('ALLUSERSPROFILE'), "pda.host.cfg")
        else:
            raise NotImplementedError("HostConfig for non-windows is not implemented yet")

    def __del__(self):
        PersistentConfig.__del__(self)
