"""
Module that contains implementation of the configuration class that is automatically stored persistently
"""
import os
import pickle
from pda.config.Config import Config


class PersistentConfig(Config):
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
            pickle.dump(self.data, persistent_file, PersistentConfig.pickle_protocol_version)

    def load(self):
        """
        Loads container data.

        Container data is loaded from path returned by getPersistentPath function
        """
        if os.path.exists(self.getPersistentPath()):
            with open(self.getPersistentPath(), "rb") as persistent_file:
                self.data = pickle.load(persistent_file)

    @staticmethod
    def getPersistentPath():
        """
        Returns path where data was stored.

        Must be implemented in child classes
        """
        raise NotImplementedError

    def __del__(self):
        self.save()
