
while :
do
    year="$((RANDOM %3))""$((RANDOM %10))""$((RANDOM %10))""$((RANDOM %10))"
    if [ "$year" -gt "1980" ] && [ "$year" -lt "2050" ];then
        break
    fi
done
echo $year

while :
do
    month="$((RANDOM %13))"
    if [ "$month" -gt "0" ];then
        break
    fi
done
echo $month

while :
do
    day="$((RANDOM %29))"
    if [ "$day" -gt "0" ];then
        break
    fi
done
echo $day

while :
do
    hour="$((RANDOM %24))"
    if [ "$hour" -ge "0" ];then
        break
    fi
done
echo $hour


while :
do
    minute="$((RANDOM %60))"
    if [ "$minute" -ge "0" ];then
        break
    fi
done
echo $minute

while :
do
    second="$((RANDOM %60))"
    if [ "$second" -ge "0" ];then
        break
    fi
done
echo $second

python3 calculate_core.py 阳历 $year $month $day $hour $minute $second
