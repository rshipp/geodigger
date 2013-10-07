"""
A base class to use for API miners.
"""

import pymongo
import config

class APIMiner(object):
    def __init__(self):
        self.twitter = config.twitter
        self.mongodb = config.mongodb

    def store(userID, time, coordinates):
        """Write geolocation data to the Mongo database."""
        conn = pymongo.Connection("127.0.0.1")

