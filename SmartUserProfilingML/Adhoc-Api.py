from flask import Flask, request,json
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps
import csv 
import sys
# import csv
import random
import pandas as pd
import numpy as np
import os
from flask_restful import reqparse
import ast
from flask import Response


app = Flask(__name__)
# api = Api(app)

@app.route('/product')
def api_hello():
	print "nilGT"
	trainfile=open("adhoc.dat","w")
	f = open('projextitemusermatrix.csv','r')
	reader = csv.reader(f)
#     print request.args['productid']
	if 'productid' in request.args:
		d=request.args.getlist('productid')
	else:
		return 'Invalid ProductId'
	print d
	print str(type(d))+"nileshtype"
	for q in d:
		print q
	# q=[int(i) for i in ast.literal_eval(d)]
	# json_list = json.dumps(d)
	# print len(json_list)
	# print json_list[0],json_list[1]
	# parser=reqparse.RequestParser()
	# parser.add_argumnet('productid',type=list)
	# args=parser.parse_args()
	# parser.add_argumnet('productid',action='append')


	for num in range(1,2):
		l=[]
# 	dead=random.randint(1,10)
# 	print "dead="+str(dead)
# 	temp=random.sample(range(1,176),dead)
		temp=d  #take variable on flask
		for i in range(0,len(temp)):
			temp[i]=str(temp[i])
	#         print temp
			f.seek(0,0)
			for row in reader:
				if(temp[i]==row[0]):
					ll=row
					l.append(ll)
# 					print ll

					
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
	##for prediction the adhoc query
	os.system("./svm-predict  adhoc.dat  model/train.model adhoc.prediction")
	adhocfile=open("adhoc.prediction","r")
	# adhocfile=open("adhoc.prediction","r")

	userProfile=adhocfile.read()
	# print type(userProfile)
	userProfile=userProfile[:-1]
	# print userProfile+"gttttttttttttttt"
	js = json.dumps(userProfile)
	print type(js)
	resp = Response(js, status=200, mimetype='application/json')
	return resp
	# print temp





if __name__ == '__main__':
	app.run()


