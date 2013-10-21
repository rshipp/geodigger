import pymongo

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger_test']
coll = db['data_test']

coll.create_index([('loc', pymongo.GEOSPHERE)])

print coll.find({

        })
