import pickle
tokens = pickle.load(open('tokens.dat','rb'))
keywords = pickle.load(open('keywords.dat','rb'))
lem_tokens = pickle.load(open('lem_tokens.dat','rb'))
stem_tokens = pickle.load(open('stem_tokens.dat','rb'))
pos_tag_tokens = pickle.load(open('pos_tag_tokens.dat','rb'))
heads = pickle.load(open('heads.dat','rb'))
hypernyms = pickle.load(open('hypernyms.dat','rb'))
hyponyms = pickle.load(open('hyponyms.dat','rb'))
meronyms = pickle.load(open('meronyms.dat','rb'))
holonyms = pickle.load(open('holonyms.dat','rb'))
phrases = pickle.load(open('phrases.dat','rb'))

fp = open('test2.xml','a')
fp.write('<add>\n')
'''
for i in range(0,1300):
	s0 = '<doc>\n<field name="id">%d</field>\n' %(i)
	fp.write(s0)
	for j in range(0,5):
		s = '<field name="keywords">%s</field>\n' %(str(keywords[i][j]))
		fp.write(s )
	s1 = '</doc>\n'	
	fp.write(s1)
'''
for i in range(0,1300):
	'''
	for j in range(0,5):
		s = '<field name="keywords">%s</field>\n' %(str(keywords[i][j]))
		fp.write(s)
	'''
	for z in range(len(tokens[i])):
		s0 = '<doc>\n<field name="doc_id">%d</field>\n' %(i)
		fp.write(s0)
		s1 = '<field name="sent_id">%d</field>\n' %(z)
		fp.write(s1)
		for x in range(len(tokens[i][z])):
			s = '<field name="tokens">%s</field>\n' %(str(tokens[i][z][x]))
			fp.write(s)
		for a in range(len(lem_tokens[i][z])):
			s = '<field name="lem_tokens">%s</field>\n' %(str(lem_tokens[i][z][a]))
			fp.write(s)
		for b in range(len(stem_tokens[i][z])):
			s = '<field name="stem_tokens">%s</field>\n' %(str(stem_tokens[i][z][b]))
			fp.write(s)
		for c in range(len(pos_tag_tokens[i][z])):
			s = '<field name="pos_tag_tokens">%s</field>\n' %(str(pos_tag_tokens[i][z][c]))
			fp.write(s)		
		s = '<field name="heads">%s</field>\n' %(str(heads[i][z]))
		fp.write(s)
		for e in range(len(phrases[i][z])):
			s = '<field name="phrases">%s</field>\n' %(str(phrases[i][z][e]))
			fp.write(s)	
		for f in range(len(hypernyms[i][z])):
			s = '<field name="hypernyms">%s</field>\n' %(str(hypernyms[i][z][f]))
			fp.write(s)
		for g in range(len(hyponyms[i][z])):
			s = '<field name="hyponyms">%s</field>\n' %(str(hyponyms[i][z][g]))
			fp.write(s)
		for h in range(len(meronyms[i][z])):
			s = '<field name="meronyms">%s</field>\n' %(str(meronyms[i][z][h]))
			fp.write(s)
		for k in range(len(holonyms[i][z])):
			s = '<field name="holonyms">%s</field>\n' %(str(holonyms[i][z][k]))
			fp.write(s)
		s3 = '</doc>\n'	
		fp.write(s3)
fp.write('</add>')	
fp.close()
