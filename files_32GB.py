import os
import glob2
import pandas as pd
import time
import matplotlib as plt
import operator
import pandas as pd
from collections import Counter

#to print 100 frequent words according to most freq_words list
def by_freq(word_dict):
    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1))
    list_of_common_words = sorted(sorted_words, key=operator.itemgetter(1), reverse = True)
    common_words = list_of_common_words[0:100]
    return common_words


start = time.time()
# word_list = []
words_dict = {}  #we intialise a global variable which is dictionary

file_list = glob2.glob('C:\\Users\\dubey\\PycharmProjects\\big_data\\dataset\\data_32GB.split*.log00*')
print(file_list)
#now read the file
for each_file in file_list:
    with open(each_file, 'r') as f:
        for line in f:
            for word in line.split():
                word.replace("+", "") #remove the "+" char and replace with no space
                if word in words_dict:  #check if the word in the file is in dictionary
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1   #we directly read each word into the dictionary so that there is no iteration on the same word_list again
  #we save the memory space
    f.close()

print(f"Number of words: {len(words_dict)}")
sorted_word_count = by_freq(words_dict)
print(sorted_word_count) #print most frequent word line by line
end = time.time()
print("Execution Time : ", end - start)
x = dict(sorted_word_count)
df = pd. Series(x, name = 'Freq')
df.to_csv(path = 'C:/Users/dubey/PycharmProjects/big_data/output.csv')

