import csv 
import sys
# import csv
import random
import pandas as pd
import numpy as np
import os

trainfile=open("test.dat","w")

f = open('projextitemusermatrix.csv','r')
reader = csv.reader(f)

for num in range(1,5000):
	l=[]
	dead=random.randint(1,10)
	temp=random.sample(range(1,176),dead)
	for i in range(0,len(temp)):
		temp[i]=str(temp[i])
		f.seek(0,0)
		for row in reader:
			if(temp[i]==row[0]):
				ll=row
				l.append(ll)
# 					print

					
	arr=[]
# 	print "length of "+str(len(l))

	for i in range(2,18):
        #i denotes total no. of classes that comes from csv
		temp1=0
		for j in range(0,len(l)):
	#         print l[j][i]
			temp1 +=int(l[j][i])
	#     print "nilesh"
	#     print temp
		arr.append(temp1)
# 		print len(arr)
		
		
	classs=['Student','Homemaker','IT_Proffesional','Salesman','Senior_Citizen','Teachers','Gamers','Traveller','Sportsman','Medical','Artist','PhotoGrapher','BuisnessMan','Muscican','Fitness_Trainer','Job_Seeker']
    # 	print len(classs)
	for i, j in enumerate(arr):
		if j == max(arr):
# 			print classs[i]
			classid=i
	trainfile.write(classs[classid])
	# newarr=[]
	for k in range(0,len(l)):
		trainfile.write(" " + l[k][0]+ ":"+l[k][classid+2])
	trainfile.write("\n")
f.close()
trainfile.close()
os.system("./svm-predict test.dat  model/train.model  testingresult.prediction")