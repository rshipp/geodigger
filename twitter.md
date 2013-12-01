# Twitter APIs
Twitter is a popular microblogging platform, with over 230 million
active users [[1]](https://about.twitter.com/company). It provides a
number of APIs, or application programming interfaces, that allow
developers to use various Twitter services. These APIs come in two
flavors: one a traditional REST API, and the other a "streaming" API
that allows live data consumption [[2]](https://dev.twitter.com/docs/api)
[[3]](https://dev.twitter.com/docs/streaming-apis).

## Traditional vs streaming APIs
In order to use a traditional REST API, an application must send HTTP
requests to a server and listen for responses. This is ideal for
applications that wish to post Twitter status updates, change settings,
or retrieve data at regular intervals. For developers that need access
to live data, Twitter provides a set of streaming APIs, which are more
suited for data mining applications than their REST counterparts.
To use one of the streaming APIs, an application simply authenticates
to the desired stream, sets up an HTTP connection, and waits. Twitter's
servers then push data to the application in real time, throttling the
number of status updates sent based on available bandwidth or the
streaming cap whenever necessary
[[4]](https://dev.twitter.com/docs/faq#6861).

## Public streams and the filter endpoint
Twitter offers three streaming APIs for use by developers
[[3]](https://dev.twitter.com/docs/streaming-apis). The first,
which is the most useful for data mining applications, is the public
stream. This API allows applications to read from a subset of all public
data flowing through Twitter. The other streaming APIs, the user stream
and the site stream, are geared towards developers who are writing an
application that provides some sort of service to Twitter users. Within
the public streaming API are three "endpoints," which are used to
determine what messages the application wishes to receive
[[5]](https://dev.twitter.com/docs/streaming-apis/streams/public).
The "sample" endpoint returns a small, random subset of all data, while the
"firehose" endpoint returns all status updates that pass through
Twitter. The endpoint that is most useful for human mobility
researchers is the "filter" stream, which allows developers to query for
status updates that match a certain filter or filters. One filtering
option limits returned statuses to only those that contain geolocation
data [[6]](https://dev.twitter.com/docs/api/1.1/post/statuses/filter).
This "filter" endpoint of the public streaming API is what the twitter
portion of the GeoDigger application uses to collect geotagged status
updates from Twitter users.

## OAuth
Since the filter endpoint of the public streaming API requires user
context [[6]](https://dev.twitter.com/docs/api/1.1/post/statuses/filter),
an important step in establishing a connection to the API is
authenticating as a certain user. The current version of the Twitter API
requires applications to authenticate using OAuth, and open
authentication protocol considered more secure than the HTTP "Basic"
authentication scheme supported by previous versions of the Twitter API
[[7]](http://oauth.net/). OAuth authentication relies on a set of tokens
and keys, which can be obtained by setting up a Twitter account and
registering an application [[8]](https://dev.twitter.com/docs)
[[9]](https://dev.twitter.com/apps).

## Tweet and User objects
The data sent to clients from the Twitter API consists of a number of
objects, two of which are used by this project. The first object is the
"Tweet," or status update
[[10]](https://dev.twitter.com/docs/platform-objects/tweets).
Tweets have a number of fields, some of which contain other embedded
objects. The fields used by GeoDigger are "created_at", which contains a
date and time value that is supposed to be the time the Tweet was
created; "coordinates," which contains a [GeoJSON](geojson.md) point;
and "user," which contains an embedded User object. User objects
themselves have a large number of fields
[[11]](https://dev.twitter.com/docs/platform-objects/users), but the
only one of interest to us is the "id_str" field, which is a string
representation of the unique integer identifier for the user who created
the Tweet. According to the Twitter documentation for the User object,
the integer ID number itself "is greater than 53 bits and some
programming languages may have difficulty/silent defects in interpreting
it." Developers are encouraged to "Use id_str for fetching the identifier
to stay on the safe side,"
[[11]](https://dev.twitter.com/docs/platform-objects/users) rather than
using the "id" field on the User object and risking an integer overflow
or other similar error.
