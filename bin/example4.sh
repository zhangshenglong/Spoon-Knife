#!bin/sh
path="../data"
cat $path/e4_1 | tr '[A-Z]' '[a-z]' > $path/tmp1
cat $path/e4_2 | tr '[A-Z]' '[a-z]' > $path/tmp2
sed -i 's/[^A-Za-z]/\n/g' $path/tmp1
sed -i 's/[^A-Za-z]/\n/g' $path/tmp2
sort -u $path/tmp1 >$path/tmp3
sort -u $path/tmp2 >$path/tmp4
echo "The intersection is:" 
comm -12 $path/tmp3 $path/tmp4
echo "The difference set is:(in the first file)" 
comm -23 $path/tmp3 $path/tmp4
echo "The union set is:"
cat $path/tmp3 $path/tmp4 | uniq
rm $path/tmp*
