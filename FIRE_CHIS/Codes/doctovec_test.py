from gensim import corpora, models, similarities
import gensim
import re, string
import numpy
import lmdb
from nltk.stem.porter import *
from os import listdir
from os.path import isfile, join
import os, sys
from scipy import spatial
import operator
import xlrd

#342 414 260 279 247

sentences = []
class LabeledLineSentence(object):
    def __init__(self,sentences):
        self.lists = sentences
        self.j = 0

    def __iter__(self):
        for sent in self.lists:
            self.j =self.j +1
            yield gensim.models.doc2vec.LabeledSentence(words= sent, tags=["sent_"+ str(self.j)])

path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/skincancer.xlsx"    
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
print first_sheet.nrows
for i in range(1,first_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = first_sheet.cell(i,0)
     sent= cell.value.split()
     sentences.append(sent)

it = LabeledLineSentence(sentences)    #contains one file of all appended doc for that categoty 
doc2vecmodel = models.Doc2Vec(it,size = 200, window = 5, min_count = 0, dm = 0)

index2wordcollection = doc2vecmodel.index2word
env = lmdb.open('wikipedia-pubmed-and-PMC-w2v')
txn = env.begin(buffers=True)
wordvector=[]

for i in range(len(doc2vecmodel.syn0)):
    #pdb.set_trace()
    #if index2wordcollection[i].startswith("SENT_"):
    #    continue
    word = index2wordcollection[i]
   
    try:
    	word = index2wordcollection[i]
        text = word.encode('UTF-8') 
        #print text 
    	lists = str(txn.get(text))
       
        if lists != 'None' :    
    	      wordvector = lists.split(" ")
	      #print "word vector is ",word,wordvector[:1]
    	      wordvector = map(lambda x:float(x), wordvector)
        else:
           wordvector = [0.00] * 200     
      	doc2vecmodel.syn0[i] = wordvector
    except Exception as e:
        print i  
        print "---------------------------------------------"
	print "Exception is ",str(e),

#----------------------------------------------------------------------
#Train Doc2Ve 
doc2vecmodel.train_words = False 
for i in range(100):
    doc2vecmodel.train(it)
doc2vecmodel.save('q01_test.doc2vec')


#-----------------------------------------------------------------------
path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/ecig.xlsx"    
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
print first_sheet.nrows
for i in range(1,first_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = first_sheet.cell(i,0)
     sent= cell.value.split()
     sentences.append(sent)

it = LabeledLineSentence(sentences)    #contains one file of all appended doc for that categoty 
doc2vecmodel = models.Doc2Vec(it,size = 200, window = 5, min_count = 0, dm = 0)

index2wordcollection = doc2vecmodel.index2word

wordvector=[]

for i in range(len(doc2vecmodel.syn0)):
    #pdb.set_trace()
    #if index2wordcollection[i].startswith("SENT_"):
    #    continue
    word = index2wordcollection[i]
   
    try:
    	word = index2wordcollection[i]
        text = word.encode('UTF-8') 
        #print text 
    	lists = str(txn.get(text))
       
        if lists != 'None' :    
    	      wordvector = lists.split(" ")
	      #print "word vector is ",word,wordvector[:1]
    	      wordvector = map(lambda x:float(x), wordvector)
        else:
           wordvector = [0.00] * 200     
      	doc2vecmodel.syn0[i] = wordvector
    except Exception as e:
        print i  
        print "---------------------------------------------"
	print "Exception is ",str(e),

#----------------------------------------------------------------------
#Train Doc2Ve 
doc2vecmodel.train_words = False 
for i in range(100):
    doc2vecmodel.train(it)
doc2vecmodel.save('q02_test.doc2vec')





#-----------------------------------------------------------------------
path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/mmr_vaccine.xlsx"    
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
print first_sheet.nrows
for i in range(1,first_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = first_sheet.cell(i,0)
     sent= cell.value.split()
     sentences.append(sent)

it = LabeledLineSentence(sentences)    #contains one file of all appended doc for that categoty 
doc2vecmodel = models.Doc2Vec(it,size = 200, window = 5, min_count = 0, dm = 0)

index2wordcollection = doc2vecmodel.index2word

wordvector=[]

for i in range(len(doc2vecmodel.syn0)):
    #pdb.set_trace()
    #if index2wordcollection[i].startswith("SENT_"):
    #    continue
    word = index2wordcollection[i]
   
    try:
    	word = index2wordcollection[i]
        text = word.encode('UTF-8') 
        #print text 
    	lists = str(txn.get(text))
       
        if lists != 'None' :    
    	      wordvector = lists.split(" ")
	      #print "word vector is ",word,wordvector[:1]
    	      wordvector = map(lambda x:float(x), wordvector)
        else:
           wordvector = [0.00] * 200     
      	doc2vecmodel.syn0[i] = wordvector
    except Exception as e:
        print i  
        print "---------------------------------------------"
	print "Exception is ",str(e),

#----------------------------------------------------------------------
#Train Doc2Ve 
doc2vecmodel.train_words = False 
for i in range(100):
    doc2vecmodel.train(it)
doc2vecmodel.save('q03_test.doc2vec')




print "ok"

#-----------------------------------------------------------------------
path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/vitaminC.xlsx"    
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
print first_sheet.nrows
for i in range(1,first_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = first_sheet.cell(i,0)
     sent= cell.value.split()
     sentences.append(sent)

it = LabeledLineSentence(sentences)    #contains one file of all appended doc for that categoty 
doc2vecmodel = models.Doc2Vec(it,size = 200, window = 5, min_count = 0, dm = 0)

index2wordcollection = doc2vecmodel.index2word

wordvector=[]

for i in range(len(doc2vecmodel.syn0)):
    #pdb.set_trace()
    #if index2wordcollection[i].startswith("SENT_"):
    #    continue
    word = index2wordcollection[i]
   
    try:
    	word = index2wordcollection[i]
        text = word.encode('UTF-8') 
        #print text 
    	lists = str(txn.get(text))
       
        if lists != 'None' :    
    	      wordvector = lists.split(" ")
	      #print "word vector is ",word,wordvector[:1]
    	      wordvector = map(lambda x:float(x), wordvector)
        else:
           wordvector = [0.00] * 200     
      	doc2vecmodel.syn0[i] = wordvector
    except Exception as e:
        print i  
        print "---------------------------------------------"
	print "Exception is ",str(e),

#----------------------------------------------------------------------
#Train Doc2Ve 
doc2vecmodel.train_words = False 
for i in range(100):
    doc2vecmodel.train(it)
doc2vecmodel.save('q04_test.doc2vec')


#-----------------------------------------------------------------------
path = "/home/raksha/FIRE-2016/CHIS_testSet/final_fire_test_data_xls/hrt.xlsx"    
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
print first_sheet.nrows
for i in range(1,first_sheet.nrows):
     #print first_sheet.row_values(i)
     cell = first_sheet.cell(i,0)
     sent= cell.value.split()
     sentences.append(sent)

it = LabeledLineSentence(sentences)    #contains one file of all appended doc for that categoty 
doc2vecmodel = models.Doc2Vec(it,size = 200, window = 5, min_count = 0, dm = 0)

index2wordcollection = doc2vecmodel.index2word

wordvector=[]

for i in range(len(doc2vecmodel.syn0)):
    #pdb.set_trace()
    #if index2wordcollection[i].startswith("SENT_"):
    #    continue
    word = index2wordcollection[i]
   
    try:
    	word = index2wordcollection[i]
        text = word.encode('UTF-8') 
        #print text 
    	lists = str(txn.get(text))
       
        if lists != 'None' :    
    	      wordvector = lists.split(" ")
	      #print "word vector is ",word,wordvector[:1]
    	      wordvector = map(lambda x:float(x), wordvector)
        else:
           wordvector = [0.00] * 200     
      	doc2vecmodel.syn0[i] = wordvector
    except Exception as e:
        print i  
        print "---------------------------------------------"
	print "Exception is ",str(e),

#----------------------------------------------------------------------
#Train Doc2Ve 
doc2vecmodel.train_words = False 
for i in range(100):
    doc2vecmodel.train(it)
doc2vecmodel.save('q05_test.doc2vec')




