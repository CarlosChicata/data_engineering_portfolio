#!/bin/bash
# this script create a back up of mongoDB and zipped its.

echo 'Welcome! i will create a back Up of mongoDB and zip it. '

current_path=`pwd`
backup_path=$current_path'/backupMongo'
destination_path='backupTestingDB.tar.gz'

if [ ! -d $backup_path ]; then
    mkdir 'backupMongo'
fi

echo '==============> 1/2 : generate backup'
mongodump --host localhost --port 27017 --db chazkiv2 --gzip --out=$backup_path
echo '==============> 2/2 : zippping backup'
tar -cvzf $destination_path  $backup_path
echo '==============> FINISH PROCCESS'
exit 1