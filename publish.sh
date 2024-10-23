#!/bin/sh
pelican content -o output -s publishconf.py
echo 'www.peterbouda.eu' > ./output/CNAME
git pull
ghp-import output -b gh-pages
git push origin gh-pages
