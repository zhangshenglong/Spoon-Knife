#!bin/sh
echo "The current user is:"
who |awk '{print $1}'|sort -u
