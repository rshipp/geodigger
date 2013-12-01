GeoDigger
=========

## Introduction

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

## Technologies

* [MongoDB](mongodb.md):
    A non-relational, document-oriented database designed to allow for
    efficient storage and searching of large datasets.
* Python:
    The tool itself is written in Python, an object-oriented interpreted
    language with a large number of community-developed extensions.
* [Twitter APIs](twitter.md):
    Application programming interfaces that allow applications to
    control Twitter services and access Twitter data.
* [Tweepy](tweepy.md):
    A Python module that allows us to use the Twitter API.
* [PyMongo](mongodb.md#About_PyMongo):
    A Python module that allows us to use a Mongo database server.
* [GeoJSON](geojson.md):
    A format used to encode geographical information.
* [Pyramid](pyramid.md):
    A Python web framework used to create a web-based frontend for the
    GeoDigger project.

## GeoDigger

The GeoDigger Python script represents the end product of this research
project. It allows researchers to easily aggregate geotagged data points
from social network users, and is extensible to allow collection from
more social networks than those which have already been implemented.

[More](geodigger.md)

## Postprocessing

A non-negligable amount of posts collected from these social networking
data sources is created by "bots," software designed to post status
updates, often for commecrial purposes. In order to filter out these
posts and obtain more accurate human mobility data, a postprocessing
tool was designed to delete suspicious posts from the database.

[More]()

## GeoDigger UI

The GeoDigger web frontend allows researchers to filter data based on
time, location, and other parameters, and convert raw data points in
a database to normalized CSV output.

[More](ui.md)

