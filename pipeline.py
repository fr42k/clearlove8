import pickle
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk import Nonterminal, nonterminals, Production, CFG
from nltk.parse import stanford
from nltk.tree import Tree
from nltk.corpus import wordnet as wn

all_tokens = pickle.load(open('tokens.dat','rb'))
all_sentences = pickle.load(open('sentences.dat','rb'))
all_keywords = pickle.load(open('keywords.dat','rb'))

def lemmatize(target):
	all_lem_tokens = []
	wnl = WordNetLemmatizer()
	for sent_tokens in target:
		lem_tokens = []
		for tokens in sent_tokens:
			tokens = [wnl.lemmatize(token) for token in tokens]
			lem_tokens.append(tokens)
		all_lem_tokens.append(lem_tokens)
	fp = open('lem_tokens.dat','wb')
	pickle.dump(all_lem_tokens,fp,True)
	fp.close()
	return all_lem_tokens

def stem(target):
	all_stem_tokens = []
	stemmer = SnowballStemmer("english")
	for sent_tokens in target:
		stem_tokens = []
		for tokens in sent_tokens:
			tokens = [stemmer.stem(token) for token in tokens]
			stem_tokens.append(tokens)
		all_stem_tokens.append(stem_tokens)
	fp = open('stem_tokens.dat','wb')
	pickle.dump(all_stem_tokens,fp,True)
	fp.close()
	return all_stem_tokens

def pos_tag(target):
	all_pos_tag_tokens = []
	for sent_tokens in target:
		pos_tag_tokens = []
		for tokens in sent_tokens:
			tokens = nltk.pos_tag(tokens)
			pos_tag_tokens.append(tokens)
		all_pos_tag_tokens.append(pos_tag_tokens)
	fp = open('pos_tag_tokens.dat','wb')
	pickle.dump(all_pos_tag_tokens,fp,True)
	fp.close()
	return all_pos_tag_tokens

def find_head(target):
	parser = stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
	java_options='-mx4g')	
	heads = []
	for sentences in target:
		head = []
		for sentence in sentences:
			flag = 0
			if (len(sentence.split())<200):
				parsing_tree = parser.raw_parse(sentence)							
				for i in (list(parsing_tree))[0].subtrees():
					if i.label() == 'NP':
						leaves = i.leaves()
				rightmost_np = leaves[-1]
				if rightmost_np.isalpha(): 
					head.append(rightmost_np)
					flag = 1
				if flag == 0:
					head.append('null')
			else:
				head.append('null')			
		heads.append(head)
		print('..')	
	fp = open('heads.dat','wb')
	pickle.dump(heads,fp,True)
	fp.close()	
	return heads		 
	
			 
def hypernym(target):
	all_hypers = []
	for s_tokens in target:
		hypers = []
		for tokens in s_tokens:
			hyper = []
			for token in tokens:
				for word_sense in wn.synsets(token):
					if word_sense.hypernyms() != []:
						for s in word_sense.hypernyms():
							for s_n in s.lemma_names():
								hyper.append(s_n)			
			hypers.append(hyper)
		all_hypers.append(hypers)
	fp = open('hypernyms.dat','wb')
	pickle.dump(all_hypers,fp,True)
	fp.close()
	return all_hypers
	
def hyponym(target):
	all_hypos = []
	for s_tokens in target:
		hypos = []
		for tokens in s_tokens:
			hypo = []
			for token in tokens:
				for word_sense in wn.synsets(token):
					if word_sense.hyponyms() != []:
						for s in word_sense.hyponyms():
							for s_n in s.lemma_names():
								hypo.append(s_n)	
			hypos.append(hypo)
		all_hypos.append(hypos)
	fp = open('hyponyms.dat','wb')
	pickle.dump(all_hypos,fp,True)
	fp.close()		
	return all_hypos	

def meronym(target):
	all_meros = []
	for s_tokens in target:
		meros = []
		for tokens in s_tokens:
			mero = []
			for token in tokens:
				for word_sense in wn.synsets(token):
					if word_sense.part_meronyms() != []:
						for s in word_sense.part_meronyms():
							for s_n in s.lemma_names():
								mero.append(s_n)				
			meros.append(mero)
		all_meros.append(meros)
	fp = open('meronyms.dat','wb')
	pickle.dump(all_meros,fp,True)
	fp.close()			
	return all_meros

def holonym(target):
	all_holos = []
	for s_tokens in target:
		holos = []
		for tokens in s_tokens:
			holo = []
			for token in tokens:
				for word_sense in wn.synsets(token):
					if word_sense.member_holonyms() != []:
						for s in word_sense.member_holonyms():
							for s_n in s.lemma_names():
								holo.append(s_n)				
			holos.append(holo)
		all_holos.append(holos)
	fp = open('holonyms.dat','wb')
	pickle.dump(all_holos,fp,True)
	fp.close()			
	return all_holos
	
find_head(all_sentences)

