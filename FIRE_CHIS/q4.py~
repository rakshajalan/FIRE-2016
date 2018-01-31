# -*- coding: utf-8 -*-
import operator
import xlrd
from itertools import product
import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import tokenize
import collections
from operator import itemgetter
from sklearn.feature_extraction.text import CountVectorizer
from numpy  import array
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from imblearn.under_sampling import ClusterCentroids
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn import svm
from imblearn.over_sampling import SMOTE
from sklearn.cross_validation import train_test_split
import os
import lmdb
from gensim import corpora, models, similarities
import gensim
from numpy  import array
import xlrd




verbose = False
ratio = 'auto'



input_list1 =[]
model_loaded = models.Doc2Vec.load('/home/raksha/FIRE-2016/query_vec.doc2vec')

q1= model_loaded.docvecs["sent_4"]


path = "/home/raksha/FIRE-2016/CHIS_TrainingData/MMRVaccineLeadToAutism_final.xlsx"
#path = "/home/raksha/FIRE-2016/CHIS_TrainingData/vitaminC_common_cold_final.xlsx"
#path = "/home/raksha/FIRE-2016/CHIS_TrainingData/women_should_Take_HRT_Post_Menopause_final.xlsx" 







myfile = open("/home/raksha/FIRE-2016/CHIS_TrainingData/q03.txt", "w")  #write sentences in text file
model_loaded = models.Doc2Vec.load('/home/raksha/FIRE-2016/q03_sentences.doc2vec') #load doc to vec repr of sentences
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)

output_file = open("/home/raksha/FIRE-2016/CHIS_TrainingData/q3_op.txt", "w") #write relevant/irrelevant class

output_file2 = open("/home/raksha/FIRE-2016/CHIS_TrainingData/q3_t2_op.txt", "w") # write support(1),oppose(-1),neutral(0)
deep_list =[]
for i in range(1,first_sheet.nrows):
     k=i+1
     string =  "sent_"+ str(i)
     data1 = model_loaded.docvecs[string] #retrieve doc to vec repr of current sent and store in deep_list 
     data1 = list(data1) 
     deep_list.append(data1)
     #print first_sheet.row_values(i)
     cell2 =  first_sheet.cell(i,1)
     cell3 =  first_sheet.cell(i,2)
     if cell2.value == "relevant":
          cell = first_sheet.cell(i,0)
          #sentences.append(sent)
          t = cell.value.encode('UTF-8') 
          myfile.write(t+"\n")  
          output_file.write("1"+"\n") 
         
     else:
          cell = first_sheet.cell(i,0)
          #sentences.append(sent)
          t = cell.value.encode('UTF-8') 
          myfile.write(t+"\n")  
          output_file.write("0"+"\n")
    
     if cell3.value == "support":   
         output_file2.write("1"+"\n") 
     elif cell3.value == "oppose":   
         output_file2.write("-1"+"\n")    
     else : 
         output_file2.write("0"+"\n")    



train_len = len(deep_list) 

#------------------------------------------------------------------------------------------------------------
path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/mmr_vaccine.xlsx" #load test data    
book = xlrd.open_workbook(path)
test_sheet = book.sheet_by_index(0)
test_len = test_sheet.nrows
test_list=[]
for i in range(1,test_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = test_sheet.cell(i,0)
     #sent= cell.value
     tp = cell.value.encode('UTF-8') 
     myfile.write(tp+"\n")  #append test data to same training sentences file inorder to generate vocab common to both train and test 
     #test_list.append(sent)


myfile.close()         
output_file.close() 
output_file2.close()  



#q1= sentences[1]
myfile = open("/home/raksha/FIRE-2016/CHIS_TrainingData/q03.txt", "r") #open file containing both training and testing sentences 
tags = myfile.readlines()

for i in range(len(tags)):
 tags[i] = str(q1) + tags[i] #query,sentence pair

with open("/home/raksha/FIRE-2016/CHIS_TrainingData/q3_op.txt") as input: #load output for training in task 1
    grades = [line.split(",") for line in input.read().splitlines()] 


bigram_vectorizer =TfidfVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1) # unigram + bigrams tokens
X_2 = bigram_vectorizer.fit_transform(tags).toarray() #numpy array storing tf-idf repr of each sentence


input_list1 = array(X_2[:train_len])
for j in range(len(input_list1)):
   np.append(input_list1[j],deep_list[j])


input_list1= preprocessing.normalize(input_list1, norm='l1') #normalize data
output_list1 = array(grades)
 
ratio = 'auto' #class imbalance technique smote
cc =  SMOTE(ratio=ratio, kind='regular')
osx,osy = cc.fit_sample(input_list1,output_list1.ravel())


import nltk
from sklearn import cross_validation
from sklearn.cross_validation import KFold, cross_val_score
#k_fold = KFold(len(osx), n_folds=5, shuffle=True, random_state=0)


# make predictions
#expected = labels_test
#predicted = model.predict(data_test)
# summarize the fit of the model

#l= cross_val_score(model, osx, osy, cv=k_fold, n_jobs=1)
#print reduce(lambda x, y: x + y, l) / len(l)



"""
data_train, data_test, labels_train, labels_test = train_test_split(osx,osy, test_size=0.3)

model = GaussianNB()
model.fit(data_train, labels_train)

# make predictions
expected = labels_test
predicted = model.predict(data_test)
# summarize the fit of the model



print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))







"""





input_list1 =[]

#for i in range(len(test_list)):
 
# tags[i] = str(q1) + test_list[i] #query,sentence pair

model_loaded = models.Doc2Vec.load('q03_test.doc2vec')
deep_list2 = []

for i in range(1,test_sheet.nrows):
     string =  "sent_"+ str(i)
     data1 = model_loaded.docvecs[string]
     deep_list2.append(data1) 



test = X_2[train_len:]
for j in range(len(test)):
   np.append(test[j],deep_list2[j])


 
test_data = preprocessing.normalize(test, norm='l1')

#print len(X_2[0])

model = GaussianNB()
model.fit(osx,osy.ravel())
predict1 = model.predict(test_data)


with open("/home/raksha/FIRE-2016/CHIS_TrainingData/q3_t2_op.txt") as input:
    output = [line.split(",") for line in input.read().splitlines()] 
input_list2= []
polar_list = []

for j in range(len(grades)):
 if grades[j]==['1']:
   input_list2.append(X_2[j]) #it contains tf_idf of sent
   polar_list.append(output[j])



#---------------testing 2nd task----------------------

test_polarity=[]
test2 = X_2[train_len:]

for j in range(len(test2)):
  if predict1[j] =='1':   #if predicted relevant
      test_polarity.append(test2[j])
      i

test_polarity = preprocessing.normalize(test_polarity, norm='l1')
import nltk
from sklearn import cross_validation
from sklearn.cross_validation import KFold, cross_val_score

polar_list= array(polar_list)
ratio = 'auto' #class imbalance technique smote
smote = SMOTE(ratio=ratio, kind='regular')
osx1,osy1 = smote.fit_sample(input_list2,polar_list.ravel())




clf = GaussianNB()
clf.fit(osx1,osy1.ravel())
predicted = clf.predict(test_polarity)
#print predicted
"""
data_train, data_test, labels_train, labels_test = train_test_split(osx1,osy1, test_size=0.3)

model = GaussianNB()
model.fit(data_train, labels_train.ravel())

# make predictions
expected = labels_test.ravel()
predicted = model.predict(data_test)
# summarize the fit of the model
"""
polar =[]
k=0
for j in range(len(predict1)):
  if predict1[j]=='0':
      polar.append(0)
  else:
     polar.append(predicted[k])
     k=k+1

from xlutils.copy import copy
from xlrd import *
w = copy(open_workbook('/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/mmr_vaccine.xlsx'))

for i in range(len(predict1)):
  w.get_sheet(0).write(i+1,1,predict1[i])
  w.get_sheet(0).write(i+1,2,polar[i])   

w.save('/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/mmr_vaccine.xlsx')
print "Done"
