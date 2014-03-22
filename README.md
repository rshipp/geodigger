GeoDigger
=========

Collect and filter location information from social network services.

## Requirements

GeoDigger has only been tested on Linux. It may or may not work on
Windows or Mac OSX systems.

Python 2.7
MongoDB Server >= 2.4.6

### Python Modules

Tweepy >= 2.1
PyCrypto >= 2.6.1
PyMongo >= 2.6.3

## Installation

To install the GeoDigger script and libraries, use:

    git clone git://github.com/GeoDigger/geodigger.git
    sudo python setup.py install

## Usage

* Make sure you have a MongoDB server installed and running. Running
  GeoDigger on the same machine as the database server is easiest, and
  is recommended.

* Obtain all the developer access secrets for the social networks you want to
  use. (Currently, only Twitter is supported.)

* Create a configuration file. See
  [examples/conf/geodigger.conf](examples/conf/geodigger.conf) for an
  example.

* Run the GeoDigger script, passing in the paths to your configuration
  and log files. GeoDigger will try to create the log file if it does
  not already exist.

    geodigger --conf MY_CONFIG_FILE --log MY_LOG_FILE

## Documentation and Papers

The GeoDigger documentation describes the reasoning and technologies
behind the project, and explains how to extend GeoDigger functionality.
You can read the documentation online [here](docs/index.md) (or, if you
prefer a single page, try [this](docs/onepage.md)).

GeoDigger is also the subject of an ongoing research project; links to
reports will be provided as they become available.

## Support

To submit bug reports, use GeoDigger's GitHub
[issues](https://github.com/GeoDigger/geodigger/issues) page.

If you have questions or comments about using GeoDigger, you can send
them to `rshipp at mines dot edu`.

## Hacking

If you want to add functionality, such as support for a new social
network, see the [extending](docs/geodigger.md#Extending) section of the
GeoDigger documentation. Pull requests are welcome.
