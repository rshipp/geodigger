import tweepy
from Crypto.Hash import SHA256

key = ''
secret = ''
atKey = ''
atSecret = ''

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(atKey, atSecret)

api = tweepy.API(auth)
#for user in api.search_users('a'):
for tweet in api.search(q="", geocode="43.30164646,-95.78780531,1mi", since=1, count=100000):
    print str(tweet.created_at) + ",",
    print "@" + tweet.user.screen_name + ":", tweet.text
