"""
Data mine for geolocation data using Twitter's streaming API.
"""

import tweetpy
from apiminer import APIMiner

class TwitterMiner(APIMiner):
    def __init__(self):
        super(TwitterMiner, self).__init__()
        self.username = self.twitter['username']
        self.key = self.twitter['consumerKey']
