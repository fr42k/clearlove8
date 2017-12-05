from nltk.corpus import reuters
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize

fileids = reuters.fileids()
token_size = 0
doc_size = 0
for fileid in fileids[:1300]:
	f = open('D:/nltk_data/corpora/reuters//'+fileid,'r')
	text = f.read()
	num = len(word_tokenize(text))
	token_size += num
	doc_size += 1
print('Doc size: ',doc_size)
print('Token size: ',token_size)
	
