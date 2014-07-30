#!bin/sh
cd ../data
cat e4_1 | tr '[A-Z]' '[a-z]' > tmp1
cat e4_2 | tr '[A-Z]' '[a-z]' > tmp2
sed -i 's/[^A-Za-z]/\n/g' tmp1
sed -i 's/[^A-Za-z]/\n/g' tmp2
sort -u tmp1 >tmp3
sort -u tmp2 >tmp4
echo "The intersection is:" 
comm -12 tmp3 tmp4
echo "The difference set is:(in the first file)" 
comm -23 tmp3 tmp4
echo "The union set is:"
cat tmp3 tmp4 | uniq
rm tmp*
