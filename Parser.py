import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import collections
import pandas as pd
import random
import sys
import os
import csv



var = raw_input("Please enter file name with extension: ")
f = open(var,'rw+')


data = [line.rstrip('\n') for line in f]

with open('Parsed_Results.csv','w+') as f:
	for i in data:
		if not (i.startswith('\n') or i.startswith('Gardiner') or i.startswith('Takai') or i.startswith('Ponger')  or i.startswith('=') or i.startswith('C') or i.startswith('ID') or i.startswith('This') or i.startswith('-')):
			f.write(i+"\n")

f.close()



parsed_data = [line.rstrip('\n') for line in open('Parsed_Results.csv')]

allist = []
for i in parsed_data:
	allist.append(i.split(","))


new = []
for i in allist:
	if len(i) != 0:
		l = map(lambda each:each.strip(''), i)
		new.append(l)


A = []
B = []
C = []
Prom = []
Intra = []
GT = []


for i in allist:
	GCperc = i[4]
	A.append(float(GCperc))
	length = i[5]
	B.append(float(length))
	obsexp = i[6]
	C.append(float(obsexp))
	type1 = i[7]
	if type1 == ' Promoter':
		Prom.append(type1)
	if type1 == ' Intragenic':
		Intra.append(type1)
	if type1 == ' Gene-terminal':
		GT.append(type1)


print "There are " + str(len(new)) + " CpG islands found for the given input file"
print "The average G+C percentage is " + str(np.mean(A))
print "The average length of CpG islands is " + str(np.mean(B))
print "The average Observed/Expected ratio is " + str(np.mean(C))
print str(len(Prom)) + " of the CpG Islands are Promoter type"
print str(len(Intra)) + " of the CpG Islands are Intragenic type"
print str(len(GT)) + " of the CpG Islands are Gene-terminal type"
	

