#!/bin/sh
path="../data"
cat $path/e5 | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'|awk -F" " '{print $1}' | sort -u > $path/list
ip_number=$(cat $path/list | wc -l)
echo "The number of ip is $ip_number,they are:"
cat $path/list
rm $path/list
