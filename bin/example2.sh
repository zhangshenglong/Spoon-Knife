#!bin/sh
path="../data"
cat $path/e2_1 | tr '[A-Z]' '[a-z]' > $path/tmp
sed -i 's/ * /\n/g' $path/tmp
sort -u $path/tmp > $path/tmp2
echo "The follow words are in the first text:" 
comm -23 $path/e2_2 $path/tmp2
rm $path/tmp*
