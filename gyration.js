// Calculates distances between points
function haversine(XY) {
    var p1 = XY[0].map(function(x){ return x * ( Math.PI / 180.0 ); });
    var p2 = XY[1].map(function(x){ return x * ( Math.PI / 180.0 ); });
    var d_lon = p1[0] - p2[0];
    var d_lat = p1[1] - p2[1];
    var h = Math.pow((Math.sin(d_lat/2.0)), 2) + Math.cos(p1[1]) * Math.cos(p2[1]) * Math.pow((Math.sin(d_lon/2.0)), 2);
    return 6372.8 * 2.0 * Math.atan2( Math.sqrt(h), Math.sqrt(1-h) );
}

// Calculates the centroid of a set of points
// points = [{point: [lon, lat], frequency: frequency}]
function centroid(points) {
    var sumLon=0, sumLat=0, total=0;
    for (var i=0; i < points.length; i++) {
        sumLon = sumLon + points[i].point[0] * points[i].frequency;
        sumLat = sumLat + points[i].point[1] * points[i].frequency;
        total = total + points[i].frequency;
    }
    return [ sumLon / total, sumLat / total ];
}

// Calculates the radius of gyration of a set of points
// points = [{point: [lon, lat], frequency: frequency}]
function gyration(points) {
    var cm = centroid(points);
    var sum = 0;
    for (var i=0; i < points.length; i++) {
        sum = sum + Math.pow(haversine([[points[i].point[0], points[i].point[1]], cm]), 2);
    }
    return Math.sqrt(1./points.length*sum);
}

print(haversine([[1, 2], [3, 4]]));
print(centroid( [{point: [1.0, 2.0], frequency: 5.0}, {point: [3.0, 4.0], frequency: 4.0}] ));
print(gyration( [{point: [1.0, 2.0], frequency: 5.0}, {point: [3.0, 4.0], frequency: 4.0}] ));
