#!/bin/bash

#for f in /*.txt; do
#	echo $f
#	nbChar=$(wc -l < $f)
#	echo $nbChar; 
#done

find Allemand  -type f -print0| xargs  -0  grep -o  c | wc -w
