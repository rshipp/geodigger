import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']

a = coll.aggregate([
        {"$group": {
            "_id": "$userID",
            "number": {"$sum": 1}
        }},
        {"$sort": {"number": -1}},
        {"$limit": 100}
])

for b in a['result']:
    print "%s,%s" % (b['_id'], b['number'])
