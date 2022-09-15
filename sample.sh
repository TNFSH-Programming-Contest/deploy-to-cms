#!/bin/bash
cd /path/to/repo
pwd
git reset --hard HEAD
git clean -fd
git pull
cmsImportTask ./pA/ -u --no-statement
cmsImportTask ./pB/ -u --no-statement
cmsImportTask ./pC/ -u --no-statement
cmsImportTask ./pD/ -u --no-statement
cmsImportTask ./pE/ -u --no-statement
cmsImportTask ./pF/ -u --no-statement
echo "Done!"
