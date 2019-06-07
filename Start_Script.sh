#!/bin/bash
cd /home/joaos/Desktop/InstaPy/Instagrambot
echo $PWD
cond=1
ola=0
while [ $cond -eq 1 ]				#Ciclo WHILE usando a variavel cond referida na primeira linha da funcao inter
	do
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
	echo "Executar script python..."
	python quickstart2.py
	let ola++
	echo "Script executado $ola vezes."
done
