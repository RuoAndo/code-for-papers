shuf -n 40 $1 > tmp-1
shuf -n 40 $2 > tmp-2
shuf -n 40 $3 > tmp-3

sort -n tmp-1 > tmp-1.s
sort -n tmp-2 > tmp-2.s
sort -n tmp-3 > tmp-3.s

paste tmp-1.s tmp-2.s tmp-3.s -d "," > tmp
