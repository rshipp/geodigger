import pymongo
from bson.son import SON

conn = pymongo.Connection('127.0.0.1')
db = conn['geodigger']
coll = db['data']

coll.ensure_index([(u'loc', pymongo.GEOSPHERE)])

# Select records within 10000m of point [-105.2, 39.7]
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
