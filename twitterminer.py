"""
Data mine for geolocation data using Twitter's streaming API.
"""

import tweepy
from apiminer import APIMiner

count = 0

class TwitterMiner(APIMiner):
    def __init__(self):
        super(TwitterMiner, self).__init__()
        self.username = self.twitter['username']
        self.key = self.twitter['consumerKey']
        self.secret = self.twitter['consumerSecret']
        self.atKey = self.twitter['accessToken']
        self.atSecret = self.twitter['accessTokenSecret']
        self.namespace = "twitter"

    def mine_forever(self):
        """Connect to the Twitter streaming API and collect statuses."""
        auth = tweepy.OAuthHandler(self.key, self.secret)
        auth.set_access_token(self.atKey, self.atSecret)
        streamer = tweepy.Stream(auth=auth, listener=TwitterStreamer(),
                timeout=5)
        streamer.filter(locations=[-180,-90,180,90]) # Any geotagged post



class TwitterStreamer(tweepy.StreamListener):
    def __init__(self):
        super(TwitterStreamer, self).__init__()
        self.count = 0

    def on_status(self, status):
        if status.coordinates != None:
            self.count += 1
            print "New tweet:", status.user.id, status.coordinates, status.created_at
        if self.count >= 1000:
            print "Done."
            raise Exception("1000 tweets reached.")

    def on_error(self, code):
        print "Error: " + str(code)
