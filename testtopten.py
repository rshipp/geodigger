import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger_test']
coll = db['data_test']

#coll.ensure_index([(u'userID', pymongo.GEOSPHERE)])

a = coll.aggregate([
        {"$group": {
            "_id": "$userID",
            "number": {"$sum": 1}
        }},
        {"$sort": {"number": -1}},
        {"$limit": 67487} # users/10
])

for b in a['result']:
    print "%s,%s" % (b['_id'], b['number'])

#c = {"loc":
#            SON([
#                ("$near", SON([
#                    ("$geometry", SON([
#                        ("type", "Point"),
#                        ("coordinates", [-105.2, 39.7])
#                        ])
#                    ),
#                    ("$maxDistance", 10000)
#                    ])
#                )
#            ])
#}

#a = coll.find(c)

#for b in a:
#    print b
