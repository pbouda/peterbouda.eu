c:\Python36\Scripts\pelican.exe content -o "c:\Users\Peter Bouda\Nextcloud\Website" -s publishconf.py
rem c:\Python27\python.exe c:\Python27\Scripts\s3cmd sync output/ s3://www.peterbouda.eu --acl-public --delete-removed
rem c:\Python27\python.exe c:\Python27\Scripts\s3cmd put -r output/ s3://www.peterbouda.eu --acl-public