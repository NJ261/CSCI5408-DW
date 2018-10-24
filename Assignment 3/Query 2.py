from nltk import word_tokenize
from nltk.corpus import stopwords
import time
from nltk import PorterStemmer
from pyspark import SparkContext
import re
import operator
from operator import add

#Loading the Data
start_time = time.time()
path_1 = "C:\\Users\\nirav\\Downloads\\WordCountData.txt"
sc = SparkContext()
textfile = sc.textFile(path_1)
singleListData = (textfile.collect())


# Process: 1 Stooping Process 
time1 = time.time()
stopWords = set(stopwords.words('english'))
words = word_tokenize(str(singleListData))
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
              
# time response: stopping process
print("PROCESS 1_STOPPING_RESPONSE TIME: %s SECONDS" % (time.time() - time1))


# PROCESS 2: Cleaning the data, removing unnecessary characters
time2 = time.time()
wordsToRemove = [",","'nan", "]", "'", ".", ";", "''", "[", "``", "'I", "'of", "'is", "'are", "'in", "'In", "'by", "'the", "'and","!", "'d","'If", "'so","'me", "'my", "(", ")", ":","'was", "'And", "'a", "'to", "'That", "'that", "'as", "'As" "'us"]
for i in range(0, len(wordsToRemove)):
    wordsFiltered = [x for x in wordsFiltered if x != wordsToRemove[i]]
print("PROCESS 2_CLEANING DATA_RESPONSE TIME: %s SECONDS" % (time.time() - time2))


# PROCESS 3: Stemming Process
time3 = time.time()
stemmedWords = PorterStemmer().stem(str(wordsFiltered))
print("PROCESS 3_STEMMING_RESPONSE TIME: %s SECONDS" % (time.time() - time3))


# PROCESS 4: number of lines, characters and occurance of characters
time4 = time.time()
stemmedWords = stemmedWords.split() #converting string in list
text2 = sc.parallelize(stemmedWords)
print ('NUMBER OF LINES IN FILE ARE: %s' % textfile.count())
chars = textfile.map(lambda s: len(s)).reduce(add)
print ('NUMBER OF CHARACTERS IN FILE ARE: %s' % chars)

words = text2.flatMap(lambda line: re.split('\W+', line.lower().strip())) #use of flatmap
words = words.filter(lambda x: len(x) > 3) 
words = words.map(lambda w : (w,1)) #use of mapping 
words = words.reduceByKey(add) #reduce by key


# Printing most 50 occurance words
print("PROCESS 4_RESPONSE TIME: %s SECONDS" % (time.time() - time4))
print(sorted(words.take(50),key=operator.itemgetter(1),reverse=True))


#time consumed for whole program
print("WHOLE PROGRAM_RESPONSE TIME: %s SECONDS" % (time.time() - start_time))
