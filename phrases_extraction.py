import nltk
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

all_sentences = pickle.load(open('sentences.dat','rb'))
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
stopwords = stopwords.words('english')
tokens = []

#Taken from Su Nam Kim Paper...
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

def leaves(tree):
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    word = word.lower()
    word = stemmer.stem(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    accepted = bool(4 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

def get_phrase(target):
	phrase = []
	source_text = word_tokenize(target)
	for token in source_text:
		if token.isalpha():			
			tokens.append(token)			
	postoks = nltk.tag.pos_tag(tokens)		
	tree = chunker.parse(postoks)
	terms = get_terms(tree)		
	for term in terms:
		phrase.append(tuple(term))
	return phrase

def corpus_get_phrases(target):
	all_phrases = []
	i = 0
	for sentences in target:
		phrases = []
		for sentence in sentences:
			phrase = []
			tokens = []
			if (len(sentence.split())<200):				
				source_text = word_tokenize(sentence)
				for token in source_text:
					if token.isalpha():			
						tokens.append(token)			
				postoks = nltk.tag.pos_tag(tokens)		
				tree = chunker.parse(postoks)
				terms = get_terms(tree)		
				for term in terms:
					phrase.append(tuple(term))
			else:
				phrase.append(())
			phrases.append(phrase)	
		all_phrases.append(phrases)				
		print(i)
		i += 1
	return all_phrases

'''
all_phrases = corpus_get_phrases(all_sentences)
fp = open('phrases.dat','wb')
pickle.dump(all_phrases,fp,True)
fp.close()
print('finish')
'''
