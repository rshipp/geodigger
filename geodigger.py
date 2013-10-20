"""
A base class to use for API geolocation diggers.
"""

import time
import pymongo
from Crypto.Hash import SHA256
import config

class GeoDigger(object):
    def __init__(self):
        self.twitter = config.twitter
        self.mongodb = config.mongodb
        self.hasher = SHA256
        # Override the namespace in your miner class.
        self.namespace = "default"
        logfile = open("geodigger.log", "a+")

    def save(self, userID, time, coordinates):
        """Write geolocation data to the Mongo database."""
        conn = pymongo.Connection("127.0.0.1")

    def sanitizeUser(self, username):
        """Return a sanitized unique ID given a namespace and username.
           Uses SHA-256 (PyCrypto).
        """
        return self.hasher.new('%s:%s' % (self.namespace,
                    username)).hexdigest()

    def log(self, message):
        logfile.write("[%s] %s", (time.asctime(), message))
