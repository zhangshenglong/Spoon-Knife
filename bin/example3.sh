#!/bin/sh
read -p "Enter your mobile phones:"  numb
length=$(echo $numb | wc -c)
length=$(( $length - 1 ))
echo $length
flag="true"
while $flag
do
    if [ $length = "15" -o $length = "18" ]; then

        echo $numb
        if [ `echo $numb | grep  '[1-9]\{8\}\(0[1-9]\|1[0-2]\)\(0[1-9]\|[12][0-9]\|3[0-1]\)[0-9]\{3\}\|[1-9]\{6\}\(20\(0[0-9]\|1[0-4]\)\|19[0-9]\{2\}\)\(0[1-9]\|1[0-2]\)\(0[1-9]\|[12][0-9]\|3[0-1]\)[0-9]\{3\}[0-9xX]
'` ];then
            flag="false"
            echo "The id is righ."
        fi
    else
        echo "Please input ID in correct format!"
        read STR
        numb=$STR
    fi
length=$(echo $numb | wc -c)
length=$(( $length - 1 ))
done
echo "succeed"
