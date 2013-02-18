"""
Module that contains implementation of the host-related configuration class
"""

from pda.config.PersistentConfig import PersistentConfig
import os


class HostConfig(PersistentConfig):
    """
    Implementation of the host-related configuration class
    """

    def __init__(self, dict=None, **kwargs):
        PersistentConfig.__init__(self, dict, **kwargs)

    def getPersistentPath(self):
        """
        Returns path where data was stored.

        Looks like: "C:/Users/[username]/pda.user.cfg"
        """
        return os.path.join(os.getenv('ALLUSERSPROFILE'), "pda.host.cfg")

    def __del__(self):
        PersistentConfig.__del__(self)
