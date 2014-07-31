#!/bin/sh

function JudgeBirthday()
{
    _birthday=$1
    date -d $_birthday +%Y%m%d
    return $?
}

read -p "Enter your ID number:"  Id_Number
length=${#Id_Number}
echo "The length of the ID is:"
echo $length
flag="true"
while $flag
do
    if [ $length = "15" ]; then

        #echo $Id_Number
        birthday=`echo $Id_Number | cut -c 7-12`
        birthday="19"${birthday}
        if JudgeBirthday $birthday;then
            flag="false"
            echo "The id is righ."
        else
            echo "The birthday is wrong."
            echo "Please input ID in correct format!"
            read Id_Number
        fi
    elif [ `echo $Id_Number | grep '[0-9]\{17\}[0-9xX]'` -a $length = "18" ];then
        birthday=`echo $Id_Number | cut -c 7-14`
        if JudgeBirthday $birthday;then
            flag="false"
            echo "The id is righ."
        else
            echo "The birthday is wrong."
            echo "Please input ID in correct format!"
            read Id_Number
        fi
    else
        echo "Please input ID in correct format!"
        read Id_Number
    fi
length=${#Id_Number}
done
echo "succeed"
