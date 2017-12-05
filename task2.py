import pysolr
import nltk
import math
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

solr = pysolr.Solr('http://localhost:8983/solr/news2', timeout=10)
stopwords = stopwords.words('english')

def solr_search(s):
	results = solr.search(s)
	print("Saw {0} result(s).".format(len(results)))
	for result in results:
		print("The doc_id is '{0}'.".format(result['doc_id']))
		print("The sent_id is '{0}'.".format(result['sent_id']))
		print("The tokens are '{0}'.".format(result['tokens']))

text = 'Mounting trade friction between the U.S. And Japan has raised fears among many of Asia\'s exporting nations that the row could inflict far-reaching economic damage, businessmen and officials said.'	
source_text = word_tokenize(text)
str0 = ''
for word in source_text:
	if word.isalpha() and len(word)>3:
		if word not in stopwords:
			str0 = str0 + word + ','			
solr_search('tokens:%s' %(str0))


