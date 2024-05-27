#./auto.sh 50 60 &
#./auto.sh 50 55 &
#./auto.sh 50 50 &

# ./auto.sh hints_length iteration

rm -rf seq*
rm -rf tmp*

rm -rf generated*
rm -rf sos*

#./auto.sh 150 30 &
#./auto.sh 150 35 &
#./auto.sh 150 40 &
#./auto.sh 150 45 &
#./auto.sh 150 50 &
#./auto.sh 150 55 &
./auto.sh 150 60 & 
wait
