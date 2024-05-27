#!/bin/bash

COUNT=0

while [ $COUNT -lt ${1} ]; do
    ./generate.sh ${1} ${2}; ./otter < tmp-${1}-${2} > tmp-out-${1}-${2};

    grep -a "clauses generated" tmp-out-${1}-${2} | grep -v Binary | tee -a generated-${1}-${2}
    grep -v Binary generated-${1}-${2} > generated2-${1}-${2}
    
    grep -a "sos size" tmp-out-${1}-${2} | grep -v Binary | tee -a sos-${1}-${2}
    grep -v Binary sos-${1}-${2} > sos2-${1}-${2}

    cp tmp-${1}-${2} tmp-${1}-${2}.${COUNT}

    COUNT=`expr $COUNT + 1` # COUNT ðCNg
done

cat generated2-${1}-${2} | awk '{print $3}' > generated3-${1}-${2}

cat sos2-${1}-${2} | awk '{print $3}' > sos3-${1}-${2}

