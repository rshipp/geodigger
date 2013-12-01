#!/bin/bash
# onepage.sh
# Combine all documents into one large file.

pages=( onepage_disclaimer.txt index.md twitter.md tweepy.md mongodb.md
        geojson.md pyramid.md geodigger.md twitterdigger.md
        postprocessor.md ui.md )
onepage=onepage.md

rm $onepage
for page in ${pages[@]}; do
    sed 's/(\([a-z]*\).md)/(#\1)/g; s/([a-z]*.md\(#[a-z]*\))/\1/g' $page >> $onepage
    echo >> $onepage
done
