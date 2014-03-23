import pymongo
from bson.son import SON
from Crypto.Hash import SHA256
import tweepy

key = ''
secret = ''
atKey = ''
atSecret = ''

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(atKey, atSecret)

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']

usernames = [
    'usernamehere',
    'usernamehere',
]

api = tweepy.API(auth)

for username in usernames:
    try:
        username = api.get_user(username).id
        userID = SHA256.new('%s:%s' % ('twitter', username)).hexdigest()
        a = coll.find({'userID': userID})
        for b in a:
            print "0,%s,%s,%s,%s" % (b['userID'], b['time'], b['loc']['coordinates'][0], b['loc']['coordinates'][1])
    except:
        pass