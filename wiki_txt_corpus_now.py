import sys
import requests
from gensim.corpora import WikiCorpus

URL = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2'
SAVE_PATH = 'enwiki-latest-pages-articles.xml.bz2'
CORPUS_PATH = 'wiki_en.txt'

# 1. download the dump
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
with requests.get(URL, stream=True) as r:
    r.raise_for_status()
    with open(URL, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            #if chunk: 
            f.write(chunk)


# 2. parse dump into txt file
wiki = WikiCorpus(SAVE_PATH)

with open(CORPUS_PATH, 'w') as output:
    i = 0
    for text in wiki.get_texts():
        output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        i = i + 1
        if (i % 10000 == 0):
            print('Processed ' + str(i) + ' articles')
    print('Processing complete!')