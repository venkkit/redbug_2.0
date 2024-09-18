#!/bin/sh

tag="groceries"


python3 gsheet.py Rough_sheet 1dh3U-baiXygFzQwh5IWmU09iQRZav5mc55vlY4oqbcI
echo "--------------------Done gsheet------------------------"
python3 dsheet.py
echo "--------------------Done dsheet------------------------"
#echo $msg
python3 slip6.py $tag "with love from"
#python3 slip6_1.py Education
echo "--------------------Done slip6-------------------------"
python3 pdf6.py
echo "--------------------Done pdf6-------------------------"
rm -r output/images

#python3 sam.py
#python3 sam1.py

echo "$1"