c:\Python33\Scripts\pelican.exe content -o output -s publishconf.py
rem c:\Python27-64\python.exe c:\Python27-64\Scripts\s3cmd sync output/ s3://pbouda --acl-public --delete-removed
c:\Python27-64\python.exe c:\Python27-64\Scripts\s3cmd put -r output/ s3://pbouda --acl-public