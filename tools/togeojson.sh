#!/bin/bash
# Convert a a properly formatted file to a GeoJSON polygon.
filename="${1/.*}"

cat << EOF > "$filename.geojson"
{
    "type": "Polygon",
    "coordinates": [[
EOF
sed 's/ /\n/g; s/,/, /g;' "$filename.csv" | sed 's/^/        [/; s/$/],/' >> "$filename.geojson"
cat << EOF >> "$filename.geojson"

    ]]
}
EOF
