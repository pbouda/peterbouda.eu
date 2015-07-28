pelican content -o output -s publishconf.py
#s3cmd sync output/ s3://www.peterbouda.eu --acl-public --delete-removed
#s3cmd put -r output/ s3://www.peterbouda.eu --acl-public
rsync -vrz -e ssh /Users/pboua/Projects/git-github/peterbouda.eu/output/* pbouda@h2407922.stratoserver.net:/var/www/peterbouda.eu/