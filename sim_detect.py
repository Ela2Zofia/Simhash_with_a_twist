import re
import jieba
import time
import pickle
from collections import defaultdict
from simhash import Simhash

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext



file = open('news','rb')
outfile = open('result', 'w')
contents = pickle.load(file)

values = []
value_dict = {}

for content in contents:
    
    a_news = ''
    for i in range(len(content)-1): # strips out the date time at the end of each piece of news
        # strips out the index of the news
        if i == 0:
            i+=1
        a_news+=content[i]
    a_news = cleanhtml(a_news)
    hash_result = Simhash(jieba.lcut(a_news))
    values.append(hash_result)



for i in range(len(values)):
    value_dict[i] = values[i]

duplicates = defaultdict(list)
values = list(value_dict.items())

# this is the value of tolrance of hamming distance between two hash values
tolerance = 9

# return a list of 
for i in range(len(values)//2 + 1):
    for j in range(i+1, len(values)):
        if values[i][1].distance(values[j][1]) < tolerance:
            duplicates[i].append(j)

print(list(duplicates.items()))

for items in list(duplicates.items()):
    outfile.write(str(items[0]) + ': ')
    for dup in items[1]:
                outfile.write(str(dup) + ', ')
    outfile.write('\n')



file.close()
outfile.close()