import time
import jieba
import pickle
from simhash import Simhash
jieba.initialize()

file = open('news', 'rb')
outfile = open('time_data.csv', 'w')
outfile.write('Text length, Execution Time\n')

contents = pickle.load(file)

# this controls how many times the samples are tested
test_times = 100 

# list to store execution time data
time_data = []

# initialize the list
for content in contents:
    time_data.append([0,0])

for _ in range(test_times):
    for index in range(len(contents)):
        a_news = ''
        for i in range(len(contents[index])-1):
            if i == 0:
                i+=1
            a_news+=contents[index][i]
    
        token_time = time.time()
        a = Simhash(jieba.lcut(a_news, cut_all = False))
        time_needed = (time.time()-token_time)*1000
    
        time_data[index][0] += len(a_news)
        time_data[index][1] += time_needed

time_data.sort()
for length, time in time_data:
    outfile.write(str(length/test_times) + ',' + str(time/test_times) + 'Milliseconds\n')

file.close()
outfile.close()