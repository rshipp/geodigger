MongoDB
=======

MongoDB is a popular non-relational document-oriented database designed
to store large amounts of information. [[1]](http://www.mongodb.org/)
MongoDB's support for storing and querying from vast datasets, along
with its built-in support for [GeoJSON](geojson.md) make it a perfect
match for this project. When using a MongoDB server, it is important to
make sure that the machine on which the server runs has a 64-bit
processor. If this is not the case, the MongoDB server will only be able
to store up to two gigabytes of data, which will severely limit its
usefulness. In experiments run during the development of GeoDigger's
Twitter functionality, it took approximately two days of saving data
from the Twitter streaming API to reach this two gigabyte storage limit.

## Tables, Collections, and Indices


## Geospatial Support


## PyMongo

PyMongo is a well documented Python module, or library, that allows
developers to interact with [Mongo](mongodb.md) databases
[[1]](http://api.mongodb.org/python/current/).

### Applications in GeoDigger

PyMongo is used in the GeoDigger base class to allow child classes to
easily store correctly formatted data to a database. It is also used
more extensively in the GeoDigger web interface.

...


### BSON
MongoDB stores data in a format known as BSON
[[2]](http://bsonspec.org/), or Binary JSON [[3]](http://json.org/). This
structured binary encoding format can very efficiently store data, but
it is not directly compatible with Python. For this reason, the
developers of PyMongo ship a seperate *bson* Python library with their
PyMongo distribution. This allows users of PyMongo to access the full
functionality of MongoDB.

## Queries and Aggregation
