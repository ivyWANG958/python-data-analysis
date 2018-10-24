# coding: utf-8
import re
import csv

all_file = ["trade-wars-news1.txt",
                   "trade-wars-news2.txt",
                   "trade-wars-news3.txt",
                   "trade-wars-news4.txt",
                   "trade-wars-news5.txt"]
read_all_file = []

for file in all_file:
    f = open(file,"r+")
    contents= f.read()
    read_all_file.append(contents)
    all_words = "".join(read_all_file)

word_count = {}

punctuation="[!@#$%^&*()_+{}:\"<>?,./;“”‘’]+"
words = re.sub(punctuation,' ', all_words) 
words_list = words.lower().split()
# add stop-word, here adopt NLTK's list of english stopwords, but one could also customlize it
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "said", "should", "now"] #could customs stop words 


for word in words_list:
    if not word in stop_words:
        if not word in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1



def get_count(word_count_tuples):
    return word_count_tuples[1]

items = sorted(word_count.items(), key = get_count, reverse = True)

#print the top 15 keywords 
for item in items[0:15]:
    print(item[0],item[1])


# full keyword frequency list into a CSV file

#items = sorted(word_count.items(), key = get_count, reverse = True)
headers = ['keyword','frequency']

with open('news.csv','w') as n:
    n_csv = csv.writer(n)
    n_csv.writerow(headers)
    n_csv.writerows(items)
    