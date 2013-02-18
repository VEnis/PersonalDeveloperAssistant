"""
Module that contains implementation of the user-related configuration class
"""
import pickle
from pda.config.Config import Config
import os

class UserConfig(Config):
    """
    Implementation of the user-related configuration class
    """

    pickle_protocol_version = 2

    def __init__(self, dict=None, **kwargs):
        Config.__init__(self, dict, **kwargs)
        self.load()

    def save(self):
        """
        Saves container data.

        Container data is saved to the path returned by getPersistentPath function
        """
        with open(self.getPersistentPath(), "wb") as persistent_file:
            pickle.dump(self.data, persistent_file, UserConfig.pickle_protocol_version)

    def load(self):
        """
        Loads container data.

        Container data is loaded from path returned by getPersistentPath function
        """
        with open(self.getPersistentPath(), "rb") as persistent_file:
            self.data = pickle.load(persistent_file)

    def getPersistentPath(self):
        """
        Returns path where data was stored.

        Looks like: "C:/Users/[username]/pda.user.cfg"
        """
        return os.path.join(os.getenv('USERPROFILE'), "pda.user.cfg")

    def __del__(self):
        self.save()
