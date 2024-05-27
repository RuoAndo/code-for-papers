
sort -n generated3-150-30 > tmp1
sort -n generated3-150-35 > tmp2
sort -n generated3-150-40 > tmp3
sort -n generated3-150-45 > tmp4
sort -n generated3-150-50 > tmp5
sort -n generated3-150-55 > tmp6
sort -n generated3-150-60 > tmp7

paste tmp1 tmp2 tmp3 tmp4 tmp5 tmp6 tmp7 -d "," > generated

sort -n sos3-150-30 > tmp1
sort -n sos3-150-35 > tmp2
sort -n sos3-150-40 > tmp3
sort -n sos3-150-45 > tmp4
sort -n sos3-150-50 > tmp5
sort -n sos3-150-55 > tmp6
sort -n sos3-150-60 > tmp7

paste tmp1 tmp2 tmp3 tmp4 tmp5 tmp6 tmp7 -d "," > sos


