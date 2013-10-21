import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger_test']
coll = db['data_test']

#coll.create_index([('loc', pymongo.GEOSPHERE)])
coll.ensure_index([(u'loc', pymongo.GEOSPHERE)])

c = {"loc":
            SON([
                ("$near", SON([
                    ("$geometry", SON([
                        ("type", "Point"),
                        ("coordinates", [-105.2, 39.7])
                        ])
                    ),
                    ("$maxDistance", 10000)
                    ])
                )
            ])
}

a = coll.find(c)

for b in a:
    print b
