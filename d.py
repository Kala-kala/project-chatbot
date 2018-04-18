import sqlite3
conn = sqlite3.connect('ntlk.db')
c = conn.cursor()
dict = {'Working':['Working','functioning','mechanism'],'How':['How','produced','made','exported','available'],'Location':['Location','Where','situtated','located'],'What':['What','define','mean','understand','explain']}
models = ['is', 'are']
symbols = ['.','?']
while 1==1:
		q = input(' Your question . . . \n')
		print q
		#q = "What is Cricket ? "

		q = q.split()
		for word in q: 
			if word in models:
				q.remove(word);
		print q

		for word in q: 
			if word in symbols:
				q.remove(word);

		scoreLocation = 0; scoreHow = 0;scoreWhat = 0;scoreWorking = 0;
		for word in q:
			if word in dict['Working']:
				scoreWorking = scoreWorking+1
				q.remove(word);
			if word in dict['How']:
				scoreHow = scoreHow+1
				q.remove(word);
			if word in dict['Location']:
				scoreLocation = scoreLocation+1
				q.remove(word);
			if word in dict['What']:
				scoreWhat = scoreWhat+1
				q.remove(word);
			

		if len(q)>1:
			q = q[0]+ ' ' +q[1]

		elif len(q)==1:
			q=q[0]
		print q
		score = [scoreWorking,scoreHow,scoreLocation,scoreWhat]
		print score
		a = score.index(max(score))
		print a
		c.execute(" select name from sqlite_master where type = 'table' ")
		#print  c.fetchall()[a][0]
		c.execute('SELECT * FROM location' )
		for row in c.fetchall():
				if row[0] ==q:
					print " " +row[0]+" is in: "+row[1]		

		#print params[a]
			#print "will extract db of what"
			# c.execute('SELECT * FROM what ')
			# for row in c.fetchall():
			# 	if row[0] ==q:
			# 		print " " +row[0]+" is: "+row[1]	





