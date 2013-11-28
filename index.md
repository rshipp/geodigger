GeoDigger
=========

# Introduction

The goal of this project is to develop a tool that collects publicly
available location information from social network services, such as
Twitter and Foursquare. These social network services allow users to tag
posts with their current location. By listening to the public streams of
data that these services provide, it is possible to build a database of
location information, an invaluable data source for human mobility
research.

In order to develop a tool that would let researchers easily create
datasets of location information, several existing technologies had to be
researched and put to use.

# Technologies

* [MongoDB](mongodb.md):
    A non-relational, document-oriented database designed to allow for
    efficient storage and searching of large datasets.
* Python:
    The tool itself is written in Python, an object-oriented interpreted
    language with a large number of community-developed extensions.
* [Twitter APIs]:
    Application programming interfaces that allow applications to
    control Twitter services and access Twitter data.
* [Tweepy](tweepy.md):
    A Python module that allows us to use the Twitter API.
* [PyMongo](pymongo.md):
    A Python module that allows us to use a Mongo database server.
* [GeoJSON](geojson.md):
    A format used to encode geographical information.
* [Pyramid](pyramid.md):
    A Python web framework used to create a web-based frontend for the
    GeoDigger project.

# Usage

## Gathering data

Users interested in collecting their own data with GeoDigger would first
have to register for whatever social network services they want to use
and collect the necessary authentication information.

...

## Viewing data

The GeoDigger web frontend

...

# Extending

GeoDigger was designed with extensibility in mind. A single parent class
takes care of interfacing with the database server and sanitizing unique
user IDs. Specialized child classes such as TwitterDigger take care of
reading from a single API, using the `save()` method from the GeoDigger
parent class to store information to a local database, and the `log()`
method to provide timestamps for connection attempts, errors, and other
information that might be of use.

Adding support for additional social network service APIs is
straightforward - just take a look at TwitterDigger.py for example
code.

*** It would be great to add a class diagram here so we can actually see
the classes interface ***
