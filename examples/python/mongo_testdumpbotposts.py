import pymongo
from bson.son import SON
from Crypto.Hash import SHA256

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']

usernames = [
    '267173357', #'ELSA32_bousai',
    '1180025371', #'trendinaliaUS',
    '1644859885', #'billmackenzie22',
    '429803867', #'marsbots',
    '61043461', #'googuns_prod',
    '1001857784', #'voru_th',
]

for username in usernames:
    userID = SHA256.new('%s:%s' % ('twitter', username)).hexdigest()
    a = coll.find({'userID': userID})

    for b in a:
        print "1,%s,%s,%s,%s" % (b['userID'], b['time'], b['loc']['coordinates'][0], b['loc']['coordinates'][1])
