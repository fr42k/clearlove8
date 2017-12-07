import pysolr
import nltk
import math
from input_processing import *
from phrases_extraction import get_phrase
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

solr = pysolr.Solr('http://localhost:8983/solr/news8', timeout=10)
stopwords = stopwords.words('english')
switcher = {
	'1': 'tokens', '2': 'lem_tokens', '3': 'stem_tokens', '4': 'pos_tag_tokens',
	'5': 'hypernyms', '6': 'hyponyms', '7': 'meronyms', '8': 'holonyms',
	'9': 'heads', '10': 'phrases',		
}
func_switcher = {
	'1': normalize, '2': lemmatize, '3': stem, '4': pos_tag,
	'5': hypernym, '6': hyponym, '7': meronym, '8': holonym,
	'9': find_head, '10': get_phrase,
}

def solr_search(f,sentence):
	all_str = ''
	for i in range(len(f)):
		kind = switcher.get(f[i])
		func = func_switcher.get(f[i])
		str0 = ''
		if f[i] == '9':
			s = func(sentence)
			str0 = s[0]
		if f[i] == '10':
			try:
				s = func(sentence)
				for word in s:
					if str(word) != '()':			
						str0 = str0 + str(word) + ','
			except:
				print('.')	
		if f[i] == '4':
			text_tokens = normalize(sentence)
			s = func(text_tokens)
			for word in s:			
				str0 = str0 + str(word) + ','
		if f[i] in {'1', '2', '3', '5', '6', '7', '8'}:
			if f[i] == '1':
				s = func(sentence)
				for word in s:
					if word.isalpha():
						if word not in stopwords:
							str0 = str0 + word + ','
			else:
				text_tokens = normalize(sentence)
				s = func(text_tokens)
				for word in s:
					if word.isalpha():
						if word not in stopwords:
							str0 = str0 + word + ','
		if str0 != '':
			p_str = '%s:%s' %(kind,str0)
		else:
			p_str = ''
			print('s% is null.' %(kind))
		all_str = all_str + ' ' + p_str 
	results = solr.search(all_str)
	print("Saw {0} result(s).".format(len(results)))
	for result in results:
		print("The doc_id is '{0}'.".format(result['doc_id']))
		print("The sent_id is '{0}'.".format(result['sent_id']))
		print("The sentence is '{0}'.".format(result['sentence']))
		for j in range(len(f)):
			kind = switcher.get(f[j])
			print("The %s are "%(kind),result[kind])

def print_info():
	ls = []
	print('Please choose a kind of search index:')
	print('1. tokens; 2. lem_tokens; 3. stem_tokens; 4. pos_tag_tokens;')
	print('5. hypernyms; 6. hyponyms; 7. meronyms; 8. holonyms;')
	print('9. heads; 10. phrases;')
	m = input('How many fields would you like to combine:')
	for i in range(int(m)):
		i = input('Input:')
		ls.append(i)
	print("=" * 80)
	return ls
	
if __name__ == "__main__":
	text = 'Mounting trade friction between the U.S. And Japan has raised fears among many of Asia\'s exporting nations that the row could inflict far-reaching economic damage, businessmen and officials said.'		
	while True:
		print("#" * 80)
		solr_search(print_info(), text)



