#!bin/sh
cd ../data
cat e2_1 | tr '[A-Z]' '[a-z]' > tmp
sed -i 's/ * /\n/g' tmp
sort -u tmp > tmp2
echo "The follow words are in the first text:" 
comm -23  e2_2  tmp2
rm tmp*
