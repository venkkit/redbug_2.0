#!/bin/sh

tag="  food_for_needy"
#4870


python3 gsheet.py Sheet1 1Y4E-pcFjpCkvY5XthgYx7AJCCKl1550QGjaBmxfdKRs
echo "--------------------Done gsheet------------------------"
python3 dsheet.py
echo "--------------------Done dsheet------------------------"
#python3 slip8.py $tag "Happy Birthday"
python3 slip8_limit.py 5802 5892 $tag "with love from"
#python3 custom8.py "with love from" "  " 30
echo "--------------------Done slip8-------------------------"
python3 pdf8.py
echo "--------------------Done pdf8-------------------------"
rm -r output/images

#python3 sam.py
#python3 sam1.py

echo "$1"