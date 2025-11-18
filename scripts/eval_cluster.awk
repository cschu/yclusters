#!/bin/awk -f 

BEGIN { OFS="\t"; }
/^CLUSTER/ { 
	if ($8==0) {spire_core="NA"} else {spire_core=($7/$8>0.95)};
	if ($6==0) {pg3_core="NA"} else {pg3_core=($5/$6>0.95)};
	print FILENAME,$0,($3/$4>0.95),pg3_core,spire_core;
}
