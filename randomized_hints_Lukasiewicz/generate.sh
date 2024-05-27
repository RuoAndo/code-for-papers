cat manyval.first > tmp-${1}-${2}
echo "" >> tmp-${1}-${2}

shuf -n ${2} hints > hints-${1}-${2}
cat hints-${1}-${2} >> tmp-${1}-${2}

#shuf -n ${1} hints >> tmp-${1}-${2}

echo "end_of_list." >> tmp-${1}-${2}


