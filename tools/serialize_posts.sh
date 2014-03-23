#!/bin/bash
# convert hash-based dumps to numbered dumps

c=0
for userid in $(cut -d, -f2 "$1" | uniq); do
    sed -i "s/$userid/$c/g" "$1"
    c=$(($c+1))
done

