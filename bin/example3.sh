#!/bin/sh
read -p "Enter your mobile phones:"  numb
#length=$(echo $numb | wc -c)
#length=$(( $length - 1 ))
length=${#numb}
echo $length
flag="true"
while $flag
do
    if [ $length = "15" -o $length = "18" ]; then
          
        #echo $numb
        if [ `echo $numb | grep  '[0-9]\{15\}\|[0-9]\{18\}\|[0-9]\{17\}[0-9xX]'` ];then
            flag="false"
            echo "The id is righ."
        fi        
    else
    	echo "Please input ID in correct format!"
        read STR
        numb=$STR
    fi
#length=$(echo $numb | wc -c)
#length=$(( $length - 1 ))
length=${#numb}
done
echo "succeed"
