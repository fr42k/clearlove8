import pysolr
import nltk
import math
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

solr = pysolr.Solr('http://localhost:8983/solr/news', timeout=10)

def split_to_sentence(text):
	return sent_tokenize(s)

def tokenize(s):
	return word_tokenize(s)

def get_tokens(token):
	tokens = []
	wnl = WordNetLemmatizer()
	tokens = [wnl.lemmatize(token) for token in tokens]
	stopwords = stopwords.words('english')
	for token in token:
		if token not in stopwords:
			tokens.append(token)
	return tokens
'''
def extract_keyword(corpus):
	index = 0
	dic = {}
	tf_idf = {}
	for text in corpus:
		token0 = tokenize(text)
		tokens = get_tokens(token0)
		dic[index] = tokens
		index += 1
		 				
	for i in range(index):
		for token in dic[i]:
			count = 0
			tf = dic[i].count(token)/len(dic[i])
			for j in range(index):
				if token in dic[j]:
					count += 1
			idf = math.log(index/count)
			tf_idf[token] = tf * idf
		terms_sorted_tfidf_desc = sorted(tf_idf.items(), key=lambda x: -x[1])  
		terms, scores = zip(*terms_sorted_tfidf_desc)
		keywords = terms[:k]
'''		
def solr_search(s):
	results = solr.search(s)
	print("Saw {0} result(s).".format(len(results)))
	for result in results:
		print("The id is '{0}'.".format(result['id']))
