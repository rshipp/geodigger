PyMongo
=======

# About PyMongo

PyMongo is a well documented Python module, or library, that allows
developers to interact with [Mongo](mongodb.md) databases
[[1]](http://api.mongodb.org/python/current/).

# PyMongo applications in GeoDigger

PyMongo is used in the GeoDigger base class to allow child classes to
easily store correctly formatted data to a database. It is also used
more extensively in the GeoDigger web interface.

...


## BSON
MongoDB stores data in a format known as BSON
[[2]](http://bsonspec.org/), or Binary JSON [[3]](http://json.org/). This
structured binary encoding format can very efficiently store data, but
it is not directly compatible with Python. For this reason, the
developers of PyMongo ship a seperate *bson* Python library with their
PyMongo distribution. This allows users of PyMongo to access the full
functionality of MongoDB.
