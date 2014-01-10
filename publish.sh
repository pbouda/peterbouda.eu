pelican content -o output -s publishconf.py
s3cmd sync output/ s3://www.peterbouda.eu --acl-public --delete-removed
