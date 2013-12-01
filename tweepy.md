Tweepy
======

Tweepy is one of a number of Python libraries that adds support for
using Twitter's APIs. It was chosen over other Twitter libraries
because, at the time of this writing, it is under active development and
has full support for all of Twitter's features, including authenticating
via OAuth and connecting to the streaming APIs. Unfortunately, tweepy is
not well documented, especially when it comes to the streaming APIs;
however, this lack of documentation is helped by the fact that the
tweepy developers used a very predictable, "Pythonic" style and closely
followed the spirit of the Twitter APIs. Once a developer understands
the basic rules governing tweepy usage, delving deeper into Twitter API
internals with this library becomes trivial.

## OAuth

The first hurdle in the path of any developer who wishes to use tweepy
in their own application is authenticating to Twitter via OAuth.
Assuming Twitter developer and application keys and secrets have already
been obtained, this is relatively simple. First, the tweepy library mist
be imported into the Python script:

    import tweepy

Once this is done, an authentication handler is set up, using the
consumer key, consumer secret, access token key, and access token
secret, all of which can be found on the Twitter developer "Manage
Apps" page.

    auth = tweepy.OAuthHandler(myConsumerKey, myConsumerSecret)
    auth.set_access_token(myAccessTokenKey, myAccessTokenSecret)

This `auth` variable can be passed to other functions and used to
authenticate to various Twitter services.

## Setting up a listener

The first step in connecting to one of the avaiable Twitter streaming
API endpoints is to create a "Stream Listener" class that extends
`tweepy.StreamListener`, and implements one or more of the virtual
methods of the parent class:

    class MyStreamListener(tweepy.StreamListener):

        def on_status(self, status):
            # This code will be executed automatically whenever the
            # listener recieves a "Tweet," or status, from the streaming
            # API. It is passed a 'status' object, which acts like a
            # Python dictionary, and includes all fields described in
            # the Twitter developer documentation for the "status"
            # object.

        def on_error(self, code):
            # This code will be executed automatically whenever the
            # listener recieves an error message from the streaming API.
            # It is passed an integer value representing the error code.

        ...

For more information on the parent methods available, see the tweepy
documentation.

Once a listener class has been created, the developer can create an
instance of this class and pass it into the constructor for the tweepy
"Stream" class, along with the previously created authentication
handler:

    streamer = tweepy.Stream(auth=auth, listener=MyStreamListener(),
            timeout=5)

The `timeout` parameter is optional, and defines the length of time, in
seconds, for which the stream listener shoudl wait before throwing a
timeout exception.

Finally, choose a streaming endpoint - one of `filter`, `firehose`, or
`sample`, and start listening to the stream. For geolocation data
mining, the most useful endpoint is `filter`, which, when passed a
`locations` parameter, returns only geotagged statuses:

    streamer.filter(locations=[-180.0,-90.0,180.0,90.0])

Adjust the coordinates as necessary; those shown above do not limit
returned data to a certain area, instead matching statuses from anywhere
in the world.
