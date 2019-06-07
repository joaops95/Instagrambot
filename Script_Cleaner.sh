#!/bin/bash
pgrep chrom > temp.txt
cat temp.txt | while read line
do
	kill -9 $line
done
pgrep python > temp.txt
cat temp.txt | while read line
do
	kill -9 $line
done

pgrep Start_Script > temp.txt
cat temp.txt | while read line
do
	kill -9 $line
done
