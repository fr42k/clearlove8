import pickle
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import reuters
from nltk.corpus import stopwords

all_tokens = []
fileids = reuters.fileids()
stopwords = stopwords.words('english')
all_sentences = pickle.load(open('sentences.dat','rb'))

def text_to_words(target):
	for sentences in target:
		sent_tokens = []
		for sentence in sentences:
			tokens = []
			st = word_tokenize(sentence)
			for token in st:
				if token.isalpha():			
					if token not in stopwords:
						tokens.append(token)		
			sent_tokens.append(tokens)
		all_tokens.append(sent_tokens)
	fp = open('tokens.dat','wb')
	pickle.dump(all_tokens,fp,True)
	fp.close()
	return all_tokens
	
def text_to_sentences(fileids):	
	for fileid in fileids[:1300]:
		f = open('D:/nltk_data/corpora/reuters//'+fileid,'r')
		text = f.read()
		clean_text =  re.sub("\\n ","",text)	
		source_text = sent_tokenize(clean_text)
		all_tokens.append(source_text)
		f.close()
	#return [articles[sentences]]
	fp = open('sentences.dat','wb')
	pickle.dump(all_tokens,fp,True)
	fp.close()
	return all_tokens	

text_to_words(all_sentences)

