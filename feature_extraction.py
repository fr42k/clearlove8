import numpy as np
import scipy
import operator
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import reuters
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

corpus = []
fileids = reuters.fileids()
vectorizer = TfidfVectorizer()
stopwords = stopwords.words('english')

def load_corpus(start,end):
	for fid in fileids[start:end]:
		tokens = []
		token_to_text = ''
		f = open('D:/nltk_data/corpora/reuters//'+fid,'r')
		text = f.read() 
		source_text = word_tokenize(text)
		for word in source_text:
			if word.isalpha() and len(word)>3:
				word = word.lower()		
				#All keywords should be lower.	
				if word not in stopwords:
					tokens.append(word)
		for token in tokens:
			token_to_text = token_to_text + ' ' + token + ' '	
		corpus.append(token_to_text)
		f.close()
	return corpus
	
def keywords_extraction(corpus):	
	x = vectorizer.fit_transform(corpus)
	#tf-idf
	vocabulary_sort = [v[0] for v in sorted(vectorizer.vocabulary_.items(),
	                                      key = operator.itemgetter(1))]
	sorted_array = np.fliplr(np.argsort(x.toarray()))
	key_words = []
	for sorted_array_doc in sorted_array:
		key_word = [vocabulary_sort[e] for e in sorted_array_doc[0:5]]
		#Each article provides 5 keywords
		key_words.append(key_word)
	return key_words
'''	
load_corpus(0,1300)
k = keywords_extraction(corpus)
fp = open('keywords.dat','wb')
pickle.dump(k,fp,True)
fp.close()
'''
