import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']


# dump all data
for b in coll.find():
    print "%s,%s,%s,%s" % (b['userID'], b['time'],
            b['loc']['coordinates'][0], b['loc']['coordinates'][1])
