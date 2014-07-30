#!/bin/sh
cd ../data
cat e5 | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'|awk -F" " '{print $1}' | sort -u > list
num=$(cat list | wc -l)
echo "The number of ip is $num,they are:"
cat list
rm list
