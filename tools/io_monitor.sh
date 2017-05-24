#!/bin/bash
while :
do
echo $1 >> $2_io
cat /proc/$1/io >> $2_io
echo $1 >> $2_stat
cat /proc/$1/stat >> $2_stat
sleep 1
done
