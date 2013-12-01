# GeoDigger

## The GeoDigger class

The GeoDigger class acts as a parent, or base class, which can be
extended by creating derivative child classes. This parent class has
four main functions: reading from the global configuration file and
setting up member variables based on its contents, setting up a
connection to a MongoDB database server and saving information to this
server, sanitizing user IDs to remove identifiable information while
retaining a unique value, and writing time stamped messages to a log file
to keep track of API connections, errors, and other possibly useful
information.

![GeoDigger UML diagram.](GDUML.png "GeoDigger UML diagram.")

## Configuration and constructor

In order to facilitate code reuse, configuration for the tool is stored
in a separate file. The GeoDigger constructor reads from this file and
sets up member variables that are used to connect to the database, write
to a log file, and read from social networking APIs. These variables are
accessible to all methods in the GeoDigger class, as well as all
GeoDigger subclasses, but most of them are only used by the base
GeoDigger class. The exception is `config`, an object that represents
all the information stored in the configuration file. Subclasses read
API connection information from attributes of this object (eg,
`config.twitter`). The GeoDigger constructor also sets up a connection
to the MongoDB server defined in the configuration file, and ensures
that a "collection" with the necessary parameters is defined on the
server. Finally, the constructor sets up a member variable called
`namespace`, with a default value of "unknown", which should be
overridden by the child class. This variable is used to determine the
source from which a data point originated, to facilitate querying data
based on source. It is also used in the user ID sanitizing method to
ensure that, for example, user #312 from Twitter (namespace "twitter")
receives a different unique identifier than user #312 from Facebook
(namespace "facebook").

## Saving to the database

Regardless of the data source being queried, each child class needs the
ability to save the information it gathers to a central database. The
GeoDigger class provides this functionality with its `save()` method.
This method takes a unique user identifier, a time stamp (assumed to be
the time a specific data point was created by the user), and an ordered
list in `[longitude, latitude]` format that tells the position from
which the data point originated. It then inserts this information into
the database as a MongoDB "document" in the correct format, along with
the "namespace" variable defined by the child class. The fact that this
method is included in the parent class means that children need to know
absolutely nothing about the database.

## User ID sanitizing

When collecting data, it is important to ensure that each user can be
uniquely identified and tied to his or her own data points. However, as
is often the case in human mobility research, user privacy is a concern
here. Since GeoDigger pulls from public social networking APIs, it might
be acceptable to simply assume that privacy is not an issue for these
users, who have chosen to opt in to publicly share their geolocation
information. This said, an effort was still made to protect the privacy
of these users. Each unique user identifier passed into the
`anonymizeUser()` method of the GeoDigger class is combined with the
namespace of the child class and passed through a one-way hashing
algorithm, SHA512. This provides us with a suitably unique identifier to
associate with data points, while abstracting from the original ID.

## Logging

The final function of the GeoDigger class is to provide logging
functionality. Knowing how many data points from an API have been
dropped due to slow network speeds, when an API connection was created,
dropped (perhaps due to network errors), or resumed might be extremely
important information. Assume for simplicity that a researcher is
attempting to analyze data obtained over a single week. If an API
connection was established on Monday of that week and continued until
Wednesday, when a network disruption caused the connection to be lost
for several hours, and finally resumed on Thursday and continued without
interruption until the end of the week, a sizeable amount of data might
have been collected. Without a log, the researcher might assume data was
being collected during the entire week, and any analysis performed would
be skewed due to the missing data. The GeoDigger log accounts for this
problem by allowing child classes to write date and time stamped messages
to a central log file whenever something of importance occurs in the
process of reading from the API. Time stamps are added automatically, so
child classes only need to call the logging method as `log("message")`.

## Usage

Users interested in collecting their own data with GeoDigger will first
have to register for whatever social network services they want to use
and collect the necessary authentication information.

   ...


## Extending

GeoDigger was designed with extensibility in mind. A single parent class
takes care of interfacing with the database server and sanitizing unique
user IDs. Specialized child classes such as TwitterDigger take care of
reading from a single API, using the `save()` method from the GeoDigger
parent class to store information to a local database, and the `log()`
method to provide time stamps for connection attempts, errors, and other
information that might be of use.

Adding support for additional social network service APIs is
straightforward - just take a look at TwitterDigger.py for example
code.
