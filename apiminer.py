"""
A base class to use for API miners.
"""

import pymongo
from Crypto.Hash import SHA256
import config

class APIMiner(object):
    def __init__(self):
        self.twitter = config.twitter
        self.mongodb = config.mongodb
        self.hasher = SHA256.new()
        # Override the namespace in your miner class.
        self.namespace = "default"

    def save(self, userID, time, coordinates):
        """Write geolocation data to the Mongo database."""
        conn = pymongo.Connection("127.0.0.1")

    def sanitizeUser(self, username):
        """Return a sanitized unique ID given a namespace and username.
           Uses SHA-256 (PyCrypto).
        """
        self.hasher.update('%s:%s' % (self.namespace, username))
        return self.hasher.hexdigest()
