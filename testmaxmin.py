import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']

a = coll.aggregate([
        {"$group": {
            "_id": 0,
            "minDate": {"$min": "$time"}
        }},
])

for b in a['result']:
    print "Min date: ", b['minDate']

c = coll.aggregate([
        {"$group": {
            "_id": 0,
            "maxDate": {"$max": "$time"}
        }},
])

for d in c['result']:
    print "Max date: ", d['maxDate']
