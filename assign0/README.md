 Handle the stop words:
 
 The stop words list here adopt NLTK's list of english stopwords, but one could also customlize it by adding morewords to that list.
 
 Discussion or demo:
 
 1. To locate one keyword in articles, we could use index. First to use edges and nodes to create matrix, then index words. Ref here: [
textrank 关键词提取-python实现](https://blog.csdn.net/y12345678904/article/details/77855936)
 
 2. If we want to reuse the code for future analysis, we could write functions for keyword extraction from one file, and later call it while needed. While dealing with keyword extraction with a lager amount of files, we could run the same function on every different files. It seems more workable instead of use function on one long string -- in this case we may need to combine files to one string or divide one file to serveral strings, it add workload.
 
 3. I used the first method, to assemble the content of all 5 files and extract keyword list form one string. Because here the data size is smell, so the use of two method wouldn't make much difference.
 But for practical usage, the second method (extract keyword-frequency list for all 5 files first and then merge the keyword-frequency) may be better for two reasons:
 
    (1) Facing a large amount of data, put all files together and extract keywords could be inefficient due to the size, function usage and further reuse concern. 
 
    (2) Here we only have the words count，but for more accurate we could analysis words weight in files. To do that we need to consider the frequency of a word in one file, and also the files that contain the word in all files. So we need to have the files separately instead of merge them together. Ref here: [tf-idf](https://zh.wikipedia.org/wiki/Tf-idf)  
