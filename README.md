GeoDigger
=========

Collect and filter location information from social network services.

[Read more](docs/index.md)

## Requirements

GeoDigger has only been tested on Linux. It may or may not work on
Windows or Mac OSX systems.

* Python 2.7
* MongoDB Server >= 2.4.6

### Python Modules

* Tweepy >= 2.1
* PyCrypto >= 2.6.1
* PyMongo >= 2.6.3

## Installation

To install the GeoDigger script and libraries, use:

    python setup.py install

## Usage

1. Make sure you have a MongoDB server installed and running. Running
   GeoDigger on the same machine as the database server is easiest, and
   is recommended.

2. Obtain all the developer access secrets for the social networks you want to
   use. (Currently, only Twitter is supported.)

3. Create a configuration file. See
   [examples/conf/geodigger.conf](examples/conf/geodigger.conf) for an
   example.

4. Run the GeoDigger script, passing in the paths to your configuration
   and log files. GeoDigger will try to create the log file if it does
   not already exist.

    `geodigger --conf MY_CONFIG_FILE --log MY_LOG_FILE`


## Support

To submit bug reports, use GeoDigger's GitHub
[issues](https://github.com/rshipp/geodigger/issues) page.

## Hacking

If you want to add functionality, such as support for a new social
network, see the [extending](docs/geodigger.md#extending) section of the
GeoDigger documentation. Pull requests are welcome.
