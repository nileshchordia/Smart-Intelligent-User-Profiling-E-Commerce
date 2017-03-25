import os

# os.system("./svm-predict  manualdataset/adhoc.dat model/train.model adhoc.prediction")
adhocfile=open("adhoc.prediction","r")
temp=adhocfile.read()
print temp