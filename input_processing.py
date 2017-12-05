import pickle
import nltk
import numpy as np
import scipy
import operator
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk import Nonterminal, nonterminals, Production, CFG
from nltk.parse import stanford
from nltk.tree import Tree
from nltk.corpus import wordnet as wn
from feature_extraction import load_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from phrases_extraction import get_phrase

vectorizer = TfidfVectorizer()
stopwords = stopwords.words('english')

def normalize(target):
	tokens = []
	for token in word_tokenize(target):
		if token.isalpha():
			tokens.append(token)
	return tokens
	
def lemmatize(target):
	lem_tokens = []
	wnl = WordNetLemmatizer()
	for token in target:
		token = wnl.lemmatize(token)
		lem_tokens.append(token)
	return lem_tokens

def stem(target):
	stem_tokens = []
	stemmer = SnowballStemmer("english")
	for token in target:
		token = stemmer.stem(token)
		stem_tokens.append(token)
	return stem_tokens

def pos_tag(target):
	tokens = []
	tokens = nltk.pos_tag(target)	
	return tokens
		
def find_head(target):
	parser = stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
	java_options='-mx4g')	
	heads = []
	if (len(target.split())<200):
		parsing_tree = parser.raw_parse(target)							
		for i in (list(parsing_tree))[0].subtrees():
			if i.label() == 'NP':
				leaves = i.leaves()
		rightmost_np = leaves[-1]
		if rightmost_np.isalpha(): 
			heads.append(rightmost_np)
	else:
		heads = []				
	return heads		 

def hypernym(target):
	hypers = []	
	for token in target:
		for word_sense in wn.synsets(token):
			if word_sense.hypernyms() != []:
				for s in word_sense.hypernyms():
					for s_n in s.lemma_names():
						hypers.append(s_n)			
	return hypers
	
def hyponym(target):
	hypos = []
	for token in target:
		for word_sense in wn.synsets(token):
			if word_sense.hyponyms() != []:
				for s in word_sense.hyponyms():
					for s_n in s.lemma_names():
						hypos.append(s_n)	
	return hypos	

def meronym(target):
	meros = []
	for token in target:		
		for word_sense in wn.synsets(token):
			if word_sense.part_meronyms() != []:
				for s in word_sense.part_meronyms():
					for s_n in s.lemma_names():
						meros.append(s_n)						
	return meros

def holonym(target):
	holos = []
	for token in target:	
		for word_sense in wn.synsets(token):
			if word_sense.part_holonyms() != []:
				for s in word_sense.member_holonyms():
					for s_n in s.lemma_names():
						holos.append(s_n)						
	return holos

def keywords_extraction(target):	
	x = vectorizer.fit_transform(target)
	#tf-idf
	vocabulary_sort = [v[0] for v in sorted(vectorizer.vocabulary_.items(),	                                      
	key = operator.itemgetter(1))]
	sorted_array = np.fliplr(np.argsort(x.toarray()))
	key_words = []
	for sorted_array_doc in sorted_array:
		key_word = [vocabulary_sort[e] for e in sorted_array_doc[0:5]]
		#Each article provides 5 keywords
		key_words.append(key_word)
	return key_words[-1]



#get_phrase('Japanese music is popular in asian young generation.')

