#!/bin/bash


cut -f 1,4 $1 | sed 's/SP[0-9]\{3\}_0*\([0-9]\)/\1/g' > $(basename $1 .tsv)_no_count_minid.tsv
