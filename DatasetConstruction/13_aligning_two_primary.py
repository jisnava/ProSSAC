#Program to align two primary sequence
# So one primary sequence in one file, and with its id go to the second file and take primary from there then align both
import os
import re
import math
import glob
from pathlib import Path
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#import amino
directory_path1='/home/jisna/Jisna/18_FULL_LENGTH_DATA_FOR_ASSIGNMENT/18_PDB_CA_COORD/'
#directory_path2='/home/jisna/Jisna/STRUCTURE_ASSIGNMENT/A_chain_result/'
x=0
string_1=''
string_2=''
for file in os.listdir(directory_path1):
	#print(file)
	id=file.split('.')[0]
	print(id)
	f= open('/home/jisna/Jisna/18_FULL_LENGTH_DATA_FOR_ASSIGNMENT/18_PDB_CA_COORD/'+file,"r")
	lines=f.readlines()
	x=len(lines)
	L=[]
	string_1=lines[2]
	#for i in range(0,x):
	#print(string_1)
	#print("\n")

	with open('12_Our_and_their_A_chain_only_new_line_removed.txt','r') as f:
	    line1 = f.readlines()

	if not line1:
	    sys.exit("Could not read haystack data")

	#with open('ss.txt','r') as f1:
	i=0
	s=0
	always_print=True
	now_print = False
	needle='>'+id+':A:sequence'
	needle2= '^\d'
	needle1='[0-9A-Z]:A:secstr'
	x=len(line1)
	#print(x)
	for i in range(0,x-2):
		#print("Hello")
		if (re.search(needle,line1[i])):
			#print("Hai")
			string_2=line1[i+1]
			break
	#string_2=string_1
	#print(string_2)
	alignments=pairwise2.align.globalxx(string_1,string_2)
	print(format_alignment(*alignments[0]))

"""

(re.search('>'+id+':A:sequence',line1):
		elif (re.search(needle,line1)):
			#id=line1.split(':')[0]
			#print(id)
			#i=i+1
			s=0
				always_print= True
			now_print = False
			#print(line1, end='')
			print("\n")
			print(line1)
			#print("\n")
			#f2.write(line1)
		elif '>' not in line1 and always_print:
			print(line1, end='')
			#s=s+len(line1)
			#print(s)
			#f2.write(line1)
		elif (re.search(needle1,line1)):
			now_print= True
			always_print = False
			print("\n")
			#print(line1)
		elif '>' not in line1 and now_print:
			print(line1, end='')
		elif '>' in line1:
			always_print = False
			now_print= False
			#print("\n")
	
"""
