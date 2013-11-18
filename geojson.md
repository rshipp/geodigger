GeoJSON
=======

GeoJSON is "a format for encoding a variety of geographic data
stuctures." [[1]](http://geojson.org/) This format, which is fully
supported by [MongoDB](mondodb.md), allows us to run extremely flexible
queries on the data that the GeoDigger tool collects. Data is saved into
our database as a number of GeoJSON "points", each consisting of a
latitude and longitude:

    {
        type: "Point",
        coordinates: [0.5, 0.5]
    }

If we then instruct MongoDB to treat this as a point on a
two-dimensional sphere, it allows us to run queries on our data with
this in mind. We can define a polygon of an arbitrary size and shape by
specifying its vertices, then pass this polygon to MongoDB and ask it to
return all data points that fall within this polygon. Alternatively, we
can query for all data points that lie within a certain radius of a
givern GeoJSON point.
[[2]](http://docs.mongodb.org/manual/applications/geospatial-indexes/)

The GeoJSON support provided by MongoDB makes deriving useful
geographical information from our dataset much easier.
