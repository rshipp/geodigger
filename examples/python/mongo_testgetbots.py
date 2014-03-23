import os
import math
import datetime

# This is a method being tested to find bots.

def haversine( XY ):
    p1 = [ x * ( math.pi / 180 ) for x in XY[0] ]
    p2 = [ x * ( math.pi / 180 ) for x in XY[1] ]
    d_lon = p1[0] - p2[0]
    d_lat = p1[1] - p2[1]
    h = (math.sin(d_lat/2))**2 + math.cos(p1[1]) * math.cos(p2[1]) * (math.sin(d_lon/2))**2
    return 6372.8 * 2 * math.atan2( math.sqrt(h), math.sqrt(1-h) )

u = dict()
lastuser = -1
for line in open(os.path.expanduser('test.csv'), 'r+'):
   line = line.split(',')
   user = line[0]
   if user != lastuser and lastuser != -1:
      for tweet in u['tweets']:
         # tweets is a list with the tweets of the same user
         # tweet is the current tweet of the user with [datetime, (lon, lat)]
         previousTweet = u['tweets'][len(u['tweets'])-1]
         distance = haversine([tweet[1], previousTweet[1]])
         time = datetime.datetime.strptime(tweet[0], '%Y-%m-%d %H:%M:%S')
         previousTime = datetime.datetime.strptime(previousTweet[0], '%Y-%m-%d %H:%M:%S')
         time = (time - previousTime).total_seconds() / 3600
         if time != 0:
            speed = distance / time
            # too fast, you might be a robot
            if speed > 1000: # 1000km/h
               # print the user ID and manually check if it is a bot
               print user
   if user != lastuser:
      u['tweets'] = []
      lastuser = user
   u['tweets'] += [[line[1], (float(line[2]), float(line[3]))]]

print "last user: " + user
