"""
Module that contains implementation of the user-related configuration class
"""

from config.PersistentConfig import PersistentConfig
import os


class UserConfig(PersistentConfig):
    """
    Implementation of the user-related configuration class
    """

    def __init__(self, dict=None, **kwargs):
        PersistentConfig.__init__(self, dict, **kwargs)


    def getPersistentPath(self):
        """
        Returns path where data was stored.

        Looks like: "C:/Users/[username]/pda.user.cfg"
        """
        return os.path.join(os.getenv('USERPROFILE'), "pda.user.cfg")

    def __del__(self):
        PersistentConfig.__del__(self)








