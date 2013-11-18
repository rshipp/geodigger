"""
This is the postprocessor for GeoDigger. It attempts to remove some
"noise" from geotagged information in a Mongo database. 

BE CAREFUL!
This script will permanently delete information from the database. This
cannot be undone.
"""

class GeoPostProcessor(object):
    def __init__(self):
        self.numDocs = 0
        self.MAXSPEED = 95

    def speedLimit(self):
        """Enforce a speed limit of 95 MPH.
           Returns True if a record should be deleted, False otherwise.
        """
        # First, we need to convert our two lat/long points into a
        # distance in miles.

        # TODO ...

        # Then, check the speed.
        if distance/dtime > self.MAXSPEED:
            return True
        else:
            return False


    def blacklistedUsers(self):
        """Remove explicitly blacklisted users."""
        return self.doc['userID'] in config.blacklist


    def topNPercent(self):
        """Find the top N% of users by number of posts. These users are
           probably bots.
        """
        # We don't want to (and probably can't) store the whole database
        # in memory, so let's do this dynamically.
        # 


    def analyze(self):
        """Analyse the Mongo databse and determine what documents should
           be removed.

           self.numDocs will be set to the number of "noise" documents
           found.
        """


    def clean(self):
        """Permanently remove documents from the database."""




if __name__ == "__main__":
    g = GeoPostProcessor()
    print "Finding 'noise' in the database..."
    g.analyze()
    print str(d.numDocs) + "'noise' documents identified. Do you want to delete them?"
    print "This action cannot be undone!"
    while True:
        print "Continue? (yes/no)"
        answer = raw_input.lower()
        if answer == 'yes':
            break
        elif answer == 'no'
            exit()

    # Continue
    g.clean()
    print "All done. The database should be less noisy now."
