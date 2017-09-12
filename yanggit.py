import os

def upload(comment='allok'):
	'''
	i dislike every time to repeat every step!!!!fuck
	'''
	os.system('git add .')
	os.system('git commit -m '+str(comment))
	os.system('git push origin master')