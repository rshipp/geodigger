import math

# Calculates distances between points
def haversine(XY):
    p1 = [ x * ( math.pi / 180 ) for x in XY[0] ]
    p2 = [ x * ( math.pi / 180 ) for x in XY[1] ]
    d_lon = p1[0] - p2[0]
    d_lat = p1[1] - p2[1]
    h = (math.sin(d_lat/2))**2 + math.cos(p1[1]) * math.cos(p2[1]) * (math.sin(d_lon/2))**2
    return 6372.8 * 2 * math.atan2( math.sqrt(h), math.sqrt(1-h) )

# Calculates the centroid of a set of points
# points = { (lon, lat): frequency }
def centroid(points):
    sumLon = 0
    sumLat = 0
    total  = 0
    for point in points:
        sumLon = sumLon + point[0] * points[point] 
        sumLat = sumLat + point[1] * points[point]
        total = total + points[point]
    return [ sumLon / total, sumLat / total ]

# Calculates the radius of gyration of a set of points
# points = { (lon, lat): frequency }
def gyration(points):
    sum = 0
    cm = centroid(points)
    for point in points:
        sum = sum + math.pow(haversine([[point[0], point[1]], cm]), 2)
    return math.sqrt(1./len(points)*sum)

print(haversine([[1, 2], [3, 4]]))
print(centroid( {(1.0, 2.0): 5.0, (3.0, 4.0): 4.0} ))
print(gyration( {(1.0, 2.0): 5.0, (3.0, 4.0): 4.0} ))
