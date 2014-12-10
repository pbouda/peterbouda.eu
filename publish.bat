c:\Python34\Scripts\pelican.exe content -o output -s publishconf.py
rem c:\Python27\python.exe c:\Python27\Scripts\s3cmd sync output/ s3://www.peterbouda.eu --acl-public --delete-removed
c:\Python27\python.exe c:\Python27\Scripts\s3cmd put -r output/ s3://www.peterbouda.eu --acl-public