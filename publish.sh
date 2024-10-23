#!/bin/sh
pelican content -o output -s publishconf.py
ghp-import output -b gh-pages
git push origin gh-pages
