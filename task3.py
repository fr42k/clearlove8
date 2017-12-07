import pysolr
import nltk
import math
from input_processing import *
from phrases_extraction import get_phrase
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

solr = pysolr.Solr('http://localhost:8983/solr/news8', timeout=100)
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
	kind = switcher.get(f)
	func = func_switcher.get(f)
	if f == '9':
		s = func(sentence)
		results = solr.search('%s:%s' %(kind,str(s[0])))
		print("Saw {0} result(s).".format(len(results)))
		for result in results:
			print("The doc_id is '{0}'.".format(result['doc_id']))
			print("The sent_id is '{0}'.".format(result['sent_id']))
			print("The sentence is '{0}'.".format(result['sentence']))
			print("The %s are "%(kind),result[kind])
	if f == '10':
		try:
			s = func(sentence)
			str0 = ''
			for word in s:
				if str(word) != '()':			
					str0 = str0 + str(word) + ','
			results = solr.search('%s:%s' %(kind,str0))
			print("Saw {0} result(s).".format(len(results)))
			for result in results:
				print("The doc_id is '{0}'.".format(result['doc_id']))
				print("The sent_id is '{0}'.".format(result['sent_id']))
				print("The sentence is '{0}'.".format(result['sentence']))
				
				print("The %s are "%(kind),result[kind])	
		except:
			print('.')	
	if f == '4':
		text_tokens = normalize(sentence)
		s = func(text_tokens)
		str0 = ''
		for word in s:			
			str0 = str0 + str(word) + ','
		results = solr.search('%s:%s' %(kind,str0))
		print("Saw {0} result(s).".format(len(results)))
		for result in results:
			print("The doc_id is '{0}'.".format(result['doc_id']))
			print("The sent_id is '{0}'.".format(result['sent_id']))
			print("The sentence is '{0}'.".format(result['sentence']))
			print("The %s are "%(kind),result[kind])
	if f in {'1', '2', '3', '5', '6', '7', '8'}:
		if f == '1':
			s = func(sentence)
		else:
			text_tokens = normalize(sentence)
			s = func(text_tokens)
		str0 = ''
		for word in s:
			if word.isalpha():
				if word not in stopwords:
					str0 = str0 + word + ','
		results = solr.search('%s:%s' %(kind,str0))
		print("Saw {0} result(s).".format(len(results)))
		for result in results:
			print("The doc_id is '{0}'.".format(result['doc_id']))
			print("The sent_id is '{0}'.".format(result['sent_id']))
			print("The sentence is '{0}'.".format(result['sentence']))
			print("The %s are "%(kind),result[kind])


def print_info():
	print('Please choose a kind of search index:')
	print('1. tokens; 2. lem_tokens; 3. stem_tokens; 4. pos_tag_tokens;')
	print('5. hypernyms; 6. hyponyms; 7. meronyms; 8. holonyms;')
	print('9. heads; 10. phrases;')
	i = input('Input:')
	print("=" * 80)
	return i
	
if __name__ == "__main__":
	text = 'Mounting trade friction between the U.S. And Japan has raised fears among many of Asia\'s exporting nations that the row could inflict far-reaching economic damage, businessmen and officials said.'		
	while True:
		print("#" * 80)
		solr_search(print_info(), text)



